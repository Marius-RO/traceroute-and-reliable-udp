# receptor Reiable UDP
from helper import *
from argparse import ArgumentParser
import logging
import random
import filecmp
import time

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

NUME_FISIER_PRIMIT = None
NUME_FISIER_SALVAT = None
# Setati pe un numar mare daca va grabiti :)
MAX_WINDOW_SIZE = 5

def trimitere_confirmari(sock,emitator,flags,seq_nr,payload):

    # verificam ce flag am primit
    flag = flags_to_char(flags)
    if flag == 'S' or flag == 'F':
        ack_nr = seq_nr + 1 # +1 -> pt ca nu exista payload pt aceste cereri
    elif flag == 'P':
        ack_nr = seq_nr + len(payload) # ack_nr va specifica cat payload a fost primit

    window = random.randint(1, MAX_WINDOW_SIZE)

    # impachetam header-ul fara checksum
    checksum = 0
    octeti_header_fara_checksum = struct.pack('!LHH', ack_nr, checksum, window)

    # impachetam noul header cu checksum calculat
    checksum = calculeaza_checksum(octeti_header_fara_checksum)
    octeti_header_cu_checksum = struct.pack('!LHH', ack_nr, checksum, window)

    # trimitem pachetul
    logging.info(f"Se trimit {NR_MAX_INCERCARI} confirmari")
    # avand in vedere pocket loss trimite NR_MAX_INCERCARI confirmari catre emitator
    for i in range(NR_MAX_INCERCARI):
        sock.sendto(octeti_header_cu_checksum, emitator)

    # nu ne intereseaza confirmari din partea emitatorului => daca emitatorul nu primeste confirmarile
    # datorita packet loss atunci el va retrimite acele pachete pt care nu a primit confirmari
    # iar receptorul va trimite noi confirmari

    logging.info(f"Header receptor trimis: [ack_nr: {ack_nr}] , [check:  {checksum}] , [window: {window}]")         
    logging.info(f"S-au trimis {NR_MAX_INCERCARI} confirmari")   
    logging.info(f"")     


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
    NUME_FISIER_SALVAT = fisier

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)
    
    adresa = '0.0.0.0'
    server_address = (adresa, port)
    sock.bind(server_address)
    logging.info("Serverul a pornit pe %s si portul %d", adresa, port)
    
    # Initializam o lista de seq-uri + mesaje primite,
    # pe care o vom sorta dupa seq. si o vom scrie in fisier la finalul programului
    lista_segmente = []

    while True:
        logging.info('Asteptam mesaje...')
        data, emitator = sock.recvfrom(MTU)
        logging.info("Am primit %s octeti de la %s", len(data), emitator)
        
        
        # 1. Parsare header de la emitator
        seq_nr, checksum, flags = parse_header_emitator(data)
        flag = flags_to_char(flags)
        logging.info(f"Header emitator primit: [seq_nr: {seq_nr}] , [check:  {checksum}] , [flag: {flag}]")


        # 2. Verificare checksum
        # Verifica integritatea pachetului
        if not verifica_checksum(data):
            continue

        # stim ca checksumul este corect => trimitem confirmari pentru pachet
        # 3. trimitere confirmari
        trimitere_confirmari(sock,emitator,flags,seq_nr,data[8:]) 

        if flag == 'S':
            # S-a primit mesajul de conectare care contine in payload numele fisierlui
            NUME_FISIER_PRIMIT = struct.unpack('%ds' % len(data[8:]), data[8:])[0]

        if flag == 'P':
            # S-a primit mesaj cu date
            # 4. scriere in fisier
            # Adaugam payload-ul primit
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

    # --- SALVARE IN FISIER ---
    # Cream fisierul in care vom scrie datele primite
    # In cazul in care nu exista, se va crea unul nou
    # Altfel se va suprascrie informatia
    # Sortam lista dupa seq_number
    lista_segmente = sorted(lista_segmente, key=lambda x: x[0])
    file_descriptor = open(fisier, "wb+")

    # Scriem segmentele in fisier
    for segment in lista_segmente:
        file_descriptor.write(segment[1])
    file_descriptor.close()
    logging.info(f"Transferul a fost incheiat cu succes! :)")

    
    # 5. verificare ca fisierul este la fel

    if filecmp.cmp(NUME_FISIER_PRIMIT, NUME_FISIER_SALVAT):
        logging.info("Fisierul este integru. :)")
    else:
        logging.info("Fisierul nu este integru! :(")    

if __name__ == '__main__':
    main()



