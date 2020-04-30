# emitator Reliable UDP
from helper import *
from argparse import ArgumentParser
import logging
import sys
import struct
import random
import time
from copy import deepcopy

SEG = 0

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

def connect(sock, adresa_receptor):
    '''
    Functie care initializeaza conexiunea cu receptorul.
    Returneaza ack_nr de la receptor si window
    '''

    seq_nr = random.randint(0, 200000) # setam initial sequence number
    flags = 'S'
    checksum = 0
    octeti_header_fara_checksum = create_header_emitator(seq_nr, checksum, flags)

    segment = struct.pack('!16s',"Vreau conexiune!".encode("utf-8"))
    mesaj = octeti_header_fara_checksum + segment

    logging.info(f"Am trimis cererea de conectare cu flagul S catre {adresa_receptor}")

    for i in range(NR_MAX_INCERCARI):

        # incerc trimiterea cererii de conectare initala
        try:
            sock.sendto(mesaj, adresa_receptor)
            data, receptor = sock.recvfrom(MTU)
        except socket.timeout as e:
            logging.info("Timeout la connect flag S, retrying...")
            continue # cat timp nu primește confirmare de connect, incearca din nou


        # in acest moment cerera a fost trimisa si s-a primit raspuns de la receptor
        logging.info(f"Cererea de conectare cu flagul S a fost primita de {adresa_receptor}")
        logging.info(f"Header cerere trimisa: [seq_nr: {seq_nr}] , [check:  {checksum}] , [flag: {flags}]")

        ack_nr, checksum, window = parse_header_receptor(data)
        logging.info(f"Header receptor primit: [ack_nr: {ack_nr}] , [check:  {checksum}] , [window: {window}]")
        logging.info(f"S-a realizat conexiunea")
        logging.info(f"")

        return ack_nr, window
        
    else: # nu s-a reusit trimiterea dupa un nr de NR_MAX_INCERCARI retransmisii
        logging.info(f"Receptorul {adresa_receptor} nu a raspuns dupa {NR_MAX_INCERCARI} incercari de conectare.")
        logging.info("Trimiterea pachetelor a fost anulata")
        sys.exit(0)


def finalize(sock, adresa_receptor, seq_nr):
    '''
    Functie care trimite mesajul de finalizare
    cu seq_nr dat ca parametru.
    '''
    # TODO:
    # folositi pasii de la connect() pentru a construi headerul
    # valorile de checksum si pentru a verifica primirea mesajului a avut loc

    return 0  


def send(sock, adresa_receptor, seq_nr, window, segment):
    '''
    Functie care trimite octeti ca payload catre receptor
    cu seq_nr dat ca parametru.
    Returneaza ack_nr si window curent primit de la server.
    '''
    # TODO...
    checksum = 0
    octeti_header_fara_checksum = create_header_emitator(seq_nr, checksum, "P")

    mesaj = octeti_header_fara_checksum + segment

    #checksum = calculeaza_checksum(mesaj)
    #octeti_header_cu_checksum = create_header_emitator(seq_nr, checksum, "P")
    # mesaj = octeti_header_cu_checksum + segment

    #logging.info(f"\nAm trimis cererea de conectare cu flagul S catre {adresa_receptor}")

    
    global SEG
    logging.info(f"Incerc trimitere segmentului {SEG}")
    for i in range(NR_MAX_INCERCARI):
        
        # incerc trimiterea segmentului
        try:
            sock.sendto(mesaj, adresa_receptor)
            data, receptor = sock.recvfrom(MTU)
        except socket.timeout as e:
            logging.info("Timeout la connect segment, retrying...")
            continue # TODO: cat timp nu primește confirmare de connect, incearca din nou


        # in acest moment cerera a fost trimisa si s-a primit raspuns de la receptor
        #logging.info(f"Cererea de conectare cu flagul S a fost primita de {adresa_receptor}")
        logging.info(f"Header cerere: [seq_nr: {seq_nr}] , [check:  {checksum}] , [flag: P]")

        # if verifica_checksum(data) is False:
        #     #daca checksum nu e ok, mesajul de la receptor trebuie ignorat
        #     return -1, -1

        ack_nr, checksum, window = parse_header_receptor(data)

        if ack_nr == seq_nr + len(segment): # am primit confirmarea potrivita
            logging.info(f"Header receptor primit: [ack_nr: {ack_nr}] , [check:  {checksum}] , [window: {window}]")
            logging.info(f"Am trimis segmentul {SEG} cu succes")
            SEG += 1
            return ack_nr, window
     
    else: # nu s-a reusit trimiterea dupa un nr de NR_MAX_INCERCARI retransmisii
        logging.info(f"Receptorul {adresa_receptor} nu a raspuns dupa {NR_MAX_INCERCARI} incercari de conectare.")
        logging.info("Trimiterea pachetelor va fi reluata")
        return -1, window
        #exit(0)


