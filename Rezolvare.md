# Soluție

## 1. Traceroute

Am implementat tracerout-ul, insa primim socket timeout de foarte multe ori. Noi consideram ca acest lucru se intampla atunci cand se incearca obtinerea mesajului de la un anumit IP care refuza sa raspunda (sau ignora mesajele ICMP) si se reincearca acelasi IP, dar cu un TTL mai mare. Am ales un TTL maxim de 64, deoarece altfel s-ar incerca la infinit pe acelasi IP.

Am implementat soluția iar aici este output-ul:

### Ruta către `36.51.254.91 - China`
```
--------------------------------
Cautam ruta IP-ului  36.51.254.91
--------------------------------
TTL= 1  A ajuns la IP-ul:  192.168.0.1
TTL= 2  A ajuns la IP-ul:  10.0.0.1
TTL= 3  A ajuns la IP-ul:  10.162.1.17
TTL= 4  A ajuns la IP-ul:  10.220.138.141
TTL= 5  A ajuns la IP-ul:  10.220.154.110
TTL= 6  A ajuns la IP-ul:  10.220.131.124
TTL= 7  A ajuns la IP-ul:  10.220.152.68
TTL= 8  A ajuns la IP-ul:  10.220.128.77
TTL= 9  A ajuns la IP-ul:  195.66.224.100
TTL= 10  A ajuns la IP-ul:  218.189.8.94
TTL= 11  A ajuns la IP-ul:  218.189.8.97
TTL= 12  A ajuns la IP-ul:  218.189.5.56
TTL= 13  Socket timeout 
TTL= 14  A ajuns la IP-ul:  36.51.254.91

Ruta ip-ului  36.51.254.91  este: 
--------------------------------
0: 192.168.0.1 -> este bogon IP
1: 10.0.0.1 -> este bogon IP
2: 10.162.1.17 -> este bogon IP
3: 10.220.138.141 -> este bogon IP
4: 10.220.154.110 -> este bogon IP
5: 10.220.131.124 -> este bogon IP
6: 10.220.152.68 -> este bogon IP
7: 10.220.128.77 -> este bogon IP
8: 195.66.224.100 - London, England, GB
9: 218.189.8.94 - Tsuen Wan, Tsuen Wan, HK
10: 218.189.8.97 - Tsuen Wan, Tsuen Wan, HK
11: 218.189.5.56 - Tsuen Wan, Tsuen Wan, HK
12: 36.51.254.91 - Beijing, Beijing, CN
--------------------------------

```

