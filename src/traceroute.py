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
icmp_recv_socket.settimeout(3)

def traceroute(ip, port):
    # setam TTL in headerul de IP pentru socketul de UDP
    TTL = 0 
    lista_ips = [] # o lista in care adaugam ip urile din ruta ip ului pt care ii cautam ruta

    while True:
        TTL += 1  # crestem TTL pana ce ajungem la ip ul final
        print(TTL)
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

            # adaugam ip ul la ruta
            lista_ips.append(addr[0])

            # verificam daca codul type al ICMP este diferit de 11 --> daca este diferit de 11 am ajuns la ip ul final si iesim din while
            if byte != b'\x0b':
                break

            # TODO: de rezolvat problema cu socket timeout  

        except Exception as e:
            print("Socket timeout ", str(e))
            print(traceback.format_exc())

    return lista_ips

def ip_random(): # generam un ip_fake pt a 'pacali' ipinfo
    return  "79." + str(random.randrange(0,255)) + "." + str(random.randrange(0,255)) + "." + str(random.randrange(0,255))


lista_ips = traceroute("74.125.31.139", 80)
for index, ip in enumerate(lista_ips):
    print(index, " ", ip)


# cele 3 ip uri pt care cautam rutele
ip_uri_de_cautat = ['74.125.31.139' # google.com
                    ] 
'''
for ip_cautat in ip_uri_de_cautat:
    print("Ruta ip-ului ",ip_cautat," este:")
    #lista_ips = traceroute(ip_cautat, 80)
    lista_ips = ['10.220.138.141','10.220.154.110','72.14.237.248','209.85.142.96']
    for idx,ip in enumerate(lista_ips): # afisam ruta
        ip_fake = ip_random() # genarm un ip fake si il adaugam la header

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

'''