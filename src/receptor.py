# receptor Reiable UDP
from helper import *
from argparse import ArgumentParser
import logging
import random

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

last_window_size = None
WINDOW_VARIABIL = False

def trimitere_confirmari(sock,emitator,flags,seq_nr,checksum,payload):
    
    # # verificam ce flag am primit
    # if flags & 0b100 or flags & 0b001: # inseamna ca am primit S sau F
    #     ack_nr = seq_nr + 1 # +1 -> pt ca nu exista payload pt aceste cereri
    # elif flags & 0b010: # inseamna ca am primit P ( deci exista posibilitatea de payload )
    #     ack_nr = seq_nr + len(payload) # ack_nr va specifica cat payload a fost primit

    # verificam ce flag am primit
    flag = flags_to_char(flags)
    if flag == 'S' or flag == 'F':
        ack_nr = seq_nr + 1 # +1 -> pt ca nu exista payload pt aceste cereri
    elif flag == 'P':
        ack_nr = seq_nr + len(payload) # ack_nr va specifica cat payload a fost primit

    checksum = 55
    #window = random.randint(1, 5)
    window = 2

    # impachetam nou header
    octeti = struct.pack('!LHH', ack_nr, checksum, window)

    # trimitem pachetul
    logging.info(f"Se trimit {NR_MAX_INCERCARI} confirmari")
    # avand in vedere pocket loss trimite NR_MAX_INCERCARI confirmari catre emitator
    for i in range(NR_MAX_INCERCARI):
        sock.sendto(octeti, emitator)

    # nu ne intereseaza confirmari din partea emitatorului => daca emitatorul nu primeste confirmarile
    # datorita packet loss atunci el va retrimite acele pachete pt care nu a primit confirmari
    # iar receptorul va trimite noi confirmari
    logging.info(f"Header receptor trimis: [ack_nr: {ack_nr}] , [check:  {checksum}] , [window: {window}]")         
    logging.info(f"S-au trimis {NR_MAX_INCERCARI} confirmari")
    
    # Daca nu lucram cu WINDOW VARIABIL, stocam toate mesajele intr-o lista
    # pe care o vom sorta dupa acknowledgements si o vom scrie la final in fisier.
    lista_segmente = []
        

def main():
    parser = ArgumentParser(usage=__file__ + ' '
                                             '-p/--port PORT'
                                             '-f/--fisier FILE_PATH',
                            description='Reliable UDP Receptor')

    parser.add_argument('-p', '--port',
                        dest='port',
                        default='10000',
                        help='Portul pe care sa porneasca receptorul pentru a primi mesaje')

    parser.add_argument('-f', '--fisier',
                        default='fisier_primit',
                        dest='fisier',
                        help='Calea catre fisierul in care se vor scrie octetii primiti')

    # Parse arguments
    args = vars(parser.parse_args())
    port = int(args['port'])
    fisier = args['fisier']
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)
    
    adresa = '0.0.0.0'
    server_address = (adresa, port)
    sock.bind(server_address)
    logging.info("Serverul a pornit pe %s si portul %d", adresa, port)
    
    if WINDOW_VARIABIL is True:
        # Facem un fisier cu numele primit din linia de comanda 
        # In cazul in care acesra exista deja, va fi golit (overwrite)
        # prin deschiderea in modul de citire
        # w+  create file if it doesn't exist and open it in (over)write mode
        file_descriptor = open(fisier, 'wb+')
        # Inchidem fisierul pentru a-l putea deschide in modul append
        file_descriptor.close()
        # folosim a in loc de a+ pentru ca stim ca exista fisierul
        file_descriptor = open(fisier, "ab")

    if WINDOW_VARIABIL is False:
        # Initializam o lista de seq-uri + mesaje primite,
        # pe care o vom sorta dupa seq. si o vom scrie in fisier la finalul programului
        lista_segmente = []

    while True:
        logging.info('Asteptam mesaje...')
        data, emitator = sock.recvfrom(MTU)

        logging.info("Am primit %s octeti de la %s", len(data), emitator)
        logging.info('Content primit: "%s"', data)

        '''
        TODO: pentru fiecare mesaj primit
        1. verificam checksum
        2. parsam headerul de la emitator
        3. trimitem confirmari cu ack = seq_nr+1 daca mesajul e de tip S sau F
                               cu ack = seq_nr daca mesajul e de tip P
        4. scriem intr-un fisier octetii primiti
        5. verificam la sfarsit ca fisierul este la fel cu cel trimis de emitator
        '''
        
        # 2. parsare header de la emitator
        seq_nr, checksum, flags = parse_header_emitator(data)
        logging.info(f"Header emitator primit: [seq_nr: {seq_nr}] , [check:  {checksum}] , [flag: {flags}]")


        # 1. Verificare checksum
        #checksum = calculeaza_checksum()  # se calculeaza checksumul pt pachetul primit
        #
        # si se verifica daca este corect
        #
        #
        # daca nu este corect ignoram pachetul
        # if checksum nu este corect:
        #            continue


        # stim ca checksumul este corect => trimitem confirmari pentru pachet
        # 3. trimitere confirmari
        trimitere_confirmari(sock,emitator,flags,seq_nr,checksum,data[8:])
        flag = flags_to_char(flags)

        print("-------------FLAG: -------", flag)

        if flag == 'P':
            # S-a primit mesaj cu date
            # 4. scriere in fisier
            # Adaugam payload-ul primit
            if WINDOW_VARIABIL is True:
                # TODO: Salvare dinamica.
                fisier.write(data[8:0])
                #file_descriptor.write(data[8:])
                file_descriptor.close()

            if WINDOW_VARIABIL is False:
                exista_seq = False
                for segment in lista_segmente:
                    if segment[0] == seq_nr:
                        exista_seq = True
                        break
                if exista_seq is False:
                    lista_segmente.append((seq_nr, data[8:]))
        
        if flag == 'F':
        # S-a primit semnalul de finalizare.
        # Nu mai ascultam mesajele primite.
            break

        # TEST
        # if WINDOW_VARIABIL is False:
        #     if len(lista_segmente) == 7:
        #         break

    if WINDOW_VARIABIL is False:
        # Cream fisierul in care vom scrie datele primite
        # In cazul in care nu exista, se va crea unul nou
        # Altfel se va suprascrie informatia
        # Sortam lista dupa seq_number
        lista_segmente = sorted(lista_segmente, key=lambda x: x[0])
        print(lista_segmente[0])
        file_descriptor = open(fisier, "wb+")
        # Scriem segmentele in fisier
        for segment in lista_segmente:
            file_descriptor.write(segment[1])
        file_descriptor.close()
    
     # 5. verificare ca fisierul este la fel

def bswitch(num):
    c = 1
 
    while num*2 > c:
        num = num ^ c
        c = c << 1
 
    return num
    
def calc_checksum(octeti):
    # Conversie string la bytes
    # data_bytes = bytes(data, 'utf-8')

    # Nu cred ca mai este nevoie de linia de mai jos
    # octeti = struct.pack('!%ds' % len(data), data_bytes)

    if len(octeti) % 2 == 1:
        # Adaugam '\0' in cazul in care sirul este de lungime impara
        octeti += b'\0'
      
    # print(data_bytes)
    # print(octeti)

    # Despachetam in bucati de cate 2 bytes
    bucati = struct.unpack('%dH' % (len(octeti)//2), octeti)
    print(bucati)

    # Nu este pe 2 bytes
    suma = 0
    for i in range(len(bucati)):
        # Facem suma bucatilor
        # print(bucati[i])
        suma += bucati[i]
        # print(suma)

    print("suma: ", suma)


    # Convertim numarul la un unsigned short
    # 0xffff = MAX_UNSIGNED_SHORT
    # Ar rezulta numarul de dupa overflow 65535 (restul impartirii la 65535)
    # Practic luam cei mai semnificativi 16 biti
    suma = suma & 0xffff
    print("suma dupa conversie la !H: ", suma)

    # Calculam complementul sumei
    print("Inainte de complement: ", bin(suma), "dec: ", suma)
    suma = bswitch(suma)
    print("Dupa complement: ", bin(suma), "dec: ", suma)

    # Impachetam suma intr-un unsigned short (2 bytes)
    # suma = struct.pack('!H', suma)
    print("suma returnata: ", suma)
    return suma

# def check_checksum():


if __name__ == '__main__':
    # main()

    # HEADER CU CHECKSUM 0 INITIAL 

    # seq_nr = random.randint(0, 200000) # setam initial sequence number
    seq_nr = 5
    flags = 'S'
    checksum = 0
    octeti_header_fara_checksum = create_header_emitator(seq_nr, checksum, flags)

    segment = struct.pack('!16s',"Vreau conexiune!".encode("utf-8"))
    mesaj = octeti_header_fara_checksum + segment
    print("Mesaj pentru calculat checksum: ", mesaj)

    checksum_res = calc_checksum(mesaj)
    # REFACERE HEADER CU CHECKSUMUL CALCULAT ANTERIOR 
    # ACEST HEADER SE VA TRIMITE LA RECEPTOR
    octeti_header_fara_checksum = create_header_emitator(seq_nr, checksum_res, flags)
    mesaj = octeti_header_fara_checksum + segment
    print("Mesaj cu checksumul calculat", mesaj)

    # SINGURA DIFERENTA INTRE CELE 2 MESAJE IN MOMENTUL CALCULARII SUMEI
    # ESTE A 3 A BUCATA DE 2 BYTES.

    # APLICARE CHECKSUM PESTE HEADER-UL FACUT MAI SUS
    # PENTRU A VERIFICA DACA DA 0
    checksum_res2 = calc_checksum(mesaj)
    print("Res: ", checksum_res2)