### Ruta către `163.200.81.55 - Africa`
```
--------------------------------
Cautam ruta IP-ului  163.200.81.55
--------------------------------
TTL= 1  A ajuns la IP-ul:  192.168.0.1
TTL= 2  A ajuns la IP-ul:  10.0.0.1
TTL= 3  A ajuns la IP-ul:  10.162.1.17
TTL= 4  A ajuns la IP-ul:  10.220.138.141
TTL= 5  A ajuns la IP-ul:  10.220.154.110
TTL= 6  A ajuns la IP-ul:  10.220.131.124
TTL= 7  A ajuns la IP-ul:  10.220.152.68
TTL= 8  A ajuns la IP-ul:  10.220.133.105
TTL= 9  A ajuns la IP-ul:  62.115.153.128
TTL= 10  A ajuns la IP-ul:  130.117.14.197
TTL= 11  A ajuns la IP-ul:  130.117.1.118
TTL= 12  A ajuns la IP-ul:  130.117.0.141
TTL= 13  A ajuns la IP-ul:  154.54.39.186
TTL= 14  A ajuns la IP-ul:  149.11.39.2
TTL= 15  A ajuns la IP-ul:  155.232.1.81
TTL= 16  A ajuns la IP-ul:  155.232.1.40
TTL= 17  A ajuns la IP-ul:  155.232.6.64
TTL= 18  A ajuns la IP-ul:  155.232.64.87
TTL= 19  A ajuns la IP-ul:  155.232.64.60
TTL= 20  A ajuns la IP-ul:  155.232.1.66
TTL= 21  A ajuns la IP-ul:  155.232.1.98
TTL= 22  A ajuns la IP-ul:  155.232.128.93
TTL= 23  Socket timeout 
TTL= 24  Socket timeout 
TTL= 25  Socket timeout 
TTL= 26  Socket timeout 
TTL= 27  Socket timeout 
TTL= 28  Socket timeout 
TTL= 29  Socket timeout 
TTL= 30  Socket timeout 
TTL= 31  Socket timeout 
TTL= 32  Socket timeout 
TTL= 33  Socket timeout 
TTL= 34  Socket timeout 
TTL= 35  Socket timeout 
TTL= 36  Socket timeout 
TTL= 37  Socket timeout 
TTL= 38  Socket timeout 
TTL= 39  Socket timeout 
TTL= 40  Socket timeout 
TTL= 41  Socket timeout 
TTL= 42  Socket timeout 
TTL= 43  Socket timeout 
TTL= 44  Socket timeout 
TTL= 45  Socket timeout 
TTL= 46  Socket timeout 
TTL= 47  Socket timeout 
TTL= 48  Socket timeout 
TTL= 49  Socket timeout 
TTL= 50  Socket timeout 
TTL= 51  Socket timeout 
TTL= 52  Socket timeout 
TTL= 53  Socket timeout 
TTL= 54  Socket timeout 
TTL= 55  Socket timeout 
TTL= 56  Socket timeout 
TTL= 57  Socket timeout 
TTL= 58  Socket timeout 
TTL= 59  Socket timeout 
TTL= 60  Socket timeout 
TTL= 61  Socket timeout 
TTL= 62  Socket timeout 
TTL= 63  Socket timeout 
TTL= 64  Socket timeout 

S-a atins limita maxima de TTL. Oprim cautarea...

Ruta ip-ului  163.200.81.55  este: 
--------------------------------
0: 192.168.0.1 -> este bogon IP
1: 10.0.0.1 -> este bogon IP
2: 10.162.1.17 -> este bogon IP
3: 10.220.138.141 -> este bogon IP
4: 10.220.154.110 -> este bogon IP
5: 10.220.131.124 -> este bogon IP
6: 10.220.152.68 -> este bogon IP
7: 10.220.133.105 -> este bogon IP
8: 62.115.153.128 - Råsunda, Stockholm, SE
9: 130.117.14.197 - Washington, Virginia, US
10: 130.117.1.118 - Washington, Virginia, US
11: 130.117.0.141 - Washington, Virginia, US
12: 154.54.39.186 - Washington, Virginia, US
13: 149.11.39.2 - Amsterdam, North Holland, NL
14: 155.232.1.81 - Pretoria, Gauteng, ZA
15: 155.232.1.40 - Cape Town, Western Cape, ZA
16: 155.232.6.64 - Cape Town, Western Cape, ZA
17: 155.232.64.87 - Cape Town, Western Cape, ZA
18: 155.232.64.60 - Cape Town, Western Cape, ZA
19: 155.232.1.66 - Pretoria, Gauteng, ZA
20: 155.232.1.98 - Pretoria, Gauteng, ZA
21: 155.232.128.93 - Cape Town, Western Cape, ZA
--------------------------------
```

