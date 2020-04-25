import socket
import traceback
import requests
import struct

# socket de UDP
udp_send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)

# socket RAW de citire a răspunsurilor ICMP
icmp_recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
# setam timout in cazul in care socketul ICMP la apelul recvfrom nu primeste nimic in buffer
icmp_recv_socket.settimeout(3)

def traceroute(ip, port):
    # setam TTL in headerul de IP pentru socketul de UDP
    TTL = 0
    lista_ips = []
    while True:
        TTL += 1
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
            byte = struct.unpack('!c', data[20:21])[0]
            lista_ips.append(addr[0])
            # print(addr[0], " ", byte)
            if byte != b'\x0b':
                break
        except Exception as e:
            print("Socket timeout ", str(e))
            print(traceback.format_exc())
    return lista_ips

#print(traceroute("172.217.203.94", 80))
lista_ips = traceroute("193.226.51.15", 80)
for index, ip in enumerate(lista_ips):
    print(index, " ", ip)

#print(traceroute("172.217.203.94", 80))
# exemplu de request la IP info pentru a
# obtine informatii despre localizarea unui IP 
fake_HTTP_header = {
                    'referer': 'https://ipinfo.io/',
                    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
                   }
# informatiile despre ip-ul 193.226.51.6 pe ipinfo.io
# https://ipinfo.io/193.226.51.6 e echivalent cu
# raspuns = requests.get('https://ipinfo.io/widget/193.226.51.6', headers=fake_HTTP_header)
# print (raspuns.json())

# pentru un IP rezervat retelei locale da bogon=True
# raspuns = requests.get('https://ipinfo.io/widget/10.0.0.1', headers=fake_HTTP_header)
# print (raspuns.json())

