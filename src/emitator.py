# emitator Reliable UDP
from helper import *
from argparse import ArgumentParser
import socket
import logging
import sys
import struct
import random

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

def connect(sock, adresa_receptor):
    '''
    Functie care initializeaza conexiunea cu receptorul.
    Returneaza ack_nr de la receptor si window
    '''

    seq_nr = random.randint(0, 200000) # TODO: setati initial sequence number
    flags = 'S'
    checksum = 0
    octeti_header_fara_checksum = create_header_emitator(seq_nr, checksum, flags)

    segment = struct.pack('!16s',"Vreau conexiune!".encode("utf-8"))
    mesaj = octeti_header_fara_checksum + segment

    # checksum = calculeaza_checksum(mesaj)
    # octeti_header_cu_checksum = create_header_emitator(seq_nr, checksum, flags)
    # mesaj = octeti_header_cu_checksum + segment


    logging.info(f"\nAm trimis cererea de conectare cu flagul S catre {adresa_receptor}")

    NR_MAX_INCERCARI = 2
    for i in range(NR_MAX_INCERCARI):

        # incerc trimiterea cererii de conectare initala
        try:
            sock.sendto(mesaj, adresa_receptor)
            data, receptor = sock.recvfrom(MAX_SEGMENT)
        except socket.timeout as e:
            logging.info("Timeout la connect, retrying...")
            continue # TODO: cat timp nu primește confirmare de connect, incearca din nou


        # in acest moment cerera a fost trimisa si s-a primit raspuns de la receptor
        logging.info(f"Cererea de conectare cu flagul S a fost primita de {adresa_receptor}")
        logging.info(f"Header cerere: [seq_nr: {seq_nr}] , [check:  {checksum}] , [flag: {flags}]")

        # if verifica_checksum(data) is False:
        #     #daca checksum nu e ok, mesajul de la receptor trebuie ignorat
        #     return -1, -1

        ack_nr, checksum, window = parse_header_receptor(data)
        logging.info(f"\nHeader receptor primit: [ack_nr: {ack_nr}] , [check:  {checksum}] , [window: {window}]")

        return ack_nr, window
        
    else: # nu s-a reusit trimiterea dupa un nr de NR_MAX_INCERCARI retransmisii
        logging.info(f"Receptorul {adresa_receptor} nu a raspuns dupa {NR_MAX_INCERCARI} incercari de conectare.")
        logging.info("Trimiterea pachetelor a fost anulata")
        exit(0)


def finalize(sock, adresa_receptor, seq_nr):
    '''
    Functie care trimite mesajul de finalizare
    cu seq_nr dat ca parametru.
    '''
    # TODO:
    # folositi pasii de la connect() pentru a construi headerul
    # valorile de checksum si pentru a verifica primirea mesajului a avut loc

    return 0  


def send(sock, adresa_receptor, seq_nr, window, octeti_payload):
    '''
    Functie care trimite octeti ca payload catre receptor
    cu seq_nr dat ca parametru.
    Returneaza ack_nr si window curent primit de la server.
    '''
    # TODO...

    return ack_nr, window


def main():
    parser = ArgumentParser(usage=__file__ + ' '
                                             '-a/--adresa IP '
                                             '-p/--port PORT'
                                             '-f/--fisier FILE_PATH',
                            description='Reliable UDP Emitter')

    parser.add_argument('-a', '--adresa',
                        dest='adresa',
                        default='198.8.0.2', # default 198.8.0.2 (receptor nu a functionat)
                        help='Adresa IP a receptorului (IP-ul containerului, localhost sau altceva)')

    parser.add_argument('-p', '--port',
                        dest='port',
                        default='10000',
                        help='Portul pe care asculta receptorul pentru mesaje')

    parser.add_argument('-f', '--fisier',
                        dest='fisier',
                        help='Calea catre fisierul care urmeaza a fi trimis')

    # Parse arguments
    args = vars(parser.parse_args())
    ip_receptor = args['adresa']
    port_receptor = int(args['port'])
    fisier = args['fisier']

    adresa_receptor = (ip_receptor, port_receptor)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)

    # setam timeout pe socket in cazul in care recvfrom nu primeste nimic in 3 secunde
    sock.settimeout(3)

    try:
         # trimit cererea de conectare cu flagul 'S' (incerc sa stabilesc conexiunea cu receptorul)
        ack_nr, window = connect(sock, adresa_receptor)

        # in acest moment conectarea a reusit ( daca nu reuseste conectarea programul se termina in functia connect)
        file_descriptor = open(fisier, 'rb')
        
        # extrag initial toate segmentele
        segmente = extrage_segmente(file_descriptor)

        ## TODO: send trebuie sa trimită o fereastră de window segmente
        # până primeste confirmarea primirii tuturor segmentelor

        # parcurg toate segmentele si extrag cate window segmente dupa care verific daca
        # au fost trimis si apoi continui pana ce nu mai sunt segmente deci s-a trimis totul
        #
        #
        # while True:
            #segment = citeste_segment(file_descriptor)
            #ack_nr, window = send(sock, adresa_receptor, seq_nr, window, segment)
        

        # in acest moment s-au trimis toate segmentele astfel ca
        # trimit cererea de conectare cu flagul 'F' (incerc sa inchei conexiunea cu receptorul)
        #finalize(sock, adresa_receptor)

    except Exception as e:
        logging.exception(traceback.format_exc())
        sock.close()
        file_descriptor.close() 
    finally:
        file_descriptor.close()
        sock.close()
    
if __name__ == '__main__':
    #exemplu_citire("text.txt")
    main()