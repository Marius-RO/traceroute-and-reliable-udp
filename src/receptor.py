# receptor Reiable UDP
from helper import *
from argparse import ArgumentParser
import logging
import random

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

def trimitere_confirmari(sock,emitator,flags,seq_nr,checksum,payload):
    
    # verificam ce flag am primit
    if flags & 0b100 or flags & 0b001: # inseamna ca am primit S sau F
        ack_nr = seq_nr + 1 # +1 -> pt ca nu exista payload pt aceste cereri
    elif flags & 0b010: # inseamna ca am primit P ( deci exista posibilitatea de payload )
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


        # 4. scriere in fisier
        fisier = 'text_scris.txt'
        file_descriptor = open(fisier, 'ab')
        file_descriptor.write(data[8:])
        file_descriptor.close()


        # 5. verificare ca fisierul este la fel
        
    
if __name__ == '__main__':
    main()

