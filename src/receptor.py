# receptor Reiable UDP
from helper import *
from argparse import ArgumentParser
import socket
import logging
import random

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

def trimitere_confirmari(sock,emitator,flags,seq_nr,checksum,payload):
    
    # verificam ce am primit
    if flags & 0b100 or flags & 0b001: # inseamna ca am primit S sau F
        ack_nr = seq_nr + 1 # +1 -> pt ca nu exista payload pt aceste cereri
    elif flags & 0b010: # inseamna ca am primit P
        ack_nr = seq_nr + len(payload) # ack_nr va specifica cat payload a fost primit

    #checksum = 0
    checksum = 55
    #window = random.randint(1, 5)
    window = 74

    # trimitem confirmarea
    octeti = struct.pack('!LHH', ack_nr, checksum, window)
    sock.sendto(octeti, emitator)
    logging.info(f"\nAm trimis confirmarea cu: [ack_nr: {ack_nr}] , [check:  {checksum}] , [window: {window}]")


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
        data, emitator = sock.recvfrom(MAX_SEGMENT)

        logging.info("Am primit %s octeti de la %s", len(data), emitator)
        logging.info('\nContent primit: "%s"', data)

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
        logging.info(f"\nHeader emitator primit: [seq_nr: {seq_nr}] , [check:  {checksum}] , [flag: {flags}]")


        # 1. Verificare checksum
        

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

