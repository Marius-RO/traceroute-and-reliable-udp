import struct
import socket
import logging
import sys

MAX_UINT32 = 0xFFFFFFFF
MAX_BITI_CHECKSUM = 16
MAX_SEGMENT = 1400
MTU = 1500
TIMEOUT_FEREASTRA = 1
TIMEOUT_RECVFROM = 1
NR_MAX_INCERCARI = 20 # incercari de confirmari

def compara_endianness(numar):
    '''
    https://en.m.wikipedia.org/wiki/Endianness#Etymology
        numarul 16 se scrie in binar 10000 (2^4)
        pe 8 biti, adaugam 0 pe pozitiile mai mari: 00010000
        pe 16 biti, mai adauga un octet de 0 pe pozitiile mai mari: 00000000 00010000
        daca numaratoarea incepe de la dreapta la stanga:
            reprezentarea Big Endian (Network Order) este: 00000000 00010000
                - cel mai semnificativ bit are adresa cea mai mica
            reprezentarea Little Endian este: 00010000 00000000
                - cel mai semnificativ bit are adresa cea mai mare 
    '''
    print ("Numarul: ", numar)
    print ("Network Order (Big Endian): ", [bin(byte) for byte in struct.pack('!H', numar)])
    print ("Little Endian: ", [bin(byte) for byte in struct.pack('<H', numar)])


def flags_to_char(flags):
    if flags & 0b100:
        # S-a primit S
        return 'S'
    if flags & 0b001:
        # S-a primit F
        return 'F'
    elif flags & 0b010:
        # S-a primit P
        return 'P'

def create_header_emitator(seq_nr, checksum, flags):
    '''
    TODO: folosind struct.pack impachetati numerele in octeti si returnati valorile
    flags pot fi 'S', 'P', sau 'F'
    '''

    if flags == 'S':
    # inseamna ca am trimis S
        spf = 0b100
    if flags == 'P':
    # inseamna ca am trimis P
        spf = 0b010
    if flags == 'F':
    # inseamna ca am trimis F
        spf = 0b001

    spf_zero = spf << 13 # muta cei trei biti cu 13 pozitii la stanga
    # L+H+H = 4+2+2 = 8
    header = struct.pack('!LHH', seq_nr, checksum, spf_zero)

    return header


def parse_header_emitator(octeti):
    '''
    TODO: folosind struct.unpack despachetati numerele 
    din headerul de la emitator in valori si returnati valorile
    '''

    header = octeti[:8]
    seq_nr, checksum, spf_zero = struct.unpack('!LHH', header)

    # eliminam cele 13 zerouri de padding
    flags = spf_zero >> 13

    return (seq_nr, checksum, flags)


def create_header_receptor(ack_nr, checksum, window):
    '''
    TODO: folosind struct.pack impachetati numerele in octeti si returnati valorile
    flags pot fi 'S', 'P', sau 'F'
    '''

    octeti = struct.pack('!LHH', ack_nr, checksum, window)
    return octeti


def parse_header_receptor(octeti):
    '''
    TODO: folosind struct.unpack despachetati octetii in valori si returnati valorile
    '''
    ack_nr, checksum, window = struct.unpack('!LHH', octeti)
    return (ack_nr, checksum, window)

def extrage_segmente(file_descriptor):
    # extrag toate segmentele de 1400 de octeti din fisier
    segmente = []
    while True:
        segment = file_descriptor.read(MAX_SEGMENT)
        if segment:
            #yield segment
            segmente.append(segment)
        else:
            break

    return segmente    


def exemplu_citire(cale_catre_fisier):
    with open(cale_catre_fisier, 'rb') as file_in:
        segmente = extrage_segmente(file_in)
        for segment in segmente:
            print(segment)


def complement(num):
    c = 1
 
    while num*2 > c:
        num = num ^ c
        c = c << 1
 
    return num

def calculeaza_checksum(octeti):

    checksum = 0

    if len(octeti) % 2 == 1:
        # Adaugam '\0' in cazul in care sirul este de lungime impara
        octeti += b'\0'
      
    # Despachetam in bucati de cate 2 bytes
    bucati = struct.unpack('!%dH' % (len(octeti)//2), octeti)

    # Este variabila din python, nu este pe 2 bytes
    checksum = 0
    for i in range(len(bucati)):
        # Facem suma bucatilor
        checksum += bucati[i]

    # Convertim numarul la un unsigned short
    # Ar rezulta numarul de dupa overflow 65535 (restul impartirii la 65535)
    checksum = checksum % 65535

    # Calculam complementul sumei
    checksum = complement(checksum)
    return checksum


def verifica_checksum(octeti):
    if calculeaza_checksum(octeti) == 0:
        return True
    return False



if __name__ == '__main__':
    compara_endianness(16)