### Ruta către `54.252.93.212 - Australia`
```
--------------------------------
Cautam ruta IP-ului  54.252.93.212
--------------------------------
TTL= 1  A ajuns la IP-ul:  192.168.0.1
TTL= 2  A ajuns la IP-ul:  10.0.0.1
TTL= 3  A ajuns la IP-ul:  10.162.1.17
TTL= 4  A ajuns la IP-ul:  10.220.138.141
TTL= 5  A ajuns la IP-ul:  10.220.154.110
TTL= 6  A ajuns la IP-ul:  10.220.131.124
TTL= 7  A ajuns la IP-ul:  10.220.152.68
TTL= 8  A ajuns la IP-ul:  10.220.128.77
TTL= 9  A ajuns la IP-ul:  195.66.224.177
TTL= 10  A ajuns la IP-ul:  202.40.148.33
TTL= 11  A ajuns la IP-ul:  202.84.141.145
TTL= 12  A ajuns la IP-ul:  202.40.148.106
TTL= 13  A ajuns la IP-ul:  202.84.141.226
TTL= 14  A ajuns la IP-ul:  202.84.222.198
TTL= 15  A ajuns la IP-ul:  134.159.125.178
TTL= 16  Socket timeout 
TTL= 17  Socket timeout 
TTL= 18  A ajuns la IP-ul:  52.95.37.175
TTL= 19  A ajuns la IP-ul:  150.222.112.207
TTL= 20  A ajuns la IP-ul:  150.222.112.202
TTL= 21  A ajuns la IP-ul:  52.95.37.105
TTL= 22  A ajuns la IP-ul:  52.95.38.212
TTL= 23  Socket timeout 
TTL= 24  Socket timeout 
TTL= 25  Socket timeout 
TTL= 26  Socket timeout 
TTL= 27  Socket timeout 
TTL= 28  Socket timeout 
TTL= 29  Socket timeout 
TTL= 30  Socket timeout 
TTL= 31  Socket timeout 
TTL= 32  Socket timeout 
TTL= 33  Socket timeout 
TTL= 34  Socket timeout 
TTL= 35  Socket timeout 
TTL= 36  Socket timeout 
TTL= 37  Socket timeout 
TTL= 38  Socket timeout 
TTL= 39  Socket timeout 
TTL= 40  Socket timeout 
TTL= 41  Socket timeout 
TTL= 42  Socket timeout 
TTL= 43  Socket timeout 
TTL= 44  Socket timeout 
TTL= 45  Socket timeout 
TTL= 46  Socket timeout 
TTL= 47  Socket timeout 
TTL= 48  Socket timeout 
TTL= 49  Socket timeout 
TTL= 50  Socket timeout 
TTL= 51  Socket timeout 
TTL= 52  Socket timeout 
TTL= 53  Socket timeout 
TTL= 54  Socket timeout 
TTL= 55  Socket timeout 
TTL= 56  Socket timeout 
TTL= 57  Socket timeout 
TTL= 58  Socket timeout 
TTL= 59  Socket timeout 
TTL= 60  Socket timeout 
TTL= 61  Socket timeout 
TTL= 62  Socket timeout 
TTL= 63  Socket timeout 
TTL= 64  Socket timeout 

S-a atins limita maxima de TTL. Oprim cautarea...

Ruta ip-ului  54.252.93.212  este: 
--------------------------------
0: 192.168.0.1 -> este bogon IP
1: 10.0.0.1 -> este bogon IP
2: 10.162.1.17 -> este bogon IP
3: 10.220.138.141 -> este bogon IP
4: 10.220.154.110 -> este bogon IP
5: 10.220.131.124 -> este bogon IP
6: 10.220.152.68 -> este bogon IP
7: 10.220.128.77 -> este bogon IP
8: 195.66.224.177 - London, England, GB
9: 202.40.148.33 - Wan Chai, Wan Chai, HK
10: 202.84.141.145 - Wan Chai, Wan Chai, HK
11: 202.40.148.106 - Wan Chai, Wan Chai, HK
12: 202.84.141.226 - Wan Chai, Wan Chai, HK
13: 202.84.222.198 - Wan Chai, Wan Chai, HK
14: 134.159.125.178 - Nickol, Western Australia, AU
15: 52.95.37.175 - Sydney, New South Wales, AU
16: 150.222.112.207 - Sydney, New South Wales, AU
17: 150.222.112.202 - Sydney, New South Wales, AU
18: 52.95.37.105 - Sydney, New South Wales, AU
19: 52.95.38.212 - Sydney, New South Wales, AU
--------------------------------

```


## 2. Reliable UDP

### Emițător - mesaje de logging
Rulăm `docker-compose logs emitator` și punem rezultatul aici:
```
....
....
....
....
....
```


### Receptor - mesaje de logging
Rulăm `docker-compose logs receptor` și punem rezultatul aici:
```
....
....
....
....
....
```