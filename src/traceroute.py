import socket
import traceback
import requests
import struct
import random

# socket de UDP
udp_send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)

# socket RAW de citire a răspunsurilor ICMP
icmp_recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
# setam timout in cazul in care socketul ICMP la apelul recvfrom nu primeste nimic in buffer
icmp_recv_socket.settimeout(1)

MAX_TTL = 64

def traceroute(ip, port):
    # setam TTL in headerul de IP pentru socketul de UDP
    TTL = 0 
    lista_ips = [] # o lista in care adaugam ip urile din ruta ip ului pt care ii cautam ruta

    while True:
        # Evitam blocarea pe un anumit IP (primirea de socket timeout de foarte multe ori)
        if TTL == MAX_TTL:
            print("\nS-a atins limita maxima de TTL. Oprim cautarea...")
            break

        TTL += 1  # crestem TTL pana ce ajungem la ip ul final
        udp_send_sock.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, TTL)
        
        # trimite un mesaj UDP catre un tuplu (IP, port) 
        udp_send_sock.sendto(b'salut', (ip, port))
        
        # asteapta un mesaj ICMP de tipul ICMP TTL exceeded messages
        # in cazul nostru nu verificăm tipul de mesaj ICMP
        # puteti verifica daca primul byte are valoarea Type == 11 
        # https://tools.ietf.org/html/rfc792#page-5
        # https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Header
        addr = 'done!'
        try:
            data, addr = icmp_recv_socket.recvfrom(63535)

            # extragem valoarea codului ICMP pt type
            byte = struct.unpack('!c', data[20:21])[0]

            print("TTL=", TTL, " A ajuns la IP-ul: ", addr[0])

            # adaugam ip ul la ruta
            lista_ips.append(addr[0])

            # verificam daca codul type al ICMP este diferit de 11 --> daca este diferit de 11 am ajuns la ip ul final si iesim din while
            if byte != b'\x0b':
                break

            # TODO: de rezolvat problema cu socket timeout  

        except Exception as e:
            print("TTL=", TTL, " Socket timeout ")
            # print(traceback.format_exc())

    return lista_ips

def ip_random(): # generam un ip_fake pt a 'pacali' ipinfo
    return  "79." + str(random.randrange(0,255)) + "." + str(random.randrange(0,255)) + "." + str(random.randrange(0,255))

# cele 3 ip uri pt care cautam rutele
ip_uri_de_cautat = [
                    '36.51.254.91', # china
                    '163.200.81.55', # africa
                    '54.252.93.212' # australia
                    ] 

for ip_cautat in ip_uri_de_cautat:
    print("--------------------------------")
    print("Cautam ruta IP-ului ", ip_cautat)
    print("--------------------------------")
    lista_ips = traceroute(ip_cautat, 80)
    print("\nRuta ip-ului ", ip_cautat," este: ")
    print("--------------------------------")
    for idx,ip in enumerate(lista_ips): # afisam ruta
        ip_fake = ip_random() # generam un ip fake si il adaugam la header

        fake_HTTP_header = {
                            'referer': 'https://ipinfo.io/',
                            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36',
                            'X-Forwarded-For': ip_fake 
                        }
    
        raspuns = requests.get('https://ipinfo.io/widget/' + str(ip), headers=fake_HTTP_header)

        # afisarea raspunsului
        if 'bogon' in raspuns.json():
            print (f"{idx}: {raspuns.json()['ip']} -> este bogon IP")
        else:
            print (f"{idx}: {raspuns.json()['ip']} - {raspuns.json()['city']}, {raspuns.json()['region']}, {raspuns.json()['country']}")