def send_segment(sock, adresa_receptor, seq_nr, window, segment, idx_segment):
    
    # checksum = calculeaza_checksum(segment)
    checksum = 0
    octeti_header_fara_checksum = create_header_emitator(seq_nr, checksum, "P")
    mesaj = octeti_header_fara_checksum + segment

    #checksum = calculeaza_checksum(mesaj)
    #octeti_header_cu_checksum = create_header_emitator(seq_nr, checksum, "P")
    # mesaj = octeti_header_cu_checksum + segment

    logging.info(f"Header segment {idx_segment} trimis: [seq_nr: {seq_nr}] , [check:  {checksum}] , [flag: P]")
    sock.sendto(mesaj, adresa_receptor)
         

def preia_confirmari_fereastra(sock):

    logging.info("Preluare confirmari")

    # setez temporar timeoutul cu 0 pt ca o sa preiau ceea ce a venit in timeoutul ferestrei
    sock.settimeout(0)

    # setez socketul sa nu se blocheze daca se incearca citirea si nu contine date (voi prelua toate confirmarile din buffer)
    sock.setblocking(0)

    lista_confirmari = []
    try:
        while True:
            confirmare, receptor = sock.recvfrom(MTU)
            header = parse_header_receptor(confirmare[:8])

            # adaug confirmarea o singura data in lista pt a nu exista duplicate
            if header not in lista_confirmari:
                lista_confirmari.append(header)

    except socket.error as e: # s-au terminat de citit confirmarile din buffer

        logging.info(f"Confirmari preluate = {len(lista_confirmari)}")

        # setez inapoi socketul cu setarile initale
        sock.settimeout(TIMEOUT_RECVFROM)
        sock.setblocking(1) # socketul nu se blocheaza daca se incearca citirea si nu contine date
        
        return lista_confirmari


def trimite_segmente(sock, adresa_receptor, segmente, window):
    # functia care implementeaa mecanismul sliding window Go Back N

    # generez seq number de start pt trimiterea pachetelor
    seq_nr = random.randint(0, 200000)
    
    # indecsi pentru gestionarea ferestrelor si ale segmentelor
    idx_start_fereastra = 0
    idx_final_fereastra = window - 1
    idx_segment_start = 0
    seq_nr_segment_start = seq_nr
    cnt_segmente = 0
    nr_segmente = len(segmente)

    # tuplu de tipul (idx_segment, seq_nr_trimis, ack_nr_asteptat)
    lista_info_segmente_trimise_fereastra = [] 
    
    # lista confirmarilor primite pentru fiecare incercare de trimitere a pachetelor
    lista_confirmari = []

    # voi salva indecsii pentru segmentele confirmate de receptor
    lista_idx_segmente_confirmate = []

    while True:
        # Din while se iese doar daca s-au primit confirmarile pentru toate segmentele
        # exista un return intr-o ramura else 
        
        logging.info("")
        logging.info(f"--------------------------------")
        logging.info(f"Se transmite fereastra {idx_start_fereastra} - {idx_final_fereastra}")
        logging.info(f"--------------------------------")

        # parcurgem segmentele din fereastra
        for i in range(idx_start_fereastra, idx_final_fereastra + 1):
            # daca mai sunt segmente de transmis
            if cnt_segmente < nr_segmente:
                # setam noul segment de start din fereastra (dupa el o sa se decida avansarea ferestrei catre dreapta)
                if i == idx_start_fereastra:
                    idx_segment_start = cnt_segmente
                    seq_nr = seq_nr_segment_start
                
                # verific daca segmentul nu fost deja trimis si confirmat de receptor
                # poate fi un sgement intermediar care la o iteratie anterioara a fost trimis
                # (se face retransmisia doar pt pachetele care nu au fost confirmate)
                if cnt_segmente in lista_idx_segmente_confirmate:
                    seq_nr += len(segmente[cnt_segmente])
                    cnt_segmente += 1
                    continue    

                # daca nu a fost confirmat il trimit / retrimit
                segment = segmente[cnt_segmente]
                send_segment(sock, adresa_receptor, seq_nr, window, segment, cnt_segmente)

                # salvez detalii (idx_segment, seq_nr_trimis, ack_nr_asteptat) despre segmentul trimis
                lista_info_segmente_trimise_fereastra.append((cnt_segmente,seq_nr,seq_nr + len(segment)))

                # incrementez noile valori
                seq_nr += len(segment) + 1
                cnt_segmente += 1

        
        # simuleaza timeout-ul ferestrei (asteptarea pana se verifica daca pachetele au ajuns)
        time.sleep(TIMEOUT_FEREASTRA)

        # extrag confirmarile primite si verific care pachete au fost trimise
        lista_confirmari = preia_confirmari_fereastra(sock)
        
        # pe baza confirmarilor creez o lista de ack_primite
        lista_ack_primite = []

        # parcurg confrimarile si extrag ack
        for confirmare in lista_confirmari:
            ack_nr, checksum, window = confirmare[0], confirmare[1], confirmare[2]
            logging.info(f"Header receptor pt segment primit: [ack_nr: {ack_nr}] , [check:  {checksum}] , [window: {window}]")
            lista_ack_primite.append(ack_nr)   

        # copiez lista segmentelor trimise
        aux_info_segmente_trimise = deepcopy(lista_info_segmente_trimise_fereastra)

        # si elimin din lista segmentelor trimise acele segmente pentru care am primit confirmare
        for info_segment in aux_info_segmente_trimise:
            # daca ack_trimis de emitator exista in lista de ack_primite de la receptor
            if info_segment[2] in lista_ack_primite: 
                # elimin segmentul
                lista_info_segmente_trimise_fereastra.remove(info_segment)

                # si adaug indexul segmentului in lista segmentelor confirmate doar daca nu exista deja
                # si daca mai au sens (adica nu sunt confirmari pentru segmente deja marca ca fiin confirmate)
                if info_segment[0] not in lista_idx_segmente_confirmate and info_segment[0] >= idx_segment_start:
                    lista_idx_segmente_confirmate.append(info_segment[0])
        
        # sortez lista indecsilor crescator astfel incat sa preiau mereu in ordine din stanga spre dreapta
        lista_idx_segmente_confirmate.sort()
        logging.info(f"Idx segmente confirmate: {lista_idx_segmente_confirmate}")

        # verific primele cate segmente din stanga au fost trimise pt a sti cu cat sa avansez fereastra spre dreapta
        # astfel ca parcurg lista indecsilor segmentelor trimise
        nr_confirmari_consecutive = 0
        while True:
            # daca primul segmentul din stanga a fost trimis
            if idx_segment_start in lista_idx_segmente_confirmate:
                # ii scot indexul din lista segmentelor confirmate
                lista_idx_segmente_confirmate.remove(idx_segment_start)

                # fereastra mai poate avansa cu o unitate
                nr_confirmari_consecutive += 1

                # si daca mai pot trece la urmatorul index (daca nu s-au terminat segmentele)
                if idx_segment_start + 1 < nr_segmente:
                    # actualizez noul seq_start
                    seq_nr_segment_start += len(segmente[idx_segment_start])

                    # si trec la urmatorul segment
                    idx_segment_start += 1

                else: # toate segmentele au fost trimise si confirmate
                    logging.info("")
                    logging.info("S-au trimis toate segmentele")

                    return
                    
            else:   # daca fereastra a fost trimisa complet sau                         
                    # daca un anumit segment nu a fost confirmat pana in acest moment   
                    # atunci fereastra va avansa cu nr_confirmari_consecutive
                idx_start_fereastra += nr_confirmari_consecutive
                idx_final_fereastra += nr_confirmari_consecutive
                cnt_segmente = idx_segment_start

                # si revin la seq_nr de la inceputul trimiterii segementelor din fereastra
                seq_nr = seq_nr_segment_start

                break        
        
        logging.info("")
        logging.info(f"Fereastra a avansat cu {nr_confirmari_consecutive} pozitii.")
        
        

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
    sock.settimeout(TIMEOUT_RECVFROM)

    try:
         # trimit cererea de conectare cu flagul 'S' (incerc sa stabilesc conexiunea cu receptorul)
        ack_nr, window = connect(sock, adresa_receptor)
        
        # in acest moment conectarea a reusit ( daca nu reuseste conectarea programul se termina in functia connect)
        file_descriptor = open(fisier, 'rb')
        
        # extrag initial toate segmentele
        segmente = extrage_segmente(file_descriptor)

        # trimit segmentele folosind mecanismul sliding window Go Back N
        trimite_segmente(sock, adresa_receptor,segmente, window)

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