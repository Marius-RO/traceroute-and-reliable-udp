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


# 2. Reliable UDP

Am trimis imaginea img_trimisa.jpg de 141 kb catre receptor care a salvat imaginea in img_primita.jpg. 

## 1. Conectarea emitator - receptor:

Initial emitatorul trimite un mesaj de cerere de conectare catre receptor (avand flagul `S`) si asteapta sa primeasca confirmarea de la acesta. Datorita packet loss mare incercam sa retrimitem mesajul de confirmare de `NR_MAX_INCERCARI` ori (este setat cu 20) iar daca nu primim o confirmare dupa `NR_MAX_INCERCARI` programul se va inchide. 

De asemenea, tot datorita packet loss, pentru fiecare mesaj primit, receptorul trimite `NR_MAX_INCERCARI` mesaje de confirmare catre emitator. Pentru a se incheia conectarea initala este necesar ca emitatorul sa receptioneze o singura confirmare.

Modalitatea de trimitere a mesajelor de conectare catre receptor este blocanta (trimitem mesajul si asteptam `TIMEOUT` secunde dupa o confirmare de la receptor).

## **Explicatii pe logul din emitator**


### **Se trimiterea cerea initiala**
```
[LINE:39]# INFO     [2020-05-05 10:18:52,412]  Am trimis cererea de conectare cu flagul S catre ('198.8.0.2', 10000)
```
### **Nu s-a primit raspuns dupa `TIMEOUT` secunde => se retrimite cerearea**
```
[LINE:48]# INFO     [2020-05-05 10:18:53,414]  Timeout la connect flag S, retrying...
[LINE:48]# INFO     [2020-05-05 10:18:54,417]  Timeout la connect flag S, retrying...
[LINE:48]# INFO     [2020-05-05 10:18:55,419]  Timeout la connect flag S, retrying...
[LINE:48]# INFO     [2020-05-05 10:18:56,420]  Timeout la connect flag S, retrying...
[LINE:48]# INFO     [2020-05-05 10:18:57,422]  Timeout la connect flag S, retrying...
[LINE:48]# INFO     [2020-05-05 10:18:58,424]  Timeout la connect flag S, retrying...
[LINE:48]# INFO     [2020-05-05 10:18:59,426]  Timeout la connect flag S, retrying...
[LINE:48]# INFO     [2020-05-05 10:19:00,428]  Timeout la connect flag S, retrying...
```
### **S-a receptionat un raspuns dupa 9 incercari**
```
[LINE:51]# INFO     [2020-05-05 10:19:00,430]  Header cerere trimisa: [seq_nr: 104414] , [check:  7520] , [flag: S]
[LINE:55]# INFO     [2020-05-05 10:19:00,430]  Cererea de conectare cu flagul S a fost primita de ('198.8.0.2', 10000)
[LINE:56]# INFO     [2020-05-05 10:19:00,430]  Header receptor primit: [ack_nr: 104415] , [check:  26650] , [window: 5]
[LINE:57]# INFO     [2020-05-05 10:19:00,431]  S-a realizat conexiunea
```
### In acest moment s-a realizat conexiunea si avem o fereastra initala primita cu valoarea 5.

### Golim bufferul de confirmarile ce mai trebuie sa ajunga de la receptor (pentru ca receptorul trimite pentru fiecare mesaj primit cate `NR_MAX_INCERCARI` de confirmari exista sanse mari ca dupa ce a primit prima confirmare sa mai vina si altele, astfel ca golim bufferul pentru a trece la urmatoarea etapa cu bufferul gol).

```
[LINE:152]# INFO     [2020-05-05 10:19:00,431]  Buffer golit
```



## **Explicatii pe logul din receptor**

```
[LINE:76]# INFO     [2020-05-05 10:18:49,523]  Serverul a pornit pe 0.0.0.0 si portul 10000
[LINE:83]# INFO     [2020-05-05 10:18:49,524]  Asteptam mesaje...
```

### **Receptorul a primit mesajul de solicitare a conexiunii de la emitator si trimite `NR_MAX_INCERCARI` de confirmari pentru acest mesaj**
```
[LINE:85]# INFO     [2020-05-05 10:19:00,429]  Am primit 23 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:19:00,429]  Header emitator primit: [seq_nr: 104414] , [check:  7520] , [flag: S]

[LINE:35]# INFO     [2020-05-05 10:19:00,430]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:19:00,431]  Header receptor trimis: [ack_nr: 104415] , [check:  26650] , [window: 5]
[LINE:45]# INFO     [2020-05-05 10:19:00,431]  S-au trimis 20 confirmari
```

## 2. Trimiterea segmentelor (Sliding window - Go Back N)

Modul in care functioneaza implementarea noastra este urmatorul:
- extragem toate segmentele din imaginea trimisa (pentru aceasta rulare au fost 101 segmente de maxim 1400 bytes)
- preluam marimea ferestrei (generat random de receptor) din headerul primit cand s-a realizat confirmarea de conectare (pentru aceasta rulare dimensiunea initiala a ferestrei este 5)
- parcurgem segmentele de la inceputul ferestrei pana la finalul ferestrei si le trimitem pe toate fara a astepta dupa confirmare
( le trimitem doar daca nu au fost confirmate -> este posibil sa fi fost confirmate anterior daca aceasta este o retransmisie a ferestrei)
-  asteptam `TIMEOUT` secunde pentru a prelua confirmarile primite (simulam timeout ul ferestrei)
- dupa ce am preluat confirmarile primite verificam care segmente au fost confirmate (dintre cele trimise) si mutam fereastra spre dreapta cu numarul de segmente confirmate consecutiv din stanga.




## **Explicatii pe logul din emitator**

## Initial fereastra are dimensiunea 5 (numarul primit de la receptor in confirmarea conexiunii) => se trimite fereastra 0 - 4 => se trimit segmentele 0,1,2,3,4
```
[LINE:223]# INFO     [2020-05-05 10:19:00,432]  Se transmite fereastra 0 - 4
[LINE:224]# INFO     [2020-05-05 10:19:00,433]  Mai sunt 101 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:00,433]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:00,433]  Header segment 0 trimis: [seq_nr: 190786] , [check:  6455] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:00,433]  Header segment 1 trimis: [seq_nr: 192187] , [check:  11561] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:00,434]  Header segment 2 trimis: [seq_nr: 193588] , [check:  8234] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:00,434]  Header segment 3 trimis: [seq_nr: 194989] , [check:  10225] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:00,435]  Header segment 4 trimis: [seq_nr: 196390] , [check:  15701] , [flag: P]
```
### Se asteapta `TIMEOUT` secunde (se simuleaza timeout-ul ferestrei) dupa care se preiau toate confirmarile primite pentru segmentele trimise anterior. Obs: Fiecare confirmare se salveaza o singura data in lista de confirmari.

### Pentru aceasta prima transmisie s-a primit o singura confirmare distincta, iar aceasta este pentru segmentul 0 ==> fiind segmentul cel mai din stanga fereastra va avansa cu o unitate. Dar in acelasi timp s-a primit si o noua valoare pentru fereastra (valoarea 2). In aceasta situatie noua fereastra ce va fi trimisa la urmatoarea iteratie este 1 - 2. 


```
[LINE:161]# INFO     [2020-05-05 10:19:01,437]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:01,438]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:19:01,438]  Header receptor pt segment primit: [ack_nr: 192186] , [check:  4417] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:19:01,439]  Idx segmente confirmate: [0]

[LINE:331]# INFO     [2020-05-05 10:19:01,439]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:01,440]  
[LINE:222]# INFO     [2020-05-05 10:19:01,440]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:01,440]  Se transmite fereastra 1 - 2
[LINE:224]# INFO     [2020-05-05 10:19:01,440]  Mai sunt 100 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:01,440]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:01,441]  Header segment 1 trimis: [seq_nr: 192186] , [check:  11562] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:01,442]  Header segment 2 trimis: [seq_nr: 193587] , [check:  8235] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:02,444]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:02,444]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:19:02,445]  Header receptor pt segment primit: [ack_nr: 193586] , [check:  3018] , [window: 1]
[LINE:290]# INFO     [2020-05-05 10:19:02,445]  Idx segmente confirmate: [1]
[LINE:330]# INFO     [2020-05-05 10:19:02,445]  
[LINE:331]# INFO     [2020-05-05 10:19:02,445]  Fereastra a avansat cu 1 pozitii.
```

### Acest proces se reia pana se primesc confirmari pentru toate segmentele.

**Obs 1**: In caz ca in exemplul anterior in loc de confirmarea pentru segmentul 0 se primea confirmarea pentru segmentul 4 (sa presupunem ca noua dimensiune care vine pentru fereastra este tot **`2`**), atunci fereastra nu va mai avansa (pentru ca segementul cel mai din stanga nu a fost confirmat) dar isi va schimba dimensiunea **`(noua fereastra va fi 0 - 1)`**. La urmatoarea iteratie s-ar fi retransmis segmentele **`0,1`**. Totusi segmentul 4 care a fost confirmat nu va mai fi trimis ulterior (atunci cand va fi incadrat intr-o fereastra corespunzatoare) pentru ca in momentul in care a fost marcat ca fiind confirmat nici un segement nu va mai fi retransmis(deci orice segemnt confirmat de receptor va fi sarit la o retransmisie ulterioara). 

**Obs 2**: In caz ca in exemplul anterior in loc de confirmarea pentru segmentul 0 se primea confirmarea pentru segmentul 4 (sa presupunem ca noua dimensiune care vine pentru fereastra este **`7`**), atunci fereastra nu va mai avansa (pentru ca segementul cel mai din stanga nu a fost confirmat) dar isi va schimba dimensiunea **`(noua fereastra va fi 0 - 6)`**. La urmatoarea iteratie s-ar fi retransmis segmentele **`0,1,2,3,5,6`** (segmentul 4 care a fost confirmat nu va mai fi trimis pentru ca a fost confirmat deja).

**Obs 3**: In caz ca in exemplul anterior in loc de confirmarea pentru segmentul 0 se primeau confirmari pentru segmentele 1,2,3,4 (sa presupunem ca noua dimensiune care vine pentru fereastra este **`3`**), atunci fereastra nu va mai avansa (pentru ca segementul cel mai din stanga nu a fost confirmat) dar isi va schimba dimensiunea **`(noua fereastra va fi 0 - 2)`**. La urmatoarea iteratie s-ar fi retransmis segmentul **`0`** (segmentele 1,2 care au fost confirmate nu vor mai fi trimise pentru ca au fost confirmate deja). Prespunem ca la urmatoarea iteratie cand se trimite fereastra **`0 - 2`** (doar segmentul 0 in acest caz) am primi confirmarea pentru segmentul 0 si o noua dimensiune a ferestrei de **`5`** atunci urmatoarea fereastra ar fi **`5 - 9`** (Explicatie: Fereastra curenta este **`0 - 2`** => s-a trimis segmentul 0 => s-a primit confirmare pentru segmentul 0 => stim ca aveam confirmare si pentru segmentele **`1,2`** anterior trimise => noua fereastra ar fi **`3 - 7`** => dar stim ca in fereastra **`3 - 7`** avem confirmari pentru **`3,4`** => noua fereastra care va fi rulata la urmatoarea iteratie va fi **`5 - 9`**).

**Obs 4**: Daca mai avem de trimis **`3`** segmente si primim un window de **`5`** atunci se vor trimite doar acele **`3`** segmente, deci o fereastra mai mare decat numarul de segmente neconfirmate nu afecteaza functionalitatea programului.


- Modalitatea prin care verificam daca un segment a fost confirmat este sa verificam daca ack number-ul si checksum-ul sunt cele asteptate.


## **Explicatii pentru functionalitatea receptorului**

- Receptorul primeste mesajul => ii verifica checksum-ul => daca checksum-ul este corect (trebuie sa dea 0 in urma reaplicarii algoritmului de checksum) atunci continua si trimite cele `NR_MAX_INCERCARI` de confirmari catre emitator cu `ack = seq_nr + len(payload)`, altfel va ignora pachetul si il va astepta pe urmatorul.




## 2. Finalizarea emitator - receptor

Este la fel ca pasul de conectare cu deosebirea ca flagul trimis este `F` in loc de `S` cu urmatoarele observatii:
- cand receptorul primeste flagul `F` va scrie datele primite in fiser si verifica daca fisierul trimis a ajuns integru
- este posibil ca datorita packet loss in momentul finalizarii daca receptorul a primit cerea de finalizare si a trimis cele `NR_MAX_INCERCARI` confirmari emitatorul sa nu primeasca nici una din acele confirmari. Acest comportament nu afecteaza salvarea datelor deoarece in momentul in care receptorul primeste primul mesaj de finalizare acesta trimite confirmarile catre emitator dupa care salveaza datele, verifica integritatea fisierului trimis si isi incheie executia.


### Emițător - mesaje de logging
Rulăm `docker-compose logs emitator` și punem rezultatul aici:
```
root@55adb4a978fc:/elocal/tema-3-mc-network/src# python3 emitator.py -f img_trimisa.jpg
[LINE:39]# INFO     [2020-05-05 10:18:52,412]  Am trimis cererea de conectare cu flagul S catre ('198.8.0.2', 10000)
[LINE:48]# INFO     [2020-05-05 10:18:53,414]  Timeout la connect flag S, retrying...
[LINE:48]# INFO     [2020-05-05 10:18:54,417]  Timeout la connect flag S, retrying...
[LINE:48]# INFO     [2020-05-05 10:18:55,419]  Timeout la connect flag S, retrying...
[LINE:48]# INFO     [2020-05-05 10:18:56,420]  Timeout la connect flag S, retrying...
[LINE:48]# INFO     [2020-05-05 10:18:57,422]  Timeout la connect flag S, retrying...
[LINE:48]# INFO     [2020-05-05 10:18:58,424]  Timeout la connect flag S, retrying...
[LINE:48]# INFO     [2020-05-05 10:18:59,426]  Timeout la connect flag S, retrying...
[LINE:48]# INFO     [2020-05-05 10:19:00,428]  Timeout la connect flag S, retrying...
[LINE:51]# INFO     [2020-05-05 10:19:00,430]  Header cerere trimisa: [seq_nr: 104414] , [check:  7520] , [flag: S]
[LINE:55]# INFO     [2020-05-05 10:19:00,430]  Cererea de conectare cu flagul S a fost primita de ('198.8.0.2', 10000)
[LINE:56]# INFO     [2020-05-05 10:19:00,430]  Header receptor primit: [ack_nr: 104415] , [check:  26650] , [window: 5]
[LINE:57]# INFO     [2020-05-05 10:19:00,431]  S-a realizat conexiunea
[LINE:58]# INFO     [2020-05-05 10:19:00,431]  
[LINE:152]# INFO     [2020-05-05 10:19:00,431]  Buffer golit
[LINE:221]# INFO     [2020-05-05 10:19:00,432]  
[LINE:222]# INFO     [2020-05-05 10:19:00,432]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:00,432]  Se transmite fereastra 0 - 4
[LINE:224]# INFO     [2020-05-05 10:19:00,433]  Mai sunt 101 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:00,433]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:00,433]  Header segment 0 trimis: [seq_nr: 190786] , [check:  6455] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:00,433]  Header segment 1 trimis: [seq_nr: 192187] , [check:  11561] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:00,434]  Header segment 2 trimis: [seq_nr: 193588] , [check:  8234] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:00,434]  Header segment 3 trimis: [seq_nr: 194989] , [check:  10225] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:00,435]  Header segment 4 trimis: [seq_nr: 196390] , [check:  15701] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:01,437]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:01,438]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:19:01,438]  Header receptor pt segment primit: [ack_nr: 192186] , [check:  4417] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:19:01,439]  Idx segmente confirmate: [0]
[LINE:330]# INFO     [2020-05-05 10:19:01,439]  
[LINE:331]# INFO     [2020-05-05 10:19:01,439]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:01,440]  
[LINE:222]# INFO     [2020-05-05 10:19:01,440]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:01,440]  Se transmite fereastra 1 - 2
[LINE:224]# INFO     [2020-05-05 10:19:01,440]  Mai sunt 100 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:01,440]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:01,441]  Header segment 1 trimis: [seq_nr: 192186] , [check:  11562] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:01,442]  Header segment 2 trimis: [seq_nr: 193587] , [check:  8235] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:02,444]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:02,444]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:19:02,445]  Header receptor pt segment primit: [ack_nr: 193586] , [check:  3018] , [window: 1]
[LINE:290]# INFO     [2020-05-05 10:19:02,445]  Idx segmente confirmate: [1]
[LINE:330]# INFO     [2020-05-05 10:19:02,445]  
[LINE:331]# INFO     [2020-05-05 10:19:02,445]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:02,445]  
[LINE:222]# INFO     [2020-05-05 10:19:02,445]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:02,446]  Se transmite fereastra 2 - 2
[LINE:224]# INFO     [2020-05-05 10:19:02,446]  Mai sunt 99 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:02,446]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:02,446]  Header segment 2 trimis: [seq_nr: 193586] , [check:  8236] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:03,448]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:03,449]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:03,449]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:19:03,449]  
[LINE:331]# INFO     [2020-05-05 10:19:03,449]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:03,450]  
[LINE:222]# INFO     [2020-05-05 10:19:03,450]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:03,450]  Se transmite fereastra 2 - 2
[LINE:224]# INFO     [2020-05-05 10:19:03,450]  Mai sunt 99 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:03,450]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:03,451]  Header segment 2 trimis: [seq_nr: 193586] , [check:  8236] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:04,453]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:04,454]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:04,454]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:19:04,455]  
[LINE:331]# INFO     [2020-05-05 10:19:04,455]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:04,455]  
[LINE:222]# INFO     [2020-05-05 10:19:04,456]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:04,456]  Se transmite fereastra 2 - 2
[LINE:224]# INFO     [2020-05-05 10:19:04,456]  Mai sunt 99 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:04,457]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:04,457]  Header segment 2 trimis: [seq_nr: 193586] , [check:  8236] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:05,460]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:05,460]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:05,461]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:19:05,462]  
[LINE:331]# INFO     [2020-05-05 10:19:05,462]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:05,462]  
[LINE:222]# INFO     [2020-05-05 10:19:05,462]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:05,462]  Se transmite fereastra 2 - 2
[LINE:224]# INFO     [2020-05-05 10:19:05,462]  Mai sunt 99 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:05,463]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:05,463]  Header segment 2 trimis: [seq_nr: 193586] , [check:  8236] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:06,466]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:06,466]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:06,466]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:19:06,466]  
[LINE:331]# INFO     [2020-05-05 10:19:06,466]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:06,467]  
[LINE:222]# INFO     [2020-05-05 10:19:06,467]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:06,467]  Se transmite fereastra 2 - 2
[LINE:224]# INFO     [2020-05-05 10:19:06,467]  Mai sunt 99 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:06,467]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:06,468]  Header segment 2 trimis: [seq_nr: 193586] , [check:  8236] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:07,470]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:07,470]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:07,471]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:19:07,471]  
[LINE:331]# INFO     [2020-05-05 10:19:07,471]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:07,472]  
[LINE:222]# INFO     [2020-05-05 10:19:07,472]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:07,472]  Se transmite fereastra 2 - 2
[LINE:224]# INFO     [2020-05-05 10:19:07,473]  Mai sunt 99 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:07,473]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:07,474]  Header segment 2 trimis: [seq_nr: 193586] , [check:  8236] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:08,477]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:08,477]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:08,478]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:19:08,478]  
[LINE:331]# INFO     [2020-05-05 10:19:08,479]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:08,479]  
[LINE:222]# INFO     [2020-05-05 10:19:08,479]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:08,479]  Se transmite fereastra 2 - 2
[LINE:224]# INFO     [2020-05-05 10:19:08,479]  Mai sunt 99 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:08,480]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:08,480]  Header segment 2 trimis: [seq_nr: 193586] , [check:  8236] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:09,481]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:09,481]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:09,482]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:19:09,482]  
[LINE:331]# INFO     [2020-05-05 10:19:09,482]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:09,482]  
[LINE:222]# INFO     [2020-05-05 10:19:09,482]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:09,483]  Se transmite fereastra 2 - 2
[LINE:224]# INFO     [2020-05-05 10:19:09,483]  Mai sunt 99 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:09,483]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:09,484]  Header segment 2 trimis: [seq_nr: 193586] , [check:  8236] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:10,486]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:10,486]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:19:10,487]  Header receptor pt segment primit: [ack_nr: 194986] , [check:  1618] , [window: 1]
[LINE:290]# INFO     [2020-05-05 10:19:10,488]  Idx segmente confirmate: [2]
[LINE:330]# INFO     [2020-05-05 10:19:10,488]  
[LINE:331]# INFO     [2020-05-05 10:19:10,488]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:10,488]  
[LINE:222]# INFO     [2020-05-05 10:19:10,488]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:10,489]  Se transmite fereastra 3 - 3
[LINE:224]# INFO     [2020-05-05 10:19:10,489]  Mai sunt 98 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:10,489]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:10,490]  Header segment 3 trimis: [seq_nr: 194986] , [check:  10228] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:11,492]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:11,492]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:11,492]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:19:11,493]  
[LINE:331]# INFO     [2020-05-05 10:19:11,493]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:11,493]  
[LINE:222]# INFO     [2020-05-05 10:19:11,493]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:11,493]  Se transmite fereastra 3 - 3
[LINE:224]# INFO     [2020-05-05 10:19:11,494]  Mai sunt 98 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:11,494]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:11,494]  Header segment 3 trimis: [seq_nr: 194986] , [check:  10228] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:12,496]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:12,497]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:12,497]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:19:12,497]  
[LINE:331]# INFO     [2020-05-05 10:19:12,498]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:12,498]  
[LINE:222]# INFO     [2020-05-05 10:19:12,498]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:12,498]  Se transmite fereastra 3 - 3
[LINE:224]# INFO     [2020-05-05 10:19:12,498]  Mai sunt 98 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:12,499]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:12,499]  Header segment 3 trimis: [seq_nr: 194986] , [check:  10228] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:13,502]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:13,502]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:13,503]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:19:13,503]  
[LINE:331]# INFO     [2020-05-05 10:19:13,503]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:13,503]  
[LINE:222]# INFO     [2020-05-05 10:19:13,504]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:13,504]  Se transmite fereastra 3 - 3
[LINE:224]# INFO     [2020-05-05 10:19:13,504]  Mai sunt 98 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:13,504]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:13,505]  Header segment 3 trimis: [seq_nr: 194986] , [check:  10228] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:14,507]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:14,507]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:19:14,508]  Header receptor pt segment primit: [ack_nr: 196386] , [check:  218] , [window: 1]
[LINE:290]# INFO     [2020-05-05 10:19:14,508]  Idx segmente confirmate: [3]
[LINE:330]# INFO     [2020-05-05 10:19:14,509]  
[LINE:331]# INFO     [2020-05-05 10:19:14,509]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:14,509]  
[LINE:222]# INFO     [2020-05-05 10:19:14,509]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:14,509]  Se transmite fereastra 4 - 4
[LINE:224]# INFO     [2020-05-05 10:19:14,509]  Mai sunt 97 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:14,510]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:14,510]  Header segment 4 trimis: [seq_nr: 196386] , [check:  15705] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:15,512]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:15,513]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:15,513]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:19:15,513]  
[LINE:331]# INFO     [2020-05-05 10:19:15,513]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:15,513]  
[LINE:222]# INFO     [2020-05-05 10:19:15,513]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:15,513]  Se transmite fereastra 4 - 4
[LINE:224]# INFO     [2020-05-05 10:19:15,513]  Mai sunt 97 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:15,513]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:15,514]  Header segment 4 trimis: [seq_nr: 196386] , [check:  15705] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:16,515]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:16,516]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:16,516]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:19:16,516]  
[LINE:331]# INFO     [2020-05-05 10:19:16,516]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:16,516]  
[LINE:222]# INFO     [2020-05-05 10:19:16,516]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:16,516]  Se transmite fereastra 4 - 4
[LINE:224]# INFO     [2020-05-05 10:19:16,516]  Mai sunt 97 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:16,516]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:16,517]  Header segment 4 trimis: [seq_nr: 196386] , [check:  15705] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:17,518]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:17,519]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:19:17,520]  Header receptor pt segment primit: [ack_nr: 197786] , [check:  864] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:19:17,520]  Idx segmente confirmate: [4]
[LINE:330]# INFO     [2020-05-05 10:19:17,520]  
[LINE:331]# INFO     [2020-05-05 10:19:17,520]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:17,520]  
[LINE:222]# INFO     [2020-05-05 10:19:17,521]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:17,521]  Se transmite fereastra 5 - 6
[LINE:224]# INFO     [2020-05-05 10:19:17,521]  Mai sunt 96 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:17,521]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:17,522]  Header segment 5 trimis: [seq_nr: 197786] , [check:  23156] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:17,522]  Header segment 6 trimis: [seq_nr: 199187] , [check:  1204] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:18,524]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:18,525]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:19:18,525]  Header receptor pt segment primit: [ack_nr: 200587] , [check:  110] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:19:18,525]  Idx segmente confirmate: [6]
[LINE:330]# INFO     [2020-05-05 10:19:18,525]  
[LINE:331]# INFO     [2020-05-05 10:19:18,526]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:18,526]  
[LINE:222]# INFO     [2020-05-05 10:19:18,526]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:18,526]  Se transmite fereastra 5 - 7
[LINE:224]# INFO     [2020-05-05 10:19:18,526]  Mai sunt 96 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:18,526]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:18,527]  Header segment 5 trimis: [seq_nr: 197786] , [check:  23156] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:18,527]  Header segment 7 trimis: [seq_nr: 200587] , [check:  15355] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:19,530]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:19,530]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:19,530]  Idx segmente confirmate: [6]
[LINE:330]# INFO     [2020-05-05 10:19:19,531]  
[LINE:331]# INFO     [2020-05-05 10:19:19,531]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:19,531]  
[LINE:222]# INFO     [2020-05-05 10:19:19,531]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:19,532]  Se transmite fereastra 5 - 7
[LINE:224]# INFO     [2020-05-05 10:19:19,532]  Mai sunt 96 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:19,532]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:19,532]  Header segment 5 trimis: [seq_nr: 197786] , [check:  23156] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:19,533]  Header segment 7 trimis: [seq_nr: 200587] , [check:  15355] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:20,535]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:20,536]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:19:20,536]  Header receptor pt segment primit: [ack_nr: 201987] , [check:  2808] , [window: 1]
[LINE:290]# INFO     [2020-05-05 10:19:20,537]  Idx segmente confirmate: [6, 7]
[LINE:330]# INFO     [2020-05-05 10:19:20,537]  
[LINE:331]# INFO     [2020-05-05 10:19:20,537]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:20,537]  
[LINE:222]# INFO     [2020-05-05 10:19:20,538]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:20,538]  Se transmite fereastra 5 - 5
[LINE:224]# INFO     [2020-05-05 10:19:20,538]  Mai sunt 96 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:20,538]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:20,539]  Header segment 5 trimis: [seq_nr: 197786] , [check:  23156] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:21,541]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:21,542]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:19:21,542]  Header receptor pt segment primit: [ack_nr: 199186] , [check:  1512] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:19:21,542]  Idx segmente confirmate: [5, 6, 7]
[LINE:330]# INFO     [2020-05-05 10:19:21,543]  
[LINE:331]# INFO     [2020-05-05 10:19:21,543]  Fereastra a avansat cu 3 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:21,543]  
[LINE:222]# INFO     [2020-05-05 10:19:21,543]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:21,544]  Se transmite fereastra 8 - 9
[LINE:224]# INFO     [2020-05-05 10:19:21,544]  Mai sunt 93 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:21,544]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:21,544]  Header segment 8 trimis: [seq_nr: 201986] , [check:  306] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:21,545]  Header segment 9 trimis: [seq_nr: 203387] , [check:  14532] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:22,547]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:22,548]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:22,548]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:19:22,548]  
[LINE:331]# INFO     [2020-05-05 10:19:22,548]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:22,548]  
[LINE:222]# INFO     [2020-05-05 10:19:22,548]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:22,548]  Se transmite fereastra 8 - 9
[LINE:224]# INFO     [2020-05-05 10:19:22,549]  Mai sunt 93 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:22,549]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:22,549]  Header segment 8 trimis: [seq_nr: 201986] , [check:  306] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:22,549]  Header segment 9 trimis: [seq_nr: 203387] , [check:  14532] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:23,552]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:23,552]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:23,552]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:19:23,553]  
[LINE:331]# INFO     [2020-05-05 10:19:23,553]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:23,553]  
[LINE:222]# INFO     [2020-05-05 10:19:23,553]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:23,554]  Se transmite fereastra 8 - 9
[LINE:224]# INFO     [2020-05-05 10:19:23,554]  Mai sunt 93 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:23,554]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:23,554]  Header segment 8 trimis: [seq_nr: 201986] , [check:  306] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:23,555]  Header segment 9 trimis: [seq_nr: 203387] , [check:  14532] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:24,557]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:24,558]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:24,559]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:19:24,559]  
[LINE:331]# INFO     [2020-05-05 10:19:24,559]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:24,559]  
[LINE:222]# INFO     [2020-05-05 10:19:24,560]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:24,560]  Se transmite fereastra 8 - 9
[LINE:224]# INFO     [2020-05-05 10:19:24,560]  Mai sunt 93 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:24,560]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:24,561]  Header segment 8 trimis: [seq_nr: 201986] , [check:  306] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:24,561]  Header segment 9 trimis: [seq_nr: 203387] , [check:  14532] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:25,564]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:25,564]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:25,564]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:19:25,565]  
[LINE:331]# INFO     [2020-05-05 10:19:25,565]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:25,565]  
[LINE:222]# INFO     [2020-05-05 10:19:25,565]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:25,565]  Se transmite fereastra 8 - 9
[LINE:224]# INFO     [2020-05-05 10:19:25,565]  Mai sunt 93 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:25,566]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:25,566]  Header segment 8 trimis: [seq_nr: 201986] , [check:  306] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:25,567]  Header segment 9 trimis: [seq_nr: 203387] , [check:  14532] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:26,569]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:26,570]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:26,570]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:19:26,570]  
[LINE:331]# INFO     [2020-05-05 10:19:26,571]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:26,571]  
[LINE:222]# INFO     [2020-05-05 10:19:26,571]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:26,571]  Se transmite fereastra 8 - 9
[LINE:224]# INFO     [2020-05-05 10:19:26,572]  Mai sunt 93 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:26,572]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:26,572]  Header segment 8 trimis: [seq_nr: 201986] , [check:  306] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:26,573]  Header segment 9 trimis: [seq_nr: 203387] , [check:  14532] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:27,574]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:27,575]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:27,575]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:19:27,575]  
[LINE:331]# INFO     [2020-05-05 10:19:27,575]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:27,575]  
[LINE:222]# INFO     [2020-05-05 10:19:27,576]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:27,576]  Se transmite fereastra 8 - 9
[LINE:224]# INFO     [2020-05-05 10:19:27,576]  Mai sunt 93 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:27,576]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:27,576]  Header segment 8 trimis: [seq_nr: 201986] , [check:  306] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:27,577]  Header segment 9 trimis: [seq_nr: 203387] , [check:  14532] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:28,579]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:28,579]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:19:28,580]  Header receptor pt segment primit: [ack_nr: 203386] , [check:  1406] , [window: 4]
[LINE:290]# INFO     [2020-05-05 10:19:28,580]  Idx segmente confirmate: [8]
[LINE:330]# INFO     [2020-05-05 10:19:28,580]  
[LINE:331]# INFO     [2020-05-05 10:19:28,580]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:28,581]  
[LINE:222]# INFO     [2020-05-05 10:19:28,581]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:28,581]  Se transmite fereastra 9 - 12
[LINE:224]# INFO     [2020-05-05 10:19:28,581]  Mai sunt 92 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:28,581]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:28,582]  Header segment 9 trimis: [seq_nr: 203386] , [check:  14533] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:28,583]  Header segment 10 trimis: [seq_nr: 204787] , [check:  24479] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:28,583]  Header segment 11 trimis: [seq_nr: 206188] , [check:  14938] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:28,584]  Header segment 12 trimis: [seq_nr: 207589] , [check:  10657] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:29,586]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:29,587]  Confirmari preluate = 2
[LINE:270]# INFO     [2020-05-05 10:19:29,588]  Header receptor pt segment primit: [ack_nr: 207588] , [check:  5396] , [window: 4]
[LINE:270]# INFO     [2020-05-05 10:19:29,588]  Header receptor pt segment primit: [ack_nr: 208989] , [check:  3998] , [window: 1]
[LINE:290]# INFO     [2020-05-05 10:19:29,589]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:29,589]  
[LINE:331]# INFO     [2020-05-05 10:19:29,589]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:29,590]  
[LINE:222]# INFO     [2020-05-05 10:19:29,590]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:29,590]  Se transmite fereastra 9 - 9
[LINE:224]# INFO     [2020-05-05 10:19:29,590]  Mai sunt 92 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:29,591]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:29,591]  Header segment 9 trimis: [seq_nr: 203386] , [check:  14533] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:30,593]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:30,594]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:19:30,594]  Header receptor pt segment primit: [ack_nr: 204786] , [check:  7] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:19:30,595]  Idx segmente confirmate: [9, 11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:30,595]  
[LINE:331]# INFO     [2020-05-05 10:19:30,595]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:30,595]  
[LINE:222]# INFO     [2020-05-05 10:19:30,596]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:30,596]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:30,596]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:30,596]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:30,597]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:31,599]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:31,600]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:31,600]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:31,600]  
[LINE:331]# INFO     [2020-05-05 10:19:31,601]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:31,601]  
[LINE:222]# INFO     [2020-05-05 10:19:31,601]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:31,601]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:31,601]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:31,601]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:31,602]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:32,604]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:32,605]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:32,605]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:32,605]  
[LINE:331]# INFO     [2020-05-05 10:19:32,605]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:32,605]  
[LINE:222]# INFO     [2020-05-05 10:19:32,606]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:32,606]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:32,606]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:32,606]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:32,607]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:33,609]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:33,609]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:33,609]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:33,609]  
[LINE:331]# INFO     [2020-05-05 10:19:33,609]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:33,609]  
[LINE:222]# INFO     [2020-05-05 10:19:33,610]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:33,610]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:33,610]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:33,610]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:33,610]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:34,612]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:34,612]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:34,612]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:34,613]  
[LINE:331]# INFO     [2020-05-05 10:19:34,613]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:34,613]  
[LINE:222]# INFO     [2020-05-05 10:19:34,613]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:34,613]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:34,613]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:34,613]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:34,614]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:35,615]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:35,616]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:35,617]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:35,617]  
[LINE:331]# INFO     [2020-05-05 10:19:35,617]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:35,618]  
[LINE:222]# INFO     [2020-05-05 10:19:35,618]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:35,618]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:35,618]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:35,618]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:35,619]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:36,621]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:36,621]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:36,622]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:36,622]  
[LINE:331]# INFO     [2020-05-05 10:19:36,622]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:36,622]  
[LINE:222]# INFO     [2020-05-05 10:19:36,622]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:36,622]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:36,622]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:36,622]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:36,623]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:37,624]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:37,624]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:37,625]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:37,625]  
[LINE:331]# INFO     [2020-05-05 10:19:37,625]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:37,625]  
[LINE:222]# INFO     [2020-05-05 10:19:37,625]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:37,625]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:37,625]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:37,626]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:37,626]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:38,628]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:38,628]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:38,629]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:38,629]  
[LINE:331]# INFO     [2020-05-05 10:19:38,629]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:38,629]  
[LINE:222]# INFO     [2020-05-05 10:19:38,629]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:38,629]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:38,629]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:38,629]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:38,630]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:39,631]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:39,632]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:39,632]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:39,632]  
[LINE:331]# INFO     [2020-05-05 10:19:39,632]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:39,632]  
[LINE:222]# INFO     [2020-05-05 10:19:39,633]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:39,633]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:39,633]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:39,633]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:39,633]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:40,635]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:40,636]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:40,636]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:40,636]  
[LINE:331]# INFO     [2020-05-05 10:19:40,636]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:40,636]  
[LINE:222]# INFO     [2020-05-05 10:19:40,636]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:40,636]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:40,637]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:40,637]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:40,637]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:41,638]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:41,639]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:41,639]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:41,639]  
[LINE:331]# INFO     [2020-05-05 10:19:41,639]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:41,639]  
[LINE:222]# INFO     [2020-05-05 10:19:41,640]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:41,640]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:41,640]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:41,640]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:41,640]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:42,642]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:42,643]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:42,643]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:42,643]  
[LINE:331]# INFO     [2020-05-05 10:19:42,643]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:42,643]  
[LINE:222]# INFO     [2020-05-05 10:19:42,644]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:42,644]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:42,644]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:42,644]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:42,644]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:43,646]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:43,647]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:43,648]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:43,648]  
[LINE:331]# INFO     [2020-05-05 10:19:43,648]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:43,648]  
[LINE:222]# INFO     [2020-05-05 10:19:43,649]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:43,649]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:43,649]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:43,649]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:43,650]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:44,652]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:44,652]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:44,653]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:44,653]  
[LINE:331]# INFO     [2020-05-05 10:19:44,653]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:44,653]  
[LINE:222]# INFO     [2020-05-05 10:19:44,653]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:44,653]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:44,654]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:44,654]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:44,654]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:45,657]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:45,657]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:45,658]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:45,658]  
[LINE:331]# INFO     [2020-05-05 10:19:45,658]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:45,658]  
[LINE:222]# INFO     [2020-05-05 10:19:45,658]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:45,658]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:45,658]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:45,659]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:45,659]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:46,661]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:46,662]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:46,662]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:46,662]  
[LINE:331]# INFO     [2020-05-05 10:19:46,662]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:46,662]  
[LINE:222]# INFO     [2020-05-05 10:19:46,662]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:46,663]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:46,663]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:46,663]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:46,663]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:47,664]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:47,664]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:47,665]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:47,666]  
[LINE:331]# INFO     [2020-05-05 10:19:47,666]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:47,666]  
[LINE:222]# INFO     [2020-05-05 10:19:47,666]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:47,666]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:47,667]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:47,667]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:47,667]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:48,669]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:48,670]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:48,671]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:48,671]  
[LINE:331]# INFO     [2020-05-05 10:19:48,671]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:48,671]  
[LINE:222]# INFO     [2020-05-05 10:19:48,672]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:48,672]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:48,672]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:48,672]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:48,673]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:49,675]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:49,676]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:49,677]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:49,677]  
[LINE:331]# INFO     [2020-05-05 10:19:49,677]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:49,678]  
[LINE:222]# INFO     [2020-05-05 10:19:49,678]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:49,678]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:49,678]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:49,679]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:49,680]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:50,682]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:50,683]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:50,683]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:50,684]  
[LINE:331]# INFO     [2020-05-05 10:19:50,684]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:50,684]  
[LINE:222]# INFO     [2020-05-05 10:19:50,684]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:50,684]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:50,684]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:50,684]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:50,685]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:51,686]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:51,687]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:51,688]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:51,689]  
[LINE:331]# INFO     [2020-05-05 10:19:51,689]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:51,689]  
[LINE:222]# INFO     [2020-05-05 10:19:51,690]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:51,690]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:51,691]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:51,691]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:51,694]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:52,697]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:52,697]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:52,698]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:52,699]  
[LINE:331]# INFO     [2020-05-05 10:19:52,699]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:52,699]  
[LINE:222]# INFO     [2020-05-05 10:19:52,700]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:52,700]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:52,701]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:52,701]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:52,702]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:53,704]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:53,704]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:53,705]  Idx segmente confirmate: [11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:53,706]  
[LINE:331]# INFO     [2020-05-05 10:19:53,706]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:53,706]  
[LINE:222]# INFO     [2020-05-05 10:19:53,706]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:53,706]  Se transmite fereastra 10 - 12
[LINE:224]# INFO     [2020-05-05 10:19:53,706]  Mai sunt 91 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:53,706]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:53,707]  Header segment 10 trimis: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:54,709]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:54,709]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:19:54,710]  Header receptor pt segment primit: [ack_nr: 206186] , [check:  6797] , [window: 5]
[LINE:290]# INFO     [2020-05-05 10:19:54,711]  Idx segmente confirmate: [10, 11, 12]
[LINE:330]# INFO     [2020-05-05 10:19:54,711]  
[LINE:331]# INFO     [2020-05-05 10:19:54,711]  Fereastra a avansat cu 3 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:54,712]  
[LINE:222]# INFO     [2020-05-05 10:19:54,712]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:54,712]  Se transmite fereastra 13 - 17
[LINE:224]# INFO     [2020-05-05 10:19:54,712]  Mai sunt 88 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:54,712]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:54,713]  Header segment 13 trimis: [seq_nr: 208986] , [check:  9895] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:54,714]  Header segment 14 trimis: [seq_nr: 210387] , [check:  28496] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:54,714]  Header segment 15 trimis: [seq_nr: 211788] , [check:  589] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:54,714]  Header segment 16 trimis: [seq_nr: 213189] , [check:  3260] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:54,715]  Header segment 17 trimis: [seq_nr: 214590] , [check:  5630] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:55,717]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:55,718]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:19:55,718]  Header receptor pt segment primit: [ack_nr: 214589] , [check:  14778] , [window: 5]
[LINE:290]# INFO     [2020-05-05 10:19:55,718]  Idx segmente confirmate: [16]
[LINE:330]# INFO     [2020-05-05 10:19:55,718]  
[LINE:331]# INFO     [2020-05-05 10:19:55,718]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:55,718]  
[LINE:222]# INFO     [2020-05-05 10:19:55,718]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:55,718]  Se transmite fereastra 13 - 17
[LINE:224]# INFO     [2020-05-05 10:19:55,718]  Mai sunt 88 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:55,719]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:55,719]  Header segment 13 trimis: [seq_nr: 208986] , [check:  9895] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:55,719]  Header segment 14 trimis: [seq_nr: 210387] , [check:  28496] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:55,720]  Header segment 15 trimis: [seq_nr: 211788] , [check:  589] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:55,720]  Header segment 17 trimis: [seq_nr: 214589] , [check:  5631] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:56,721]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:56,722]  Confirmari preluate = 2
[LINE:270]# INFO     [2020-05-05 10:19:56,722]  Header receptor pt segment primit: [ack_nr: 210386] , [check:  2600] , [window: 2]
[LINE:270]# INFO     [2020-05-05 10:19:56,722]  Header receptor pt segment primit: [ack_nr: 215989] , [check:  13380] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:19:56,723]  Idx segmente confirmate: [13, 16, 17]
[LINE:330]# INFO     [2020-05-05 10:19:56,723]  
[LINE:331]# INFO     [2020-05-05 10:19:56,723]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:56,723]  
[LINE:222]# INFO     [2020-05-05 10:19:56,723]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:56,723]  Se transmite fereastra 14 - 16
[LINE:224]# INFO     [2020-05-05 10:19:56,723]  Mai sunt 87 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:56,724]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:56,724]  Header segment 14 trimis: [seq_nr: 210386] , [check:  28497] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:56,724]  Header segment 15 trimis: [seq_nr: 211787] , [check:  590] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:57,726]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:57,726]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:57,727]  Idx segmente confirmate: [16, 17]
[LINE:330]# INFO     [2020-05-05 10:19:57,727]  
[LINE:331]# INFO     [2020-05-05 10:19:57,728]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:57,728]  
[LINE:222]# INFO     [2020-05-05 10:19:57,728]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:57,728]  Se transmite fereastra 14 - 16
[LINE:224]# INFO     [2020-05-05 10:19:57,728]  Mai sunt 87 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:57,728]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:57,729]  Header segment 14 trimis: [seq_nr: 210386] , [check:  28497] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:57,729]  Header segment 15 trimis: [seq_nr: 211787] , [check:  590] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:58,731]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:58,731]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:19:58,731]  Idx segmente confirmate: [16, 17]
[LINE:330]# INFO     [2020-05-05 10:19:58,732]  
[LINE:331]# INFO     [2020-05-05 10:19:58,732]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:58,732]  
[LINE:222]# INFO     [2020-05-05 10:19:58,732]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:58,732]  Se transmite fereastra 14 - 16
[LINE:224]# INFO     [2020-05-05 10:19:58,733]  Mai sunt 87 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:58,733]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:58,733]  Header segment 14 trimis: [seq_nr: 210386] , [check:  28497] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:19:58,734]  Header segment 15 trimis: [seq_nr: 211787] , [check:  590] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:19:59,735]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:19:59,735]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:19:59,736]  Header receptor pt segment primit: [ack_nr: 213187] , [check:  16181] , [window: 4]
[LINE:290]# INFO     [2020-05-05 10:19:59,736]  Idx segmente confirmate: [15, 16, 17]
[LINE:330]# INFO     [2020-05-05 10:19:59,736]  
[LINE:331]# INFO     [2020-05-05 10:19:59,737]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:19:59,737]  
[LINE:222]# INFO     [2020-05-05 10:19:59,737]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:19:59,737]  Se transmite fereastra 14 - 17
[LINE:224]# INFO     [2020-05-05 10:19:59,737]  Mai sunt 87 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:19:59,737]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:19:59,738]  Header segment 14 trimis: [seq_nr: 210386] , [check:  28497] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:00,739]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:00,740]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:00,741]  Idx segmente confirmate: [15, 16, 17]
[LINE:330]# INFO     [2020-05-05 10:20:00,741]  
[LINE:331]# INFO     [2020-05-05 10:20:00,741]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:00,742]  
[LINE:222]# INFO     [2020-05-05 10:20:00,742]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:00,742]  Se transmite fereastra 14 - 17
[LINE:224]# INFO     [2020-05-05 10:20:00,742]  Mai sunt 87 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:00,742]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:00,743]  Header segment 14 trimis: [seq_nr: 210386] , [check:  28497] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:01,745]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:01,745]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:01,746]  Idx segmente confirmate: [15, 16, 17]
[LINE:330]# INFO     [2020-05-05 10:20:01,746]  
[LINE:331]# INFO     [2020-05-05 10:20:01,746]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:01,746]  
[LINE:222]# INFO     [2020-05-05 10:20:01,746]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:01,746]  Se transmite fereastra 14 - 17
[LINE:224]# INFO     [2020-05-05 10:20:01,746]  Mai sunt 87 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:01,746]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:01,747]  Header segment 14 trimis: [seq_nr: 210386] , [check:  28497] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:02,748]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:02,748]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:20:02,748]  Header receptor pt segment primit: [ack_nr: 211786] , [check:  1200] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:20:02,749]  Idx segmente confirmate: [14, 15, 16, 17]
[LINE:330]# INFO     [2020-05-05 10:20:02,749]  
[LINE:331]# INFO     [2020-05-05 10:20:02,749]  Fereastra a avansat cu 4 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:02,749]  
[LINE:222]# INFO     [2020-05-05 10:20:02,749]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:02,749]  Se transmite fereastra 18 - 19
[LINE:224]# INFO     [2020-05-05 10:20:02,750]  Mai sunt 83 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:02,750]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:02,750]  Header segment 18 trimis: [seq_nr: 215986] , [check:  22279] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:02,751]  Header segment 19 trimis: [seq_nr: 217387] , [check:  10192] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:03,752]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:03,752]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:20:03,753]  Header receptor pt segment primit: [ack_nr: 218787] , [check:  10582] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:20:03,753]  Idx segmente confirmate: [19]
[LINE:330]# INFO     [2020-05-05 10:20:03,753]  
[LINE:331]# INFO     [2020-05-05 10:20:03,753]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:03,754]  
[LINE:222]# INFO     [2020-05-05 10:20:03,754]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:03,754]  Se transmite fereastra 18 - 20
[LINE:224]# INFO     [2020-05-05 10:20:03,754]  Mai sunt 83 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:03,754]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:03,754]  Header segment 18 trimis: [seq_nr: 215986] , [check:  22279] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:03,755]  Header segment 20 trimis: [seq_nr: 218787] , [check:  23073] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:04,756]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:04,756]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:04,757]  Idx segmente confirmate: [19]
[LINE:330]# INFO     [2020-05-05 10:20:04,757]  
[LINE:331]# INFO     [2020-05-05 10:20:04,757]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:04,757]  
[LINE:222]# INFO     [2020-05-05 10:20:04,757]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:04,757]  Se transmite fereastra 18 - 20
[LINE:224]# INFO     [2020-05-05 10:20:04,757]  Mai sunt 83 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:04,757]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:04,758]  Header segment 18 trimis: [seq_nr: 215986] , [check:  22279] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:04,758]  Header segment 20 trimis: [seq_nr: 218787] , [check:  23073] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:05,760]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:05,760]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:05,761]  Idx segmente confirmate: [19]
[LINE:330]# INFO     [2020-05-05 10:20:05,761]  
[LINE:331]# INFO     [2020-05-05 10:20:05,761]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:05,762]  
[LINE:222]# INFO     [2020-05-05 10:20:05,762]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:05,762]  Se transmite fereastra 18 - 20
[LINE:224]# INFO     [2020-05-05 10:20:05,762]  Mai sunt 83 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:05,762]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:05,763]  Header segment 18 trimis: [seq_nr: 215986] , [check:  22279] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:05,764]  Header segment 20 trimis: [seq_nr: 218787] , [check:  23073] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:06,765]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:06,766]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:06,767]  Idx segmente confirmate: [19]
[LINE:330]# INFO     [2020-05-05 10:20:06,767]  
[LINE:331]# INFO     [2020-05-05 10:20:06,767]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:06,767]  
[LINE:222]# INFO     [2020-05-05 10:20:06,767]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:06,768]  Se transmite fereastra 18 - 20
[LINE:224]# INFO     [2020-05-05 10:20:06,768]  Mai sunt 83 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:06,768]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:06,768]  Header segment 18 trimis: [seq_nr: 215986] , [check:  22279] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:06,769]  Header segment 20 trimis: [seq_nr: 218787] , [check:  23073] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:07,770]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:07,771]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:07,772]  Idx segmente confirmate: [19]
[LINE:330]# INFO     [2020-05-05 10:20:07,772]  
[LINE:331]# INFO     [2020-05-05 10:20:07,773]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:07,773]  
[LINE:222]# INFO     [2020-05-05 10:20:07,773]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:07,773]  Se transmite fereastra 18 - 20
[LINE:224]# INFO     [2020-05-05 10:20:07,773]  Mai sunt 83 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:07,773]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:07,774]  Header segment 18 trimis: [seq_nr: 215986] , [check:  22279] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:07,774]  Header segment 20 trimis: [seq_nr: 218787] , [check:  23073] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:08,776]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:08,776]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:08,777]  Idx segmente confirmate: [19]
[LINE:330]# INFO     [2020-05-05 10:20:08,777]  
[LINE:331]# INFO     [2020-05-05 10:20:08,777]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:08,777]  
[LINE:222]# INFO     [2020-05-05 10:20:08,777]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:08,777]  Se transmite fereastra 18 - 20
[LINE:224]# INFO     [2020-05-05 10:20:08,778]  Mai sunt 83 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:08,778]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:08,778]  Header segment 18 trimis: [seq_nr: 215986] , [check:  22279] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:08,778]  Header segment 20 trimis: [seq_nr: 218787] , [check:  23073] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:09,780]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:09,780]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:20:09,781]  Header receptor pt segment primit: [ack_nr: 217386] , [check:  11983] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:20:09,781]  Idx segmente confirmate: [18, 19]
[LINE:330]# INFO     [2020-05-05 10:20:09,781]  
[LINE:331]# INFO     [2020-05-05 10:20:09,781]  Fereastra a avansat cu 2 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:09,781]  
[LINE:222]# INFO     [2020-05-05 10:20:09,781]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:09,782]  Se transmite fereastra 20 - 22
[LINE:224]# INFO     [2020-05-05 10:20:09,782]  Mai sunt 81 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:09,782]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:09,782]  Header segment 20 trimis: [seq_nr: 218786] , [check:  23074] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:09,782]  Header segment 21 trimis: [seq_nr: 220187] , [check:  9213] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:09,783]  Header segment 22 trimis: [seq_nr: 221588] , [check:  15940] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:10,784]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:10,784]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:10,785]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:20:10,785]  
[LINE:331]# INFO     [2020-05-05 10:20:10,785]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:10,785]  
[LINE:222]# INFO     [2020-05-05 10:20:10,785]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:10,785]  Se transmite fereastra 20 - 22
[LINE:224]# INFO     [2020-05-05 10:20:10,786]  Mai sunt 81 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:10,786]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:10,786]  Header segment 20 trimis: [seq_nr: 218786] , [check:  23074] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:10,786]  Header segment 21 trimis: [seq_nr: 220187] , [check:  9213] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:10,786]  Header segment 22 trimis: [seq_nr: 221588] , [check:  15940] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:11,788]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:11,789]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:11,789]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:20:11,790]  
[LINE:331]# INFO     [2020-05-05 10:20:11,790]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:11,790]  
[LINE:222]# INFO     [2020-05-05 10:20:11,790]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:11,791]  Se transmite fereastra 20 - 22
[LINE:224]# INFO     [2020-05-05 10:20:11,791]  Mai sunt 81 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:11,791]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:11,792]  Header segment 20 trimis: [seq_nr: 218786] , [check:  23074] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:11,793]  Header segment 21 trimis: [seq_nr: 220187] , [check:  9213] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:11,793]  Header segment 22 trimis: [seq_nr: 221588] , [check:  15940] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:12,796]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:12,796]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:12,797]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:20:12,797]  
[LINE:331]# INFO     [2020-05-05 10:20:12,797]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:12,797]  
[LINE:222]# INFO     [2020-05-05 10:20:12,797]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:12,797]  Se transmite fereastra 20 - 22
[LINE:224]# INFO     [2020-05-05 10:20:12,797]  Mai sunt 81 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:12,798]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:12,798]  Header segment 20 trimis: [seq_nr: 218786] , [check:  23074] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:12,798]  Header segment 21 trimis: [seq_nr: 220187] , [check:  9213] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:12,798]  Header segment 22 trimis: [seq_nr: 221588] , [check:  15940] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:13,800]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:13,801]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:13,801]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:20:13,801]  
[LINE:331]# INFO     [2020-05-05 10:20:13,802]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:13,802]  
[LINE:222]# INFO     [2020-05-05 10:20:13,802]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:13,802]  Se transmite fereastra 20 - 22
[LINE:224]# INFO     [2020-05-05 10:20:13,802]  Mai sunt 81 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:13,802]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:13,802]  Header segment 20 trimis: [seq_nr: 218786] , [check:  23074] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:13,803]  Header segment 21 trimis: [seq_nr: 220187] , [check:  9213] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:13,803]  Header segment 22 trimis: [seq_nr: 221588] , [check:  15940] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:14,805]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:14,806]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:14,807]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:20:14,807]  
[LINE:331]# INFO     [2020-05-05 10:20:14,807]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:14,807]  
[LINE:222]# INFO     [2020-05-05 10:20:14,808]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:14,808]  Se transmite fereastra 20 - 22
[LINE:224]# INFO     [2020-05-05 10:20:14,808]  Mai sunt 81 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:14,808]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:14,809]  Header segment 20 trimis: [seq_nr: 218786] , [check:  23074] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:14,810]  Header segment 21 trimis: [seq_nr: 220187] , [check:  9213] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:14,810]  Header segment 22 trimis: [seq_nr: 221588] , [check:  15940] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:15,812]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:15,812]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:20:15,812]  Header receptor pt segment primit: [ack_nr: 221587] , [check:  7780] , [window: 5]
[LINE:290]# INFO     [2020-05-05 10:20:15,813]  Idx segmente confirmate: [21]
[LINE:330]# INFO     [2020-05-05 10:20:15,813]  
[LINE:331]# INFO     [2020-05-05 10:20:15,814]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:15,814]  
[LINE:222]# INFO     [2020-05-05 10:20:15,814]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:15,814]  Se transmite fereastra 20 - 24
[LINE:224]# INFO     [2020-05-05 10:20:15,814]  Mai sunt 81 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:15,814]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:15,814]  Header segment 20 trimis: [seq_nr: 218786] , [check:  23074] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:15,815]  Header segment 22 trimis: [seq_nr: 221587] , [check:  15941] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:15,815]  Header segment 23 trimis: [seq_nr: 222988] , [check:  5706] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:15,816]  Header segment 24 trimis: [seq_nr: 224389] , [check:  3262] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:16,817]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:16,818]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:20:16,818]  Header receptor pt segment primit: [ack_nr: 225789] , [check:  3582] , [window: 1]
[LINE:290]# INFO     [2020-05-05 10:20:16,819]  Idx segmente confirmate: [21, 24]
[LINE:330]# INFO     [2020-05-05 10:20:16,819]  
[LINE:331]# INFO     [2020-05-05 10:20:16,819]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:16,819]  
[LINE:222]# INFO     [2020-05-05 10:20:16,819]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:16,819]  Se transmite fereastra 20 - 20
[LINE:224]# INFO     [2020-05-05 10:20:16,819]  Mai sunt 81 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:16,819]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:16,820]  Header segment 20 trimis: [seq_nr: 218786] , [check:  23074] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:17,822]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:17,822]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:17,823]  Idx segmente confirmate: [21, 24]
[LINE:330]# INFO     [2020-05-05 10:20:17,823]  
[LINE:331]# INFO     [2020-05-05 10:20:17,824]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:17,824]  
[LINE:222]# INFO     [2020-05-05 10:20:17,824]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:17,824]  Se transmite fereastra 20 - 20
[LINE:224]# INFO     [2020-05-05 10:20:17,824]  Mai sunt 81 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:17,825]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:17,825]  Header segment 20 trimis: [seq_nr: 218786] , [check:  23074] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:18,827]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:18,828]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:18,828]  Idx segmente confirmate: [21, 24]
[LINE:330]# INFO     [2020-05-05 10:20:18,828]  
[LINE:331]# INFO     [2020-05-05 10:20:18,828]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:18,829]  
[LINE:222]# INFO     [2020-05-05 10:20:18,829]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:18,829]  Se transmite fereastra 20 - 20
[LINE:224]# INFO     [2020-05-05 10:20:18,829]  Mai sunt 81 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:18,829]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:18,829]  Header segment 20 trimis: [seq_nr: 218786] , [check:  23074] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:19,831]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:19,831]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:20:19,832]  Header receptor pt segment primit: [ack_nr: 220186] , [check:  9184] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:20:19,832]  Idx segmente confirmate: [20, 21, 24]
[LINE:330]# INFO     [2020-05-05 10:20:19,832]  
[LINE:331]# INFO     [2020-05-05 10:20:19,832]  Fereastra a avansat cu 2 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:19,832]  
[LINE:222]# INFO     [2020-05-05 10:20:19,833]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:19,833]  Se transmite fereastra 22 - 23
[LINE:224]# INFO     [2020-05-05 10:20:19,833]  Mai sunt 79 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:19,833]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:19,833]  Header segment 22 trimis: [seq_nr: 221586] , [check:  15942] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:19,834]  Header segment 23 trimis: [seq_nr: 222987] , [check:  5707] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:20,835]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:20,836]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:20,836]  Idx segmente confirmate: [24]
[LINE:330]# INFO     [2020-05-05 10:20:20,836]  
[LINE:331]# INFO     [2020-05-05 10:20:20,836]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:20,836]  
[LINE:222]# INFO     [2020-05-05 10:20:20,837]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:20,837]  Se transmite fereastra 22 - 23
[LINE:224]# INFO     [2020-05-05 10:20:20,837]  Mai sunt 79 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:20,837]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:20,837]  Header segment 22 trimis: [seq_nr: 221586] , [check:  15942] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:20,838]  Header segment 23 trimis: [seq_nr: 222987] , [check:  5707] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:21,840]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:21,840]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:20:21,840]  Header receptor pt segment primit: [ack_nr: 224387] , [check:  4983] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:20:21,841]  Idx segmente confirmate: [23, 24]
[LINE:330]# INFO     [2020-05-05 10:20:21,841]  
[LINE:331]# INFO     [2020-05-05 10:20:21,841]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:21,841]  
[LINE:222]# INFO     [2020-05-05 10:20:21,841]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:21,841]  Se transmite fereastra 22 - 23
[LINE:224]# INFO     [2020-05-05 10:20:21,841]  Mai sunt 79 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:21,842]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:21,842]  Header segment 22 trimis: [seq_nr: 221586] , [check:  15942] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:22,843]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:22,844]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:22,844]  Idx segmente confirmate: [23, 24]
[LINE:330]# INFO     [2020-05-05 10:20:22,844]  
[LINE:331]# INFO     [2020-05-05 10:20:22,845]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:22,845]  
[LINE:222]# INFO     [2020-05-05 10:20:22,845]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:22,845]  Se transmite fereastra 22 - 23
[LINE:224]# INFO     [2020-05-05 10:20:22,845]  Mai sunt 79 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:22,846]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:22,846]  Header segment 22 trimis: [seq_nr: 221586] , [check:  15942] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:23,848]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:23,849]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:23,849]  Idx segmente confirmate: [23, 24]
[LINE:330]# INFO     [2020-05-05 10:20:23,849]  
[LINE:331]# INFO     [2020-05-05 10:20:23,850]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:23,850]  
[LINE:222]# INFO     [2020-05-05 10:20:23,850]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:23,850]  Se transmite fereastra 22 - 23
[LINE:224]# INFO     [2020-05-05 10:20:23,850]  Mai sunt 79 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:23,850]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:23,850]  Header segment 22 trimis: [seq_nr: 221586] , [check:  15942] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:24,852]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:24,852]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:24,853]  Idx segmente confirmate: [23, 24]
[LINE:330]# INFO     [2020-05-05 10:20:24,853]  
[LINE:331]# INFO     [2020-05-05 10:20:24,853]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:24,853]  
[LINE:222]# INFO     [2020-05-05 10:20:24,853]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:24,853]  Se transmite fereastra 22 - 23
[LINE:224]# INFO     [2020-05-05 10:20:24,853]  Mai sunt 79 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:24,853]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:24,854]  Header segment 22 trimis: [seq_nr: 221586] , [check:  15942] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:25,856]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:25,856]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:20:25,857]  Header receptor pt segment primit: [ack_nr: 222986] , [check:  6385] , [window: 1]
[LINE:290]# INFO     [2020-05-05 10:20:25,858]  Idx segmente confirmate: [22, 23, 24]
[LINE:330]# INFO     [2020-05-05 10:20:25,858]  
[LINE:331]# INFO     [2020-05-05 10:20:25,858]  Fereastra a avansat cu 3 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:25,858]  
[LINE:222]# INFO     [2020-05-05 10:20:25,858]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:25,859]  Se transmite fereastra 25 - 25
[LINE:224]# INFO     [2020-05-05 10:20:25,859]  Mai sunt 76 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:25,859]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:25,859]  Header segment 25 trimis: [seq_nr: 225786] , [check:  1120] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:26,861]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:26,862]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:26,862]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:20:26,862]  
[LINE:331]# INFO     [2020-05-05 10:20:26,863]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:26,863]  
[LINE:222]# INFO     [2020-05-05 10:20:26,863]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:26,863]  Se transmite fereastra 25 - 25
[LINE:224]# INFO     [2020-05-05 10:20:26,863]  Mai sunt 76 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:26,863]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:26,863]  Header segment 25 trimis: [seq_nr: 225786] , [check:  1120] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:27,867]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:27,868]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:20:27,868]  Header receptor pt segment primit: [ack_nr: 227186] , [check:  2183] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:20:27,868]  Idx segmente confirmate: [25]
[LINE:330]# INFO     [2020-05-05 10:20:27,869]  
[LINE:331]# INFO     [2020-05-05 10:20:27,869]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:27,869]  
[LINE:222]# INFO     [2020-05-05 10:20:27,869]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:27,869]  Se transmite fereastra 26 - 28
[LINE:224]# INFO     [2020-05-05 10:20:27,869]  Mai sunt 75 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:27,869]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:27,870]  Header segment 26 trimis: [seq_nr: 227186] , [check:  1380] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:27,870]  Header segment 27 trimis: [seq_nr: 228587] , [check:  15023] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:27,870]  Header segment 28 trimis: [seq_nr: 229988] , [check:  4403] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:28,872]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:28,872]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:28,872]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:20:28,873]  
[LINE:331]# INFO     [2020-05-05 10:20:28,873]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:28,873]  
[LINE:222]# INFO     [2020-05-05 10:20:28,873]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:28,873]  Se transmite fereastra 26 - 28
[LINE:224]# INFO     [2020-05-05 10:20:28,873]  Mai sunt 75 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:28,873]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:28,873]  Header segment 26 trimis: [seq_nr: 227186] , [check:  1380] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:28,874]  Header segment 27 trimis: [seq_nr: 228587] , [check:  15023] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:28,874]  Header segment 28 trimis: [seq_nr: 229988] , [check:  4403] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:29,876]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:29,876]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:29,877]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:20:29,877]  
[LINE:331]# INFO     [2020-05-05 10:20:29,878]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:29,878]  
[LINE:222]# INFO     [2020-05-05 10:20:29,878]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:29,878]  Se transmite fereastra 26 - 28
[LINE:224]# INFO     [2020-05-05 10:20:29,878]  Mai sunt 75 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:29,879]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:29,879]  Header segment 26 trimis: [seq_nr: 227186] , [check:  1380] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:29,881]  Header segment 27 trimis: [seq_nr: 228587] , [check:  15023] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:29,882]  Header segment 28 trimis: [seq_nr: 229988] , [check:  4403] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:30,884]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:30,884]  Confirmari preluate = 2
[LINE:270]# INFO     [2020-05-05 10:20:30,884]  Header receptor pt segment primit: [ack_nr: 228586] , [check:  782] , [window: 4]
[LINE:270]# INFO     [2020-05-05 10:20:30,885]  Header receptor pt segment primit: [ack_nr: 231388] , [check:  30749] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:20:30,885]  Idx segmente confirmate: [26, 28]
[LINE:330]# INFO     [2020-05-05 10:20:30,885]  
[LINE:331]# INFO     [2020-05-05 10:20:30,885]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:30,885]  
[LINE:222]# INFO     [2020-05-05 10:20:30,886]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:30,886]  Se transmite fereastra 27 - 29
[LINE:224]# INFO     [2020-05-05 10:20:30,886]  Mai sunt 74 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:30,886]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:30,886]  Header segment 27 trimis: [seq_nr: 228586] , [check:  15024] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:30,887]  Header segment 29 trimis: [seq_nr: 231387] , [check:  27295] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:31,889]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:31,889]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:31,890]  Idx segmente confirmate: [28]
[LINE:330]# INFO     [2020-05-05 10:20:31,890]  
[LINE:331]# INFO     [2020-05-05 10:20:31,890]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:31,890]  
[LINE:222]# INFO     [2020-05-05 10:20:31,890]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:31,890]  Se transmite fereastra 27 - 29
[LINE:224]# INFO     [2020-05-05 10:20:31,890]  Mai sunt 74 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:31,890]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:31,891]  Header segment 27 trimis: [seq_nr: 228586] , [check:  15024] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:31,891]  Header segment 29 trimis: [seq_nr: 231387] , [check:  27295] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:32,893]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:32,893]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:32,893]  Idx segmente confirmate: [28]
[LINE:330]# INFO     [2020-05-05 10:20:32,894]  
[LINE:331]# INFO     [2020-05-05 10:20:32,894]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:32,894]  
[LINE:222]# INFO     [2020-05-05 10:20:32,894]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:32,894]  Se transmite fereastra 27 - 29
[LINE:224]# INFO     [2020-05-05 10:20:32,894]  Mai sunt 74 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:32,894]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:32,895]  Header segment 27 trimis: [seq_nr: 228586] , [check:  15024] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:32,895]  Header segment 29 trimis: [seq_nr: 231387] , [check:  27295] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:33,897]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:33,898]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:33,898]  Idx segmente confirmate: [28]
[LINE:330]# INFO     [2020-05-05 10:20:33,899]  
[LINE:331]# INFO     [2020-05-05 10:20:33,899]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:33,899]  
[LINE:222]# INFO     [2020-05-05 10:20:33,899]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:33,899]  Se transmite fereastra 27 - 29
[LINE:224]# INFO     [2020-05-05 10:20:33,900]  Mai sunt 74 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:33,900]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:33,900]  Header segment 27 trimis: [seq_nr: 228586] , [check:  15024] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:33,901]  Header segment 29 trimis: [seq_nr: 231387] , [check:  27295] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:34,903]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:34,903]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:34,904]  Idx segmente confirmate: [28]
[LINE:330]# INFO     [2020-05-05 10:20:34,904]  
[LINE:331]# INFO     [2020-05-05 10:20:34,904]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:34,904]  
[LINE:222]# INFO     [2020-05-05 10:20:34,905]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:34,905]  Se transmite fereastra 27 - 29
[LINE:224]# INFO     [2020-05-05 10:20:34,905]  Mai sunt 74 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:34,905]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:34,905]  Header segment 27 trimis: [seq_nr: 228586] , [check:  15024] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:34,905]  Header segment 29 trimis: [seq_nr: 231387] , [check:  27295] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:35,907]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:35,908]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:20:35,908]  Header receptor pt segment primit: [ack_nr: 232787] , [check:  29351] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:20:35,909]  Idx segmente confirmate: [28, 29]
[LINE:330]# INFO     [2020-05-05 10:20:35,909]  
[LINE:331]# INFO     [2020-05-05 10:20:35,909]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:35,909]  
[LINE:222]# INFO     [2020-05-05 10:20:35,909]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:35,910]  Se transmite fereastra 27 - 28
[LINE:224]# INFO     [2020-05-05 10:20:35,910]  Mai sunt 74 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:35,910]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:35,910]  Header segment 27 trimis: [seq_nr: 228586] , [check:  15024] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:36,912]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:36,912]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:20:36,912]  Header receptor pt segment primit: [ack_nr: 229986] , [check:  32150] , [window: 4]
[LINE:290]# INFO     [2020-05-05 10:20:36,913]  Idx segmente confirmate: [27, 28, 29]
[LINE:330]# INFO     [2020-05-05 10:20:36,913]  
[LINE:331]# INFO     [2020-05-05 10:20:36,913]  Fereastra a avansat cu 3 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:36,913]  
[LINE:222]# INFO     [2020-05-05 10:20:36,913]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:36,913]  Se transmite fereastra 30 - 33
[LINE:224]# INFO     [2020-05-05 10:20:36,913]  Mai sunt 71 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:36,914]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:36,914]  Header segment 30 trimis: [seq_nr: 232786] , [check:  3029] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:36,914]  Header segment 31 trimis: [seq_nr: 234187] , [check:  10482] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:36,914]  Header segment 32 trimis: [seq_nr: 235588] , [check:  26413] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:36,915]  Header segment 33 trimis: [seq_nr: 236989] , [check:  15684] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:37,916]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:37,916]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:37,917]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:20:37,917]  
[LINE:331]# INFO     [2020-05-05 10:20:37,917]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:37,917]  
[LINE:222]# INFO     [2020-05-05 10:20:37,917]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:37,918]  Se transmite fereastra 30 - 33
[LINE:224]# INFO     [2020-05-05 10:20:37,918]  Mai sunt 71 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:37,918]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:37,918]  Header segment 30 trimis: [seq_nr: 232786] , [check:  3029] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:37,918]  Header segment 31 trimis: [seq_nr: 234187] , [check:  10482] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:37,919]  Header segment 32 trimis: [seq_nr: 235588] , [check:  26413] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:37,919]  Header segment 33 trimis: [seq_nr: 236989] , [check:  15684] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:38,921]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:38,921]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:38,923]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:20:38,923]  
[LINE:331]# INFO     [2020-05-05 10:20:38,923]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:38,924]  
[LINE:222]# INFO     [2020-05-05 10:20:38,924]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:38,924]  Se transmite fereastra 30 - 33
[LINE:224]# INFO     [2020-05-05 10:20:38,924]  Mai sunt 71 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:38,924]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:38,925]  Header segment 30 trimis: [seq_nr: 232786] , [check:  3029] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:38,925]  Header segment 31 trimis: [seq_nr: 234187] , [check:  10482] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:38,926]  Header segment 32 trimis: [seq_nr: 235588] , [check:  26413] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:38,926]  Header segment 33 trimis: [seq_nr: 236989] , [check:  15684] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:39,928]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:39,928]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:20:39,929]  Header receptor pt segment primit: [ack_nr: 235587] , [check:  26549] , [window: 4]
[LINE:290]# INFO     [2020-05-05 10:20:39,929]  Idx segmente confirmate: [31]
[LINE:330]# INFO     [2020-05-05 10:20:39,929]  
[LINE:331]# INFO     [2020-05-05 10:20:39,929]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:39,930]  
[LINE:222]# INFO     [2020-05-05 10:20:39,930]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:39,930]  Se transmite fereastra 30 - 33
[LINE:224]# INFO     [2020-05-05 10:20:39,930]  Mai sunt 71 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:39,930]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:39,930]  Header segment 30 trimis: [seq_nr: 232786] , [check:  3029] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:39,931]  Header segment 32 trimis: [seq_nr: 235587] , [check:  26414] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:39,931]  Header segment 33 trimis: [seq_nr: 236988] , [check:  15685] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:40,933]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:40,933]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:40,934]  Idx segmente confirmate: [31]
[LINE:330]# INFO     [2020-05-05 10:20:40,934]  
[LINE:331]# INFO     [2020-05-05 10:20:40,934]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:40,935]  
[LINE:222]# INFO     [2020-05-05 10:20:40,935]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:40,935]  Se transmite fereastra 30 - 33
[LINE:224]# INFO     [2020-05-05 10:20:40,935]  Mai sunt 71 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:40,935]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:40,936]  Header segment 30 trimis: [seq_nr: 232786] , [check:  3029] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:40,936]  Header segment 32 trimis: [seq_nr: 235587] , [check:  26414] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:40,937]  Header segment 33 trimis: [seq_nr: 236988] , [check:  15685] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:41,939]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:41,939]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:41,939]  Idx segmente confirmate: [31]
[LINE:330]# INFO     [2020-05-05 10:20:41,940]  
[LINE:331]# INFO     [2020-05-05 10:20:41,940]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:41,940]  
[LINE:222]# INFO     [2020-05-05 10:20:41,940]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:41,940]  Se transmite fereastra 30 - 33
[LINE:224]# INFO     [2020-05-05 10:20:41,940]  Mai sunt 71 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:41,940]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:41,940]  Header segment 30 trimis: [seq_nr: 232786] , [check:  3029] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:41,941]  Header segment 32 trimis: [seq_nr: 235587] , [check:  26414] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:41,941]  Header segment 33 trimis: [seq_nr: 236988] , [check:  15685] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:42,943]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:42,943]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:42,944]  Idx segmente confirmate: [31]
[LINE:330]# INFO     [2020-05-05 10:20:42,944]  
[LINE:331]# INFO     [2020-05-05 10:20:42,944]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:42,944]  
[LINE:222]# INFO     [2020-05-05 10:20:42,944]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:42,944]  Se transmite fereastra 30 - 33
[LINE:224]# INFO     [2020-05-05 10:20:42,945]  Mai sunt 71 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:42,945]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:42,945]  Header segment 30 trimis: [seq_nr: 232786] , [check:  3029] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:42,945]  Header segment 32 trimis: [seq_nr: 235587] , [check:  26414] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:42,946]  Header segment 33 trimis: [seq_nr: 236988] , [check:  15685] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:43,947]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:43,947]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:43,948]  Idx segmente confirmate: [31]
[LINE:330]# INFO     [2020-05-05 10:20:43,949]  
[LINE:331]# INFO     [2020-05-05 10:20:43,949]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:43,949]  
[LINE:222]# INFO     [2020-05-05 10:20:43,949]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:43,949]  Se transmite fereastra 30 - 33
[LINE:224]# INFO     [2020-05-05 10:20:43,949]  Mai sunt 71 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:43,949]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:43,949]  Header segment 30 trimis: [seq_nr: 232786] , [check:  3029] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:43,950]  Header segment 32 trimis: [seq_nr: 235587] , [check:  26414] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:43,950]  Header segment 33 trimis: [seq_nr: 236988] , [check:  15685] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:44,952]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:44,952]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:20:44,952]  Header receptor pt segment primit: [ack_nr: 234186] , [check:  27951] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:20:44,953]  Idx segmente confirmate: [30, 31]
[LINE:330]# INFO     [2020-05-05 10:20:44,953]  
[LINE:331]# INFO     [2020-05-05 10:20:44,953]  Fereastra a avansat cu 2 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:44,953]  
[LINE:222]# INFO     [2020-05-05 10:20:44,953]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:44,953]  Se transmite fereastra 32 - 34
[LINE:224]# INFO     [2020-05-05 10:20:44,953]  Mai sunt 69 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:44,954]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:44,954]  Header segment 32 trimis: [seq_nr: 235586] , [check:  26415] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:44,954]  Header segment 33 trimis: [seq_nr: 236987] , [check:  15686] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:44,954]  Header segment 34 trimis: [seq_nr: 238388] , [check:  20406] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:45,956]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:45,956]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:45,958]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:20:45,959]  
[LINE:331]# INFO     [2020-05-05 10:20:45,959]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:45,959]  
[LINE:222]# INFO     [2020-05-05 10:20:45,959]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:45,959]  Se transmite fereastra 32 - 34
[LINE:224]# INFO     [2020-05-05 10:20:45,960]  Mai sunt 69 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:45,960]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:45,960]  Header segment 32 trimis: [seq_nr: 235586] , [check:  26415] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:45,961]  Header segment 33 trimis: [seq_nr: 236987] , [check:  15686] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:45,961]  Header segment 34 trimis: [seq_nr: 238388] , [check:  20406] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:46,963]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:46,963]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:46,964]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:20:46,964]  
[LINE:331]# INFO     [2020-05-05 10:20:46,964]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:46,964]  
[LINE:222]# INFO     [2020-05-05 10:20:46,964]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:46,964]  Se transmite fereastra 32 - 34
[LINE:224]# INFO     [2020-05-05 10:20:46,965]  Mai sunt 69 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:46,965]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:46,965]  Header segment 32 trimis: [seq_nr: 235586] , [check:  26415] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:46,965]  Header segment 33 trimis: [seq_nr: 236987] , [check:  15686] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:46,966]  Header segment 34 trimis: [seq_nr: 238388] , [check:  20406] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:47,968]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:47,969]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:47,970]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:20:47,970]  
[LINE:331]# INFO     [2020-05-05 10:20:47,970]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:47,971]  
[LINE:222]# INFO     [2020-05-05 10:20:47,971]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:47,971]  Se transmite fereastra 32 - 34
[LINE:224]# INFO     [2020-05-05 10:20:47,971]  Mai sunt 69 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:47,971]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:47,972]  Header segment 32 trimis: [seq_nr: 235586] , [check:  26415] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:47,972]  Header segment 33 trimis: [seq_nr: 236987] , [check:  15686] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:47,973]  Header segment 34 trimis: [seq_nr: 238388] , [check:  20406] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:48,975]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:48,976]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:48,976]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:20:48,976]  
[LINE:331]# INFO     [2020-05-05 10:20:48,976]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:48,977]  
[LINE:222]# INFO     [2020-05-05 10:20:48,977]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:48,977]  Se transmite fereastra 32 - 34
[LINE:224]# INFO     [2020-05-05 10:20:48,977]  Mai sunt 69 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:48,977]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:48,977]  Header segment 32 trimis: [seq_nr: 235586] , [check:  26415] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:48,978]  Header segment 33 trimis: [seq_nr: 236987] , [check:  15686] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:48,978]  Header segment 34 trimis: [seq_nr: 238388] , [check:  20406] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:49,980]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:49,980]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:49,981]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:20:49,981]  
[LINE:331]# INFO     [2020-05-05 10:20:49,981]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:49,981]  
[LINE:222]# INFO     [2020-05-05 10:20:49,981]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:49,981]  Se transmite fereastra 32 - 34
[LINE:224]# INFO     [2020-05-05 10:20:49,981]  Mai sunt 69 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:49,981]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:49,982]  Header segment 32 trimis: [seq_nr: 235586] , [check:  26415] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:49,982]  Header segment 33 trimis: [seq_nr: 236987] , [check:  15686] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:49,982]  Header segment 34 trimis: [seq_nr: 238388] , [check:  20406] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:50,984]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:50,984]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:50,985]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:20:50,986]  
[LINE:331]# INFO     [2020-05-05 10:20:50,986]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:50,986]  
[LINE:222]# INFO     [2020-05-05 10:20:50,986]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:50,986]  Se transmite fereastra 32 - 34
[LINE:224]# INFO     [2020-05-05 10:20:50,987]  Mai sunt 69 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:50,987]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:50,987]  Header segment 32 trimis: [seq_nr: 235586] , [check:  26415] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:50,988]  Header segment 33 trimis: [seq_nr: 236987] , [check:  15686] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:50,989]  Header segment 34 trimis: [seq_nr: 238388] , [check:  20406] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:51,991]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:51,991]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:51,992]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:20:51,992]  
[LINE:331]# INFO     [2020-05-05 10:20:51,992]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:51,992]  
[LINE:222]# INFO     [2020-05-05 10:20:51,992]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:51,992]  Se transmite fereastra 32 - 34
[LINE:224]# INFO     [2020-05-05 10:20:51,992]  Mai sunt 69 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:51,993]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:51,993]  Header segment 32 trimis: [seq_nr: 235586] , [check:  26415] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:51,993]  Header segment 33 trimis: [seq_nr: 236987] , [check:  15686] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:51,994]  Header segment 34 trimis: [seq_nr: 238388] , [check:  20406] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:52,995]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:52,996]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:52,998]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:20:52,998]  
[LINE:331]# INFO     [2020-05-05 10:20:52,998]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:52,998]  
[LINE:222]# INFO     [2020-05-05 10:20:52,998]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:52,999]  Se transmite fereastra 32 - 34
[LINE:224]# INFO     [2020-05-05 10:20:52,999]  Mai sunt 69 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:52,999]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:52,999]  Header segment 32 trimis: [seq_nr: 235586] , [check:  26415] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:53,000]  Header segment 33 trimis: [seq_nr: 236987] , [check:  15686] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:53,001]  Header segment 34 trimis: [seq_nr: 238388] , [check:  20406] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:54,003]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:54,003]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:20:54,004]  Header receptor pt segment primit: [ack_nr: 238387] , [check:  23750] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:20:54,004]  Idx segmente confirmate: [33]
[LINE:330]# INFO     [2020-05-05 10:20:54,004]  
[LINE:331]# INFO     [2020-05-05 10:20:54,005]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:54,005]  
[LINE:222]# INFO     [2020-05-05 10:20:54,005]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:54,005]  Se transmite fereastra 32 - 34
[LINE:224]# INFO     [2020-05-05 10:20:54,005]  Mai sunt 69 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:54,005]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:54,005]  Header segment 32 trimis: [seq_nr: 235586] , [check:  26415] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:54,006]  Header segment 34 trimis: [seq_nr: 238387] , [check:  20407] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:55,008]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:55,008]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:20:55,009]  Header receptor pt segment primit: [ack_nr: 236986] , [check:  25152] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:20:55,010]  Idx segmente confirmate: [32, 33]
[LINE:330]# INFO     [2020-05-05 10:20:55,010]  
[LINE:331]# INFO     [2020-05-05 10:20:55,011]  Fereastra a avansat cu 2 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:55,011]  
[LINE:222]# INFO     [2020-05-05 10:20:55,011]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:55,011]  Se transmite fereastra 34 - 35
[LINE:224]# INFO     [2020-05-05 10:20:55,012]  Mai sunt 67 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:55,012]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:55,012]  Header segment 34 trimis: [seq_nr: 238386] , [check:  20408] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:55,013]  Header segment 35 trimis: [seq_nr: 239787] , [check:  3305] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:56,014]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:56,015]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:56,015]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:20:56,015]  
[LINE:331]# INFO     [2020-05-05 10:20:56,015]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:56,016]  
[LINE:222]# INFO     [2020-05-05 10:20:56,016]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:56,016]  Se transmite fereastra 34 - 35
[LINE:224]# INFO     [2020-05-05 10:20:56,016]  Mai sunt 67 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:56,016]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:56,016]  Header segment 34 trimis: [seq_nr: 238386] , [check:  20408] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:20:56,017]  Header segment 35 trimis: [seq_nr: 239787] , [check:  3305] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:57,018]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:57,019]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:20:57,019]  Header receptor pt segment primit: [ack_nr: 241187] , [check:  20951] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:20:57,020]  Idx segmente confirmate: [35]
[LINE:330]# INFO     [2020-05-05 10:20:57,020]  
[LINE:331]# INFO     [2020-05-05 10:20:57,020]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:57,020]  
[LINE:222]# INFO     [2020-05-05 10:20:57,020]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:57,020]  Se transmite fereastra 34 - 35
[LINE:224]# INFO     [2020-05-05 10:20:57,020]  Mai sunt 67 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:57,020]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:57,021]  Header segment 34 trimis: [seq_nr: 238386] , [check:  20408] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:58,022]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:58,023]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:58,023]  Idx segmente confirmate: [35]
[LINE:330]# INFO     [2020-05-05 10:20:58,024]  
[LINE:331]# INFO     [2020-05-05 10:20:58,024]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:58,024]  
[LINE:222]# INFO     [2020-05-05 10:20:58,024]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:58,024]  Se transmite fereastra 34 - 35
[LINE:224]# INFO     [2020-05-05 10:20:58,024]  Mai sunt 67 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:58,025]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:58,025]  Header segment 34 trimis: [seq_nr: 238386] , [check:  20408] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:20:59,027]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:20:59,028]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:20:59,031]  Idx segmente confirmate: [35]
[LINE:330]# INFO     [2020-05-05 10:20:59,032]  
[LINE:331]# INFO     [2020-05-05 10:20:59,032]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:20:59,033]  
[LINE:222]# INFO     [2020-05-05 10:20:59,033]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:20:59,033]  Se transmite fereastra 34 - 35
[LINE:224]# INFO     [2020-05-05 10:20:59,033]  Mai sunt 67 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:20:59,033]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:20:59,034]  Header segment 34 trimis: [seq_nr: 238386] , [check:  20408] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:00,036]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:00,036]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:00,037]  Idx segmente confirmate: [35]
[LINE:330]# INFO     [2020-05-05 10:21:00,037]  
[LINE:331]# INFO     [2020-05-05 10:21:00,037]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:00,037]  
[LINE:222]# INFO     [2020-05-05 10:21:00,037]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:00,038]  Se transmite fereastra 34 - 35
[LINE:224]# INFO     [2020-05-05 10:21:00,038]  Mai sunt 67 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:00,038]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:00,038]  Header segment 34 trimis: [seq_nr: 238386] , [check:  20408] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:01,040]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:01,040]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:01,041]  Idx segmente confirmate: [35]
[LINE:330]# INFO     [2020-05-05 10:21:01,041]  
[LINE:331]# INFO     [2020-05-05 10:21:01,041]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:01,042]  
[LINE:222]# INFO     [2020-05-05 10:21:01,042]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:01,042]  Se transmite fereastra 34 - 35
[LINE:224]# INFO     [2020-05-05 10:21:01,042]  Mai sunt 67 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:01,042]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:01,042]  Header segment 34 trimis: [seq_nr: 238386] , [check:  20408] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:02,043]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:02,044]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:02,045]  Idx segmente confirmate: [35]
[LINE:330]# INFO     [2020-05-05 10:21:02,045]  
[LINE:331]# INFO     [2020-05-05 10:21:02,045]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:02,045]  
[LINE:222]# INFO     [2020-05-05 10:21:02,045]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:02,045]  Se transmite fereastra 34 - 35
[LINE:224]# INFO     [2020-05-05 10:21:02,045]  Mai sunt 67 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:02,046]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:02,046]  Header segment 34 trimis: [seq_nr: 238386] , [check:  20408] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:03,047]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:03,048]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:03,048]  Idx segmente confirmate: [35]
[LINE:330]# INFO     [2020-05-05 10:21:03,049]  
[LINE:331]# INFO     [2020-05-05 10:21:03,049]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:03,049]  
[LINE:222]# INFO     [2020-05-05 10:21:03,049]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:03,049]  Se transmite fereastra 34 - 35
[LINE:224]# INFO     [2020-05-05 10:21:03,049]  Mai sunt 67 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:03,049]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:03,050]  Header segment 34 trimis: [seq_nr: 238386] , [check:  20408] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:04,052]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:04,053]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:04,054]  Idx segmente confirmate: [35]
[LINE:330]# INFO     [2020-05-05 10:21:04,054]  
[LINE:331]# INFO     [2020-05-05 10:21:04,054]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:04,055]  
[LINE:222]# INFO     [2020-05-05 10:21:04,055]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:04,055]  Se transmite fereastra 34 - 35
[LINE:224]# INFO     [2020-05-05 10:21:04,055]  Mai sunt 67 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:04,056]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:04,056]  Header segment 34 trimis: [seq_nr: 238386] , [check:  20408] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:05,058]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:05,059]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:05,060]  Idx segmente confirmate: [35]
[LINE:330]# INFO     [2020-05-05 10:21:05,061]  
[LINE:331]# INFO     [2020-05-05 10:21:05,061]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:05,061]  
[LINE:222]# INFO     [2020-05-05 10:21:05,061]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:05,061]  Se transmite fereastra 34 - 35
[LINE:224]# INFO     [2020-05-05 10:21:05,061]  Mai sunt 67 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:05,061]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:05,062]  Header segment 34 trimis: [seq_nr: 238386] , [check:  20408] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:06,064]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:06,065]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:21:06,065]  Header receptor pt segment primit: [ack_nr: 239786] , [check:  22350] , [window: 4]
[LINE:290]# INFO     [2020-05-05 10:21:06,067]  Idx segmente confirmate: [34, 35]
[LINE:330]# INFO     [2020-05-05 10:21:06,067]  
[LINE:331]# INFO     [2020-05-05 10:21:06,067]  Fereastra a avansat cu 2 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:06,068]  
[LINE:222]# INFO     [2020-05-05 10:21:06,068]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:06,068]  Se transmite fereastra 36 - 39
[LINE:224]# INFO     [2020-05-05 10:21:06,069]  Mai sunt 65 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:06,069]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:06,070]  Header segment 36 trimis: [seq_nr: 241186] , [check:  10347] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:06,070]  Header segment 37 trimis: [seq_nr: 242587] , [check:  1478] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:06,071]  Header segment 38 trimis: [seq_nr: 243988] , [check:  4297] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:06,071]  Header segment 39 trimis: [seq_nr: 245389] , [check:  22039] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:07,073]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:07,073]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:07,074]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:07,074]  
[LINE:331]# INFO     [2020-05-05 10:21:07,074]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:07,074]  
[LINE:222]# INFO     [2020-05-05 10:21:07,075]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:07,075]  Se transmite fereastra 36 - 39
[LINE:224]# INFO     [2020-05-05 10:21:07,075]  Mai sunt 65 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:07,075]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:07,075]  Header segment 36 trimis: [seq_nr: 241186] , [check:  10347] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:07,076]  Header segment 37 trimis: [seq_nr: 242587] , [check:  1478] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:07,076]  Header segment 38 trimis: [seq_nr: 243988] , [check:  4297] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:07,077]  Header segment 39 trimis: [seq_nr: 245389] , [check:  22039] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:08,079]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:08,080]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:08,081]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:08,082]  
[LINE:331]# INFO     [2020-05-05 10:21:08,082]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:08,082]  
[LINE:222]# INFO     [2020-05-05 10:21:08,082]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:08,082]  Se transmite fereastra 36 - 39
[LINE:224]# INFO     [2020-05-05 10:21:08,083]  Mai sunt 65 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:08,083]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:08,084]  Header segment 36 trimis: [seq_nr: 241186] , [check:  10347] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:08,085]  Header segment 37 trimis: [seq_nr: 242587] , [check:  1478] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:08,085]  Header segment 38 trimis: [seq_nr: 243988] , [check:  4297] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:08,086]  Header segment 39 trimis: [seq_nr: 245389] , [check:  22039] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:09,088]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:09,089]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:09,089]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:09,089]  
[LINE:331]# INFO     [2020-05-05 10:21:09,090]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:09,090]  
[LINE:222]# INFO     [2020-05-05 10:21:09,090]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:09,090]  Se transmite fereastra 36 - 39
[LINE:224]# INFO     [2020-05-05 10:21:09,090]  Mai sunt 65 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:09,090]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:09,091]  Header segment 36 trimis: [seq_nr: 241186] , [check:  10347] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:09,091]  Header segment 37 trimis: [seq_nr: 242587] , [check:  1478] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:09,092]  Header segment 38 trimis: [seq_nr: 243988] , [check:  4297] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:09,092]  Header segment 39 trimis: [seq_nr: 245389] , [check:  22039] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:10,094]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:10,094]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:10,095]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:10,095]  
[LINE:331]# INFO     [2020-05-05 10:21:10,095]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:10,095]  
[LINE:222]# INFO     [2020-05-05 10:21:10,095]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:10,095]  Se transmite fereastra 36 - 39
[LINE:224]# INFO     [2020-05-05 10:21:10,096]  Mai sunt 65 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:10,096]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:10,096]  Header segment 36 trimis: [seq_nr: 241186] , [check:  10347] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:10,097]  Header segment 37 trimis: [seq_nr: 242587] , [check:  1478] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:10,097]  Header segment 38 trimis: [seq_nr: 243988] , [check:  4297] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:10,098]  Header segment 39 trimis: [seq_nr: 245389] , [check:  22039] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:11,100]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:11,100]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:11,101]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:11,101]  
[LINE:331]# INFO     [2020-05-05 10:21:11,101]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:11,101]  
[LINE:222]# INFO     [2020-05-05 10:21:11,101]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:11,102]  Se transmite fereastra 36 - 39
[LINE:224]# INFO     [2020-05-05 10:21:11,102]  Mai sunt 65 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:11,102]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:11,102]  Header segment 36 trimis: [seq_nr: 241186] , [check:  10347] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:11,102]  Header segment 37 trimis: [seq_nr: 242587] , [check:  1478] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:11,103]  Header segment 38 trimis: [seq_nr: 243988] , [check:  4297] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:11,103]  Header segment 39 trimis: [seq_nr: 245389] , [check:  22039] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:12,105]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:12,105]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:12,106]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:12,106]  
[LINE:331]# INFO     [2020-05-05 10:21:12,106]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:12,106]  
[LINE:222]# INFO     [2020-05-05 10:21:12,106]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:12,107]  Se transmite fereastra 36 - 39
[LINE:224]# INFO     [2020-05-05 10:21:12,107]  Mai sunt 65 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:12,107]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:12,107]  Header segment 36 trimis: [seq_nr: 241186] , [check:  10347] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:12,107]  Header segment 37 trimis: [seq_nr: 242587] , [check:  1478] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:12,108]  Header segment 38 trimis: [seq_nr: 243988] , [check:  4297] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:12,108]  Header segment 39 trimis: [seq_nr: 245389] , [check:  22039] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:13,110]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:13,110]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:13,112]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:13,112]  
[LINE:331]# INFO     [2020-05-05 10:21:13,112]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:13,113]  
[LINE:222]# INFO     [2020-05-05 10:21:13,113]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:13,113]  Se transmite fereastra 36 - 39
[LINE:224]# INFO     [2020-05-05 10:21:13,114]  Mai sunt 65 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:13,114]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:13,115]  Header segment 36 trimis: [seq_nr: 241186] , [check:  10347] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:13,115]  Header segment 37 trimis: [seq_nr: 242587] , [check:  1478] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:13,116]  Header segment 38 trimis: [seq_nr: 243988] , [check:  4297] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:13,119]  Header segment 39 trimis: [seq_nr: 245389] , [check:  22039] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:14,121]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:14,121]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:21:14,122]  Header receptor pt segment primit: [ack_nr: 245388] , [check:  16751] , [window: 1]
[LINE:290]# INFO     [2020-05-05 10:21:14,123]  Idx segmente confirmate: [38]
[LINE:330]# INFO     [2020-05-05 10:21:14,123]  
[LINE:331]# INFO     [2020-05-05 10:21:14,123]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:14,124]  
[LINE:222]# INFO     [2020-05-05 10:21:14,124]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:14,124]  Se transmite fereastra 36 - 36
[LINE:224]# INFO     [2020-05-05 10:21:14,124]  Mai sunt 65 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:14,124]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:14,125]  Header segment 36 trimis: [seq_nr: 241186] , [check:  10347] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:15,127]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:15,128]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:21:15,128]  Header receptor pt segment primit: [ack_nr: 242586] , [check:  19551] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:21:15,129]  Idx segmente confirmate: [36, 38]
[LINE:330]# INFO     [2020-05-05 10:21:15,129]  
[LINE:331]# INFO     [2020-05-05 10:21:15,129]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:15,129]  
[LINE:222]# INFO     [2020-05-05 10:21:15,129]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:15,129]  Se transmite fereastra 37 - 39
[LINE:224]# INFO     [2020-05-05 10:21:15,129]  Mai sunt 64 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:15,130]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:15,130]  Header segment 37 trimis: [seq_nr: 242586] , [check:  1479] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:15,130]  Header segment 39 trimis: [seq_nr: 245387] , [check:  22041] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:16,132]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:16,132]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:16,133]  Idx segmente confirmate: [38]
[LINE:330]# INFO     [2020-05-05 10:21:16,133]  
[LINE:331]# INFO     [2020-05-05 10:21:16,133]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:16,133]  
[LINE:222]# INFO     [2020-05-05 10:21:16,134]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:16,134]  Se transmite fereastra 37 - 39
[LINE:224]# INFO     [2020-05-05 10:21:16,134]  Mai sunt 64 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:16,134]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:16,134]  Header segment 37 trimis: [seq_nr: 242586] , [check:  1479] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:16,135]  Header segment 39 trimis: [seq_nr: 245387] , [check:  22041] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:17,136]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:17,136]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:17,137]  Idx segmente confirmate: [38]
[LINE:330]# INFO     [2020-05-05 10:21:17,137]  
[LINE:331]# INFO     [2020-05-05 10:21:17,138]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:17,138]  
[LINE:222]# INFO     [2020-05-05 10:21:17,138]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:17,138]  Se transmite fereastra 37 - 39
[LINE:224]# INFO     [2020-05-05 10:21:17,138]  Mai sunt 64 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:17,138]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:17,139]  Header segment 37 trimis: [seq_nr: 242586] , [check:  1479] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:17,139]  Header segment 39 trimis: [seq_nr: 245387] , [check:  22041] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:18,141]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:18,141]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:21:18,141]  Header receptor pt segment primit: [ack_nr: 246787] , [check:  15348] , [window: 5]
[LINE:290]# INFO     [2020-05-05 10:21:18,142]  Idx segmente confirmate: [38, 39]
[LINE:330]# INFO     [2020-05-05 10:21:18,142]  
[LINE:331]# INFO     [2020-05-05 10:21:18,142]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:18,142]  
[LINE:222]# INFO     [2020-05-05 10:21:18,143]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:18,143]  Se transmite fereastra 37 - 41
[LINE:224]# INFO     [2020-05-05 10:21:18,143]  Mai sunt 64 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:18,143]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:18,143]  Header segment 37 trimis: [seq_nr: 242586] , [check:  1479] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:18,144]  Header segment 40 trimis: [seq_nr: 246787] , [check:  4599] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:18,144]  Header segment 41 trimis: [seq_nr: 248188] , [check:  12919] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:19,145]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:19,146]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:19,146]  Idx segmente confirmate: [38, 39]
[LINE:330]# INFO     [2020-05-05 10:21:19,146]  
[LINE:331]# INFO     [2020-05-05 10:21:19,147]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:19,147]  
[LINE:222]# INFO     [2020-05-05 10:21:19,147]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:19,147]  Se transmite fereastra 37 - 41
[LINE:224]# INFO     [2020-05-05 10:21:19,147]  Mai sunt 64 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:19,147]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:19,148]  Header segment 37 trimis: [seq_nr: 242586] , [check:  1479] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:19,148]  Header segment 40 trimis: [seq_nr: 246787] , [check:  4599] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:19,148]  Header segment 41 trimis: [seq_nr: 248188] , [check:  12919] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:20,150]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:20,151]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:21:20,151]  Header receptor pt segment primit: [ack_nr: 243986] , [check:  18152] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:21:20,152]  Idx segmente confirmate: [37, 38, 39]
[LINE:330]# INFO     [2020-05-05 10:21:20,152]  
[LINE:331]# INFO     [2020-05-05 10:21:20,152]  Fereastra a avansat cu 3 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:20,152]  
[LINE:222]# INFO     [2020-05-05 10:21:20,152]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:20,152]  Se transmite fereastra 40 - 41
[LINE:224]# INFO     [2020-05-05 10:21:20,152]  Mai sunt 61 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:20,153]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:20,153]  Header segment 40 trimis: [seq_nr: 246786] , [check:  4600] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:20,153]  Header segment 41 trimis: [seq_nr: 248187] , [check:  12920] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:21,155]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:21,155]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:21,156]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:21,156]  
[LINE:331]# INFO     [2020-05-05 10:21:21,156]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:21,156]  
[LINE:222]# INFO     [2020-05-05 10:21:21,156]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:21,156]  Se transmite fereastra 40 - 41
[LINE:224]# INFO     [2020-05-05 10:21:21,157]  Mai sunt 61 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:21,157]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:21,157]  Header segment 40 trimis: [seq_nr: 246786] , [check:  4600] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:21,157]  Header segment 41 trimis: [seq_nr: 248187] , [check:  12920] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:22,159]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:22,159]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:22,161]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:22,161]  
[LINE:331]# INFO     [2020-05-05 10:21:22,161]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:22,162]  
[LINE:222]# INFO     [2020-05-05 10:21:22,162]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:22,162]  Se transmite fereastra 40 - 41
[LINE:224]# INFO     [2020-05-05 10:21:22,162]  Mai sunt 61 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:22,163]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:22,163]  Header segment 40 trimis: [seq_nr: 246786] , [check:  4600] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:22,164]  Header segment 41 trimis: [seq_nr: 248187] , [check:  12920] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:23,166]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:23,166]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:23,167]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:23,167]  
[LINE:331]# INFO     [2020-05-05 10:21:23,167]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:23,167]  
[LINE:222]# INFO     [2020-05-05 10:21:23,167]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:23,168]  Se transmite fereastra 40 - 41
[LINE:224]# INFO     [2020-05-05 10:21:23,168]  Mai sunt 61 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:23,168]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:23,168]  Header segment 40 trimis: [seq_nr: 246786] , [check:  4600] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:23,169]  Header segment 41 trimis: [seq_nr: 248187] , [check:  12920] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:24,171]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:24,171]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:21:24,171]  Header receptor pt segment primit: [ack_nr: 248186] , [check:  13950] , [window: 4]
[LINE:290]# INFO     [2020-05-05 10:21:24,172]  Idx segmente confirmate: [40]
[LINE:330]# INFO     [2020-05-05 10:21:24,172]  
[LINE:331]# INFO     [2020-05-05 10:21:24,172]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:24,173]  
[LINE:222]# INFO     [2020-05-05 10:21:24,173]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:24,173]  Se transmite fereastra 41 - 44
[LINE:224]# INFO     [2020-05-05 10:21:24,173]  Mai sunt 60 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:24,173]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:24,174]  Header segment 41 trimis: [seq_nr: 248186] , [check:  12921] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:24,174]  Header segment 42 trimis: [seq_nr: 249587] , [check:  8129] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:24,175]  Header segment 43 trimis: [seq_nr: 250988] , [check:  7815] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:24,175]  Header segment 44 trimis: [seq_nr: 252389] , [check:  5974] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:25,176]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:25,177]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:21:25,177]  Header receptor pt segment primit: [ack_nr: 253789] , [check:  8348] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:21:25,179]  Idx segmente confirmate: [44]
[LINE:330]# INFO     [2020-05-05 10:21:25,180]  
[LINE:331]# INFO     [2020-05-05 10:21:25,180]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:25,180]  
[LINE:222]# INFO     [2020-05-05 10:21:25,180]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:25,181]  Se transmite fereastra 41 - 43
[LINE:224]# INFO     [2020-05-05 10:21:25,181]  Mai sunt 60 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:25,181]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:25,182]  Header segment 41 trimis: [seq_nr: 248186] , [check:  12921] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:25,183]  Header segment 42 trimis: [seq_nr: 249587] , [check:  8129] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:25,183]  Header segment 43 trimis: [seq_nr: 250988] , [check:  7815] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:26,186]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:26,186]  Confirmari preluate = 2
[LINE:270]# INFO     [2020-05-05 10:21:26,187]  Header receptor pt segment primit: [ack_nr: 249586] , [check:  12550] , [window: 4]
[LINE:270]# INFO     [2020-05-05 10:21:26,187]  Header receptor pt segment primit: [ack_nr: 252388] , [check:  9749] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:21:26,188]  Idx segmente confirmate: [41, 43, 44]
[LINE:330]# INFO     [2020-05-05 10:21:26,188]  
[LINE:331]# INFO     [2020-05-05 10:21:26,189]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:26,189]  
[LINE:222]# INFO     [2020-05-05 10:21:26,189]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:26,189]  Se transmite fereastra 42 - 44
[LINE:224]# INFO     [2020-05-05 10:21:26,189]  Mai sunt 59 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:26,189]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:26,190]  Header segment 42 trimis: [seq_nr: 249586] , [check:  8130] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:27,192]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:27,193]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:27,196]  Idx segmente confirmate: [43, 44]
[LINE:330]# INFO     [2020-05-05 10:21:27,197]  
[LINE:331]# INFO     [2020-05-05 10:21:27,197]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:27,197]  
[LINE:222]# INFO     [2020-05-05 10:21:27,198]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:27,198]  Se transmite fereastra 42 - 44
[LINE:224]# INFO     [2020-05-05 10:21:27,199]  Mai sunt 59 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:27,199]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:27,200]  Header segment 42 trimis: [seq_nr: 249586] , [check:  8130] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:28,203]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:28,204]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:21:28,204]  Header receptor pt segment primit: [ack_nr: 250986] , [check:  11153] , [window: 1]
[LINE:290]# INFO     [2020-05-05 10:21:28,206]  Idx segmente confirmate: [42, 43, 44]
[LINE:330]# INFO     [2020-05-05 10:21:28,206]  
[LINE:331]# INFO     [2020-05-05 10:21:28,207]  Fereastra a avansat cu 3 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:28,207]  
[LINE:222]# INFO     [2020-05-05 10:21:28,207]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:28,208]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:28,208]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:28,208]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:28,209]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:29,211]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:29,211]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:29,212]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:29,212]  
[LINE:331]# INFO     [2020-05-05 10:21:29,212]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:29,212]  
[LINE:222]# INFO     [2020-05-05 10:21:29,212]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:29,212]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:29,212]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:29,213]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:29,213]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:30,215]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:30,215]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:30,216]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:30,216]  
[LINE:331]# INFO     [2020-05-05 10:21:30,216]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:30,216]  
[LINE:222]# INFO     [2020-05-05 10:21:30,216]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:30,217]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:30,217]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:30,217]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:30,217]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:31,219]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:31,219]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:31,220]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:31,220]  
[LINE:331]# INFO     [2020-05-05 10:21:31,220]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:31,221]  
[LINE:222]# INFO     [2020-05-05 10:21:31,221]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:31,221]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:31,221]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:31,221]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:31,221]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:32,222]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:32,222]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:32,223]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:32,223]  
[LINE:331]# INFO     [2020-05-05 10:21:32,224]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:32,224]  
[LINE:222]# INFO     [2020-05-05 10:21:32,224]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:32,224]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:32,224]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:32,224]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:32,224]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:33,226]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:33,227]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:33,228]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:33,228]  
[LINE:331]# INFO     [2020-05-05 10:21:33,228]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:33,228]  
[LINE:222]# INFO     [2020-05-05 10:21:33,228]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:33,228]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:33,228]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:33,229]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:33,229]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:34,230]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:34,231]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:34,232]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:34,233]  
[LINE:331]# INFO     [2020-05-05 10:21:34,233]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:34,233]  
[LINE:222]# INFO     [2020-05-05 10:21:34,233]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:34,234]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:34,234]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:34,234]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:34,234]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:35,237]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:35,237]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:35,238]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:35,238]  
[LINE:331]# INFO     [2020-05-05 10:21:35,238]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:35,238]  
[LINE:222]# INFO     [2020-05-05 10:21:35,238]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:35,239]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:35,239]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:35,239]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:35,239]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:36,240]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:36,240]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:36,242]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:36,242]  
[LINE:331]# INFO     [2020-05-05 10:21:36,242]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:36,242]  
[LINE:222]# INFO     [2020-05-05 10:21:36,243]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:36,243]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:36,243]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:36,243]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:36,243]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:37,246]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:37,246]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:37,247]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:37,247]  
[LINE:331]# INFO     [2020-05-05 10:21:37,247]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:37,248]  
[LINE:222]# INFO     [2020-05-05 10:21:37,248]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:37,248]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:37,248]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:37,248]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:37,248]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:38,250]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:38,251]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:38,252]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:38,252]  
[LINE:331]# INFO     [2020-05-05 10:21:38,252]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:38,252]  
[LINE:222]# INFO     [2020-05-05 10:21:38,252]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:38,252]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:38,252]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:38,252]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:38,253]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:39,254]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:39,255]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:39,255]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:39,256]  
[LINE:331]# INFO     [2020-05-05 10:21:39,256]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:39,256]  
[LINE:222]# INFO     [2020-05-05 10:21:39,256]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:39,256]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:39,256]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:39,256]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:39,256]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:40,258]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:40,259]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:40,260]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:40,260]  
[LINE:331]# INFO     [2020-05-05 10:21:40,260]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:40,260]  
[LINE:222]# INFO     [2020-05-05 10:21:40,260]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:40,260]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:40,260]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:40,260]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:40,261]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:41,262]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:41,262]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:41,263]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:41,263]  
[LINE:331]# INFO     [2020-05-05 10:21:41,263]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:41,263]  
[LINE:222]# INFO     [2020-05-05 10:21:41,264]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:41,264]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:41,264]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:41,264]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:41,264]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:42,266]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:42,266]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:42,267]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:42,267]  
[LINE:331]# INFO     [2020-05-05 10:21:42,267]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:42,267]  
[LINE:222]# INFO     [2020-05-05 10:21:42,267]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:42,267]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:42,268]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:42,268]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:42,268]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:43,270]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:43,271]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:43,272]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:43,273]  
[LINE:331]# INFO     [2020-05-05 10:21:43,273]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:43,273]  
[LINE:222]# INFO     [2020-05-05 10:21:43,273]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:43,273]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:43,273]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:43,273]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:43,273]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:44,275]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:44,276]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:44,277]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:44,277]  
[LINE:331]# INFO     [2020-05-05 10:21:44,277]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:44,277]  
[LINE:222]# INFO     [2020-05-05 10:21:44,277]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:44,277]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:44,277]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:44,278]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:44,278]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:45,279]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:45,280]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:45,281]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:45,282]  
[LINE:331]# INFO     [2020-05-05 10:21:45,282]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:45,282]  
[LINE:222]# INFO     [2020-05-05 10:21:45,282]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:45,283]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:45,283]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:45,283]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:45,283]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:46,286]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:46,286]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:46,287]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:46,287]  
[LINE:331]# INFO     [2020-05-05 10:21:46,287]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:46,288]  
[LINE:222]# INFO     [2020-05-05 10:21:46,288]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:46,288]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:46,288]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:46,288]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:46,288]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:47,290]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:47,291]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:47,292]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:47,292]  
[LINE:331]# INFO     [2020-05-05 10:21:47,292]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:47,292]  
[LINE:222]# INFO     [2020-05-05 10:21:47,292]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:47,292]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:47,292]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:47,292]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:47,293]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:48,295]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:48,295]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:48,297]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:48,297]  
[LINE:331]# INFO     [2020-05-05 10:21:48,297]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:48,297]  
[LINE:222]# INFO     [2020-05-05 10:21:48,298]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:48,298]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:48,298]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:48,298]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:48,299]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:49,301]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:49,301]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:49,304]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:49,304]  
[LINE:331]# INFO     [2020-05-05 10:21:49,304]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:49,305]  
[LINE:222]# INFO     [2020-05-05 10:21:49,305]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:49,305]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:49,305]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:49,305]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:49,306]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:50,308]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:50,308]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:50,309]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:50,309]  
[LINE:331]# INFO     [2020-05-05 10:21:50,309]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:50,309]  
[LINE:222]# INFO     [2020-05-05 10:21:50,309]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:50,310]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:50,310]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:50,310]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:50,310]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:51,312]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:51,312]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:51,313]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:51,313]  
[LINE:331]# INFO     [2020-05-05 10:21:51,313]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:51,313]  
[LINE:222]# INFO     [2020-05-05 10:21:51,313]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:51,313]  Se transmite fereastra 45 - 45
[LINE:224]# INFO     [2020-05-05 10:21:51,314]  Mai sunt 56 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:51,314]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:51,314]  Header segment 45 trimis: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:52,315]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:52,316]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:21:52,316]  Header receptor pt segment primit: [ack_nr: 255186] , [check:  6953] , [window: 1]
[LINE:290]# INFO     [2020-05-05 10:21:52,317]  Idx segmente confirmate: [45]
[LINE:330]# INFO     [2020-05-05 10:21:52,317]  
[LINE:331]# INFO     [2020-05-05 10:21:52,317]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:52,317]  
[LINE:222]# INFO     [2020-05-05 10:21:52,317]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:52,317]  Se transmite fereastra 46 - 46
[LINE:224]# INFO     [2020-05-05 10:21:52,318]  Mai sunt 55 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:52,318]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:52,318]  Header segment 46 trimis: [seq_nr: 255186] , [check:  4035] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:53,320]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:53,320]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:53,321]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:53,321]  
[LINE:331]# INFO     [2020-05-05 10:21:53,321]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:53,321]  
[LINE:222]# INFO     [2020-05-05 10:21:53,321]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:53,321]  Se transmite fereastra 46 - 46
[LINE:224]# INFO     [2020-05-05 10:21:53,321]  Mai sunt 55 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:53,322]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:53,322]  Header segment 46 trimis: [seq_nr: 255186] , [check:  4035] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:54,324]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:54,324]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:54,325]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:54,325]  
[LINE:331]# INFO     [2020-05-05 10:21:54,325]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:54,325]  
[LINE:222]# INFO     [2020-05-05 10:21:54,325]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:54,326]  Se transmite fereastra 46 - 46
[LINE:224]# INFO     [2020-05-05 10:21:54,326]  Mai sunt 55 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:54,326]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:54,326]  Header segment 46 trimis: [seq_nr: 255186] , [check:  4035] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:55,328]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:55,328]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:55,330]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:55,330]  
[LINE:331]# INFO     [2020-05-05 10:21:55,330]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:55,330]  
[LINE:222]# INFO     [2020-05-05 10:21:55,330]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:55,331]  Se transmite fereastra 46 - 46
[LINE:224]# INFO     [2020-05-05 10:21:55,331]  Mai sunt 55 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:55,331]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:55,332]  Header segment 46 trimis: [seq_nr: 255186] , [check:  4035] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:56,334]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:56,334]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:56,335]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:56,336]  
[LINE:331]# INFO     [2020-05-05 10:21:56,336]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:56,336]  
[LINE:222]# INFO     [2020-05-05 10:21:56,336]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:56,336]  Se transmite fereastra 46 - 46
[LINE:224]# INFO     [2020-05-05 10:21:56,336]  Mai sunt 55 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:56,336]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:56,337]  Header segment 46 trimis: [seq_nr: 255186] , [check:  4035] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:57,338]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:57,339]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:57,340]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:57,341]  
[LINE:331]# INFO     [2020-05-05 10:21:57,341]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:57,341]  
[LINE:222]# INFO     [2020-05-05 10:21:57,341]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:57,341]  Se transmite fereastra 46 - 46
[LINE:224]# INFO     [2020-05-05 10:21:57,342]  Mai sunt 55 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:57,342]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:57,343]  Header segment 46 trimis: [seq_nr: 255186] , [check:  4035] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:58,345]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:58,345]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:21:58,346]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:21:58,346]  
[LINE:331]# INFO     [2020-05-05 10:21:58,346]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:58,347]  
[LINE:222]# INFO     [2020-05-05 10:21:58,347]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:58,347]  Se transmite fereastra 46 - 46
[LINE:224]# INFO     [2020-05-05 10:21:58,347]  Mai sunt 55 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:58,347]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:58,347]  Header segment 46 trimis: [seq_nr: 255186] , [check:  4035] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:21:59,350]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:21:59,350]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:21:59,350]  Header receptor pt segment primit: [ack_nr: 256586] , [check:  5551] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:21:59,351]  Idx segmente confirmate: [46]
[LINE:330]# INFO     [2020-05-05 10:21:59,351]  
[LINE:331]# INFO     [2020-05-05 10:21:59,351]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:21:59,351]  
[LINE:222]# INFO     [2020-05-05 10:21:59,351]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:21:59,352]  Se transmite fereastra 47 - 49
[LINE:224]# INFO     [2020-05-05 10:21:59,352]  Mai sunt 54 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:21:59,352]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:21:59,352]  Header segment 47 trimis: [seq_nr: 256586] , [check:  15504] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:59,352]  Header segment 48 trimis: [seq_nr: 257987] , [check:  25123] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:21:59,353]  Header segment 49 trimis: [seq_nr: 259388] , [check:  105] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:00,355]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:00,355]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:22:00,355]  Header receptor pt segment primit: [ack_nr: 257986] , [check:  4152] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:22:00,356]  Idx segmente confirmate: [47]
[LINE:330]# INFO     [2020-05-05 10:22:00,356]  
[LINE:331]# INFO     [2020-05-05 10:22:00,356]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:00,356]  
[LINE:222]# INFO     [2020-05-05 10:22:00,356]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:00,356]  Se transmite fereastra 48 - 49
[LINE:224]# INFO     [2020-05-05 10:22:00,356]  Mai sunt 53 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:00,357]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:00,357]  Header segment 48 trimis: [seq_nr: 257986] , [check:  25124] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:00,357]  Header segment 49 trimis: [seq_nr: 259387] , [check:  106] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:01,359]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:01,359]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:01,360]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:22:01,360]  
[LINE:331]# INFO     [2020-05-05 10:22:01,360]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:01,360]  
[LINE:222]# INFO     [2020-05-05 10:22:01,360]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:01,361]  Se transmite fereastra 48 - 49
[LINE:224]# INFO     [2020-05-05 10:22:01,361]  Mai sunt 53 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:01,361]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:01,361]  Header segment 48 trimis: [seq_nr: 257986] , [check:  25124] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:01,361]  Header segment 49 trimis: [seq_nr: 259387] , [check:  106] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:02,363]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:02,363]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:02,364]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:22:02,364]  
[LINE:331]# INFO     [2020-05-05 10:22:02,364]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:02,364]  
[LINE:222]# INFO     [2020-05-05 10:22:02,365]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:02,365]  Se transmite fereastra 48 - 49
[LINE:224]# INFO     [2020-05-05 10:22:02,365]  Mai sunt 53 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:02,365]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:02,365]  Header segment 48 trimis: [seq_nr: 257986] , [check:  25124] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:02,365]  Header segment 49 trimis: [seq_nr: 259387] , [check:  106] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:03,368]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:03,368]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:03,369]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:22:03,369]  
[LINE:331]# INFO     [2020-05-05 10:22:03,369]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:03,369]  
[LINE:222]# INFO     [2020-05-05 10:22:03,369]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:03,369]  Se transmite fereastra 48 - 49
[LINE:224]# INFO     [2020-05-05 10:22:03,369]  Mai sunt 53 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:03,370]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:03,370]  Header segment 48 trimis: [seq_nr: 257986] , [check:  25124] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:03,370]  Header segment 49 trimis: [seq_nr: 259387] , [check:  106] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:04,372]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:04,372]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:04,373]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:22:04,373]  
[LINE:331]# INFO     [2020-05-05 10:22:04,373]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:04,373]  
[LINE:222]# INFO     [2020-05-05 10:22:04,373]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:04,373]  Se transmite fereastra 48 - 49
[LINE:224]# INFO     [2020-05-05 10:22:04,374]  Mai sunt 53 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:04,374]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:04,374]  Header segment 48 trimis: [seq_nr: 257986] , [check:  25124] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:04,374]  Header segment 49 trimis: [seq_nr: 259387] , [check:  106] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:05,376]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:05,377]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:22:05,377]  Header receptor pt segment primit: [ack_nr: 259386] , [check:  2752] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:22:05,379]  Idx segmente confirmate: [48]
[LINE:330]# INFO     [2020-05-05 10:22:05,379]  
[LINE:331]# INFO     [2020-05-05 10:22:05,380]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:05,380]  
[LINE:222]# INFO     [2020-05-05 10:22:05,380]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:05,380]  Se transmite fereastra 49 - 50
[LINE:224]# INFO     [2020-05-05 10:22:05,380]  Mai sunt 52 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:05,381]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:05,381]  Header segment 49 trimis: [seq_nr: 259386] , [check:  107] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:05,382]  Header segment 50 trimis: [seq_nr: 260787] , [check:  20777] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:06,383]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:06,384]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:06,385]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:22:06,385]  
[LINE:331]# INFO     [2020-05-05 10:22:06,385]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:06,385]  
[LINE:222]# INFO     [2020-05-05 10:22:06,385]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:06,385]  Se transmite fereastra 49 - 50
[LINE:224]# INFO     [2020-05-05 10:22:06,385]  Mai sunt 52 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:06,386]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:06,386]  Header segment 49 trimis: [seq_nr: 259386] , [check:  107] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:06,386]  Header segment 50 trimis: [seq_nr: 260787] , [check:  20777] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:07,388]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:07,388]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:07,389]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:22:07,390]  
[LINE:331]# INFO     [2020-05-05 10:22:07,390]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:07,390]  
[LINE:222]# INFO     [2020-05-05 10:22:07,390]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:07,390]  Se transmite fereastra 49 - 50
[LINE:224]# INFO     [2020-05-05 10:22:07,390]  Mai sunt 52 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:07,390]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:07,390]  Header segment 49 trimis: [seq_nr: 259386] , [check:  107] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:07,391]  Header segment 50 trimis: [seq_nr: 260787] , [check:  20777] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:08,392]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:08,393]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:08,394]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:22:08,394]  
[LINE:331]# INFO     [2020-05-05 10:22:08,394]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:08,394]  
[LINE:222]# INFO     [2020-05-05 10:22:08,394]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:08,395]  Se transmite fereastra 49 - 50
[LINE:224]# INFO     [2020-05-05 10:22:08,395]  Mai sunt 52 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:08,395]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:08,395]  Header segment 49 trimis: [seq_nr: 259386] , [check:  107] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:08,396]  Header segment 50 trimis: [seq_nr: 260787] , [check:  20777] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:09,398]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:09,398]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:09,399]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:22:09,399]  
[LINE:331]# INFO     [2020-05-05 10:22:09,399]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:09,399]  
[LINE:222]# INFO     [2020-05-05 10:22:09,400]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:09,400]  Se transmite fereastra 49 - 50
[LINE:224]# INFO     [2020-05-05 10:22:09,400]  Mai sunt 52 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:09,400]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:09,400]  Header segment 49 trimis: [seq_nr: 259386] , [check:  107] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:09,400]  Header segment 50 trimis: [seq_nr: 260787] , [check:  20777] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:10,403]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:10,403]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:10,404]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:22:10,404]  
[LINE:331]# INFO     [2020-05-05 10:22:10,404]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:10,404]  
[LINE:222]# INFO     [2020-05-05 10:22:10,404]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:10,404]  Se transmite fereastra 49 - 50
[LINE:224]# INFO     [2020-05-05 10:22:10,404]  Mai sunt 52 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:10,405]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:10,405]  Header segment 49 trimis: [seq_nr: 259386] , [check:  107] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:10,406]  Header segment 50 trimis: [seq_nr: 260787] , [check:  20777] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:11,407]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:11,408]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:22:11,408]  Header receptor pt segment primit: [ack_nr: 260786] , [check:  1352] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:22:11,409]  Idx segmente confirmate: [49]
[LINE:330]# INFO     [2020-05-05 10:22:11,409]  
[LINE:331]# INFO     [2020-05-05 10:22:11,409]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:11,409]  
[LINE:222]# INFO     [2020-05-05 10:22:11,409]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:11,409]  Se transmite fereastra 50 - 51
[LINE:224]# INFO     [2020-05-05 10:22:11,410]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:11,410]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:11,410]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:11,410]  Header segment 51 trimis: [seq_nr: 262187] , [check:  5579] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:12,412]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:12,413]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:12,414]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:22:12,415]  
[LINE:331]# INFO     [2020-05-05 10:22:12,415]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:12,415]  
[LINE:222]# INFO     [2020-05-05 10:22:12,415]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:12,416]  Se transmite fereastra 50 - 51
[LINE:224]# INFO     [2020-05-05 10:22:12,416]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:12,416]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:12,416]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:12,417]  Header segment 51 trimis: [seq_nr: 262187] , [check:  5579] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:13,419]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:13,419]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:13,421]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:22:13,421]  
[LINE:331]# INFO     [2020-05-05 10:22:13,421]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:13,421]  
[LINE:222]# INFO     [2020-05-05 10:22:13,422]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:13,422]  Se transmite fereastra 50 - 51
[LINE:224]# INFO     [2020-05-05 10:22:13,422]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:13,422]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:13,423]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:13,423]  Header segment 51 trimis: [seq_nr: 262187] , [check:  5579] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:14,425]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:14,425]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:22:14,425]  Header receptor pt segment primit: [ack_nr: 263587] , [check:  597] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:22:14,426]  Idx segmente confirmate: [51]
[LINE:330]# INFO     [2020-05-05 10:22:14,426]  
[LINE:331]# INFO     [2020-05-05 10:22:14,427]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:14,427]  
[LINE:222]# INFO     [2020-05-05 10:22:14,427]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:14,427]  Se transmite fereastra 50 - 52
[LINE:224]# INFO     [2020-05-05 10:22:14,427]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:14,427]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:14,427]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:14,428]  Header segment 52 trimis: [seq_nr: 263587] , [check:  15493] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:15,429]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:15,430]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:22:15,430]  Header receptor pt segment primit: [ack_nr: 264987] , [check:  1245] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:22:15,431]  Idx segmente confirmate: [51, 52]
[LINE:330]# INFO     [2020-05-05 10:22:15,431]  
[LINE:331]# INFO     [2020-05-05 10:22:15,431]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:15,431]  
[LINE:222]# INFO     [2020-05-05 10:22:15,431]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:15,431]  Se transmite fereastra 50 - 52
[LINE:224]# INFO     [2020-05-05 10:22:15,431]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:15,431]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:15,432]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:16,433]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:16,433]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:16,434]  Idx segmente confirmate: [51, 52]
[LINE:330]# INFO     [2020-05-05 10:22:16,434]  
[LINE:331]# INFO     [2020-05-05 10:22:16,434]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:16,435]  
[LINE:222]# INFO     [2020-05-05 10:22:16,435]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:16,435]  Se transmite fereastra 50 - 52
[LINE:224]# INFO     [2020-05-05 10:22:16,435]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:16,435]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:16,435]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:17,437]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:17,437]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:17,439]  Idx segmente confirmate: [51, 52]
[LINE:330]# INFO     [2020-05-05 10:22:17,439]  
[LINE:331]# INFO     [2020-05-05 10:22:17,439]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:17,439]  
[LINE:222]# INFO     [2020-05-05 10:22:17,439]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:17,439]  Se transmite fereastra 50 - 52
[LINE:224]# INFO     [2020-05-05 10:22:17,440]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:17,440]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:17,440]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:18,442]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:18,442]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:18,443]  Idx segmente confirmate: [51, 52]
[LINE:330]# INFO     [2020-05-05 10:22:18,443]  
[LINE:331]# INFO     [2020-05-05 10:22:18,443]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:18,443]  
[LINE:222]# INFO     [2020-05-05 10:22:18,443]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:18,444]  Se transmite fereastra 50 - 52
[LINE:224]# INFO     [2020-05-05 10:22:18,444]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:18,444]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:18,444]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:19,446]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:19,446]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:19,447]  Idx segmente confirmate: [51, 52]
[LINE:330]# INFO     [2020-05-05 10:22:19,447]  
[LINE:331]# INFO     [2020-05-05 10:22:19,447]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:19,447]  
[LINE:222]# INFO     [2020-05-05 10:22:19,448]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:19,448]  Se transmite fereastra 50 - 52
[LINE:224]# INFO     [2020-05-05 10:22:19,448]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:19,448]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:19,448]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:20,450]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:20,450]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:20,452]  Idx segmente confirmate: [51, 52]
[LINE:330]# INFO     [2020-05-05 10:22:20,452]  
[LINE:331]# INFO     [2020-05-05 10:22:20,452]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:20,452]  
[LINE:222]# INFO     [2020-05-05 10:22:20,452]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:20,452]  Se transmite fereastra 50 - 52
[LINE:224]# INFO     [2020-05-05 10:22:20,452]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:20,452]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:20,453]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:21,455]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:21,455]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:21,457]  Idx segmente confirmate: [51, 52]
[LINE:330]# INFO     [2020-05-05 10:22:21,457]  
[LINE:331]# INFO     [2020-05-05 10:22:21,458]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:21,458]  
[LINE:222]# INFO     [2020-05-05 10:22:21,458]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:21,458]  Se transmite fereastra 50 - 52
[LINE:224]# INFO     [2020-05-05 10:22:21,458]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:21,458]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:21,459]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:22,460]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:22,461]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:22,462]  Idx segmente confirmate: [51, 52]
[LINE:330]# INFO     [2020-05-05 10:22:22,462]  
[LINE:331]# INFO     [2020-05-05 10:22:22,462]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:22,462]  
[LINE:222]# INFO     [2020-05-05 10:22:22,462]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:22,462]  Se transmite fereastra 50 - 52
[LINE:224]# INFO     [2020-05-05 10:22:22,463]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:22,463]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:22,463]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:23,465]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:23,465]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:23,466]  Idx segmente confirmate: [51, 52]
[LINE:330]# INFO     [2020-05-05 10:22:23,467]  
[LINE:331]# INFO     [2020-05-05 10:22:23,467]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:23,467]  
[LINE:222]# INFO     [2020-05-05 10:22:23,467]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:23,467]  Se transmite fereastra 50 - 52
[LINE:224]# INFO     [2020-05-05 10:22:23,467]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:23,467]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:23,468]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:24,469]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:24,470]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:24,471]  Idx segmente confirmate: [51, 52]
[LINE:330]# INFO     [2020-05-05 10:22:24,472]  
[LINE:331]# INFO     [2020-05-05 10:22:24,472]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:24,472]  
[LINE:222]# INFO     [2020-05-05 10:22:24,472]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:24,472]  Se transmite fereastra 50 - 52
[LINE:224]# INFO     [2020-05-05 10:22:24,473]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:24,473]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:24,473]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:25,474]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:25,475]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:25,477]  Idx segmente confirmate: [51, 52]
[LINE:330]# INFO     [2020-05-05 10:22:25,477]  
[LINE:331]# INFO     [2020-05-05 10:22:25,477]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:25,477]  
[LINE:222]# INFO     [2020-05-05 10:22:25,477]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:25,478]  Se transmite fereastra 50 - 52
[LINE:224]# INFO     [2020-05-05 10:22:25,478]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:25,478]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:25,478]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:26,480]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:26,481]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:26,482]  Idx segmente confirmate: [51, 52]
[LINE:330]# INFO     [2020-05-05 10:22:26,482]  
[LINE:331]# INFO     [2020-05-05 10:22:26,482]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:26,482]  
[LINE:222]# INFO     [2020-05-05 10:22:26,482]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:26,482]  Se transmite fereastra 50 - 52
[LINE:224]# INFO     [2020-05-05 10:22:26,482]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:26,482]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:26,483]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:27,483]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:27,484]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:27,485]  Idx segmente confirmate: [51, 52]
[LINE:330]# INFO     [2020-05-05 10:22:27,485]  
[LINE:331]# INFO     [2020-05-05 10:22:27,485]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:27,485]  
[LINE:222]# INFO     [2020-05-05 10:22:27,485]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:27,485]  Se transmite fereastra 50 - 52
[LINE:224]# INFO     [2020-05-05 10:22:27,485]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:27,485]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:27,485]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:28,487]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:28,487]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:28,489]  Idx segmente confirmate: [51, 52]
[LINE:330]# INFO     [2020-05-05 10:22:28,490]  
[LINE:331]# INFO     [2020-05-05 10:22:28,490]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:28,490]  
[LINE:222]# INFO     [2020-05-05 10:22:28,490]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:28,491]  Se transmite fereastra 50 - 52
[LINE:224]# INFO     [2020-05-05 10:22:28,491]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:28,491]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:28,492]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:29,493]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:29,494]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:29,495]  Idx segmente confirmate: [51, 52]
[LINE:330]# INFO     [2020-05-05 10:22:29,495]  
[LINE:331]# INFO     [2020-05-05 10:22:29,495]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:29,495]  
[LINE:222]# INFO     [2020-05-05 10:22:29,496]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:29,496]  Se transmite fereastra 50 - 52
[LINE:224]# INFO     [2020-05-05 10:22:29,496]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:29,496]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:29,496]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:30,498]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:30,498]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:30,500]  Idx segmente confirmate: [51, 52]
[LINE:330]# INFO     [2020-05-05 10:22:30,501]  
[LINE:331]# INFO     [2020-05-05 10:22:30,501]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:30,501]  
[LINE:222]# INFO     [2020-05-05 10:22:30,501]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:30,501]  Se transmite fereastra 50 - 52
[LINE:224]# INFO     [2020-05-05 10:22:30,502]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:30,502]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:30,502]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:31,504]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:31,504]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:31,505]  Idx segmente confirmate: [51, 52]
[LINE:330]# INFO     [2020-05-05 10:22:31,505]  
[LINE:331]# INFO     [2020-05-05 10:22:31,505]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:31,505]  
[LINE:222]# INFO     [2020-05-05 10:22:31,505]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:31,506]  Se transmite fereastra 50 - 52
[LINE:224]# INFO     [2020-05-05 10:22:31,506]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:31,506]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:31,506]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:32,508]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:32,508]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:32,509]  Idx segmente confirmate: [51, 52]
[LINE:330]# INFO     [2020-05-05 10:22:32,509]  
[LINE:331]# INFO     [2020-05-05 10:22:32,509]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:32,510]  
[LINE:222]# INFO     [2020-05-05 10:22:32,510]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:32,510]  Se transmite fereastra 50 - 52
[LINE:224]# INFO     [2020-05-05 10:22:32,510]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:32,510]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:32,510]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:33,513]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:33,513]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:33,514]  Idx segmente confirmate: [51, 52]
[LINE:330]# INFO     [2020-05-05 10:22:33,514]  
[LINE:331]# INFO     [2020-05-05 10:22:33,514]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:33,514]  
[LINE:222]# INFO     [2020-05-05 10:22:33,514]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:33,514]  Se transmite fereastra 50 - 52
[LINE:224]# INFO     [2020-05-05 10:22:33,515]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:33,515]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:33,515]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:34,516]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:34,516]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:34,519]  Idx segmente confirmate: [51, 52]
[LINE:330]# INFO     [2020-05-05 10:22:34,519]  
[LINE:331]# INFO     [2020-05-05 10:22:34,520]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:34,520]  
[LINE:222]# INFO     [2020-05-05 10:22:34,520]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:34,520]  Se transmite fereastra 50 - 52
[LINE:224]# INFO     [2020-05-05 10:22:34,521]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:34,521]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:34,521]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:35,524]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:35,524]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:35,526]  Idx segmente confirmate: [51, 52]
[LINE:330]# INFO     [2020-05-05 10:22:35,526]  
[LINE:331]# INFO     [2020-05-05 10:22:35,527]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:35,527]  
[LINE:222]# INFO     [2020-05-05 10:22:35,527]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:35,527]  Se transmite fereastra 50 - 52
[LINE:224]# INFO     [2020-05-05 10:22:35,527]  Mai sunt 51 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:35,527]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:35,528]  Header segment 50 trimis: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:36,530]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:36,530]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:22:36,530]  Header receptor pt segment primit: [ack_nr: 262186] , [check:  16] , [window: 1]
[LINE:290]# INFO     [2020-05-05 10:22:36,532]  Idx segmente confirmate: [50, 51, 52]
[LINE:330]# INFO     [2020-05-05 10:22:36,532]  
[LINE:331]# INFO     [2020-05-05 10:22:36,532]  Fereastra a avansat cu 3 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:36,532]  
[LINE:222]# INFO     [2020-05-05 10:22:36,532]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:36,532]  Se transmite fereastra 53 - 53
[LINE:224]# INFO     [2020-05-05 10:22:36,532]  Mai sunt 48 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:36,532]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:36,533]  Header segment 53 trimis: [seq_nr: 264986] , [check:  14237] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:37,535]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:37,535]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:37,536]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:22:37,536]  
[LINE:331]# INFO     [2020-05-05 10:22:37,537]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:37,537]  
[LINE:222]# INFO     [2020-05-05 10:22:37,537]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:37,537]  Se transmite fereastra 53 - 53
[LINE:224]# INFO     [2020-05-05 10:22:37,537]  Mai sunt 48 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:37,537]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:37,537]  Header segment 53 trimis: [seq_nr: 264986] , [check:  14237] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:38,539]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:38,539]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:38,541]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:22:38,541]  
[LINE:331]# INFO     [2020-05-05 10:22:38,541]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:38,542]  
[LINE:222]# INFO     [2020-05-05 10:22:38,542]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:38,542]  Se transmite fereastra 53 - 53
[LINE:224]# INFO     [2020-05-05 10:22:38,542]  Mai sunt 48 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:38,543]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:38,543]  Header segment 53 trimis: [seq_nr: 264986] , [check:  14237] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:39,545]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:39,546]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:39,546]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:22:39,547]  
[LINE:331]# INFO     [2020-05-05 10:22:39,547]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:39,547]  
[LINE:222]# INFO     [2020-05-05 10:22:39,547]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:39,547]  Se transmite fereastra 53 - 53
[LINE:224]# INFO     [2020-05-05 10:22:39,547]  Mai sunt 48 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:39,547]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:39,548]  Header segment 53 trimis: [seq_nr: 264986] , [check:  14237] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:40,548]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:40,549]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:40,549]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:22:40,550]  
[LINE:331]# INFO     [2020-05-05 10:22:40,550]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:40,550]  
[LINE:222]# INFO     [2020-05-05 10:22:40,550]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:40,550]  Se transmite fereastra 53 - 53
[LINE:224]# INFO     [2020-05-05 10:22:40,550]  Mai sunt 48 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:40,550]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:40,550]  Header segment 53 trimis: [seq_nr: 264986] , [check:  14237] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:41,552]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:41,552]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:41,553]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:22:41,553]  
[LINE:331]# INFO     [2020-05-05 10:22:41,554]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:41,554]  
[LINE:222]# INFO     [2020-05-05 10:22:41,554]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:41,554]  Se transmite fereastra 53 - 53
[LINE:224]# INFO     [2020-05-05 10:22:41,554]  Mai sunt 48 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:41,554]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:41,554]  Header segment 53 trimis: [seq_nr: 264986] , [check:  14237] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:42,556]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:42,556]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:42,558]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:22:42,558]  
[LINE:331]# INFO     [2020-05-05 10:22:42,558]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:42,558]  
[LINE:222]# INFO     [2020-05-05 10:22:42,559]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:42,559]  Se transmite fereastra 53 - 53
[LINE:224]# INFO     [2020-05-05 10:22:42,559]  Mai sunt 48 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:42,559]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:42,560]  Header segment 53 trimis: [seq_nr: 264986] , [check:  14237] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:43,562]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:43,562]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:43,563]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:22:43,563]  
[LINE:331]# INFO     [2020-05-05 10:22:43,563]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:43,563]  
[LINE:222]# INFO     [2020-05-05 10:22:43,563]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:43,564]  Se transmite fereastra 53 - 53
[LINE:224]# INFO     [2020-05-05 10:22:43,564]  Mai sunt 48 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:43,564]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:43,564]  Header segment 53 trimis: [seq_nr: 264986] , [check:  14237] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:44,568]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:44,569]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:22:44,569]  Header receptor pt segment primit: [ack_nr: 266386] , [check:  3943] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:22:44,570]  Idx segmente confirmate: [53]
[LINE:330]# INFO     [2020-05-05 10:22:44,570]  
[LINE:331]# INFO     [2020-05-05 10:22:44,570]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:44,571]  
[LINE:222]# INFO     [2020-05-05 10:22:44,571]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:44,571]  Se transmite fereastra 54 - 55
[LINE:224]# INFO     [2020-05-05 10:22:44,571]  Mai sunt 47 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:44,571]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:44,571]  Header segment 54 trimis: [seq_nr: 266386] , [check:  12325] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:44,572]  Header segment 55 trimis: [seq_nr: 267787] , [check:  28895] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:45,573]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:45,573]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:45,574]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:22:45,575]  
[LINE:331]# INFO     [2020-05-05 10:22:45,575]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:45,575]  
[LINE:222]# INFO     [2020-05-05 10:22:45,575]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:45,575]  Se transmite fereastra 54 - 55
[LINE:224]# INFO     [2020-05-05 10:22:45,575]  Mai sunt 47 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:45,575]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:45,576]  Header segment 54 trimis: [seq_nr: 266386] , [check:  12325] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:45,576]  Header segment 55 trimis: [seq_nr: 267787] , [check:  28895] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:46,578]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:46,578]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:46,580]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:22:46,580]  
[LINE:331]# INFO     [2020-05-05 10:22:46,580]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:46,580]  
[LINE:222]# INFO     [2020-05-05 10:22:46,580]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:46,580]  Se transmite fereastra 54 - 55
[LINE:224]# INFO     [2020-05-05 10:22:46,581]  Mai sunt 47 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:46,581]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:46,581]  Header segment 54 trimis: [seq_nr: 266386] , [check:  12325] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:46,583]  Header segment 55 trimis: [seq_nr: 267787] , [check:  28895] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:47,584]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:47,584]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:22:47,584]  Header receptor pt segment primit: [ack_nr: 267786] , [check:  2542] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:22:47,586]  Idx segmente confirmate: [54]
[LINE:330]# INFO     [2020-05-05 10:22:47,586]  
[LINE:331]# INFO     [2020-05-05 10:22:47,586]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:47,586]  
[LINE:222]# INFO     [2020-05-05 10:22:47,586]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:47,587]  Se transmite fereastra 55 - 57
[LINE:224]# INFO     [2020-05-05 10:22:47,587]  Mai sunt 46 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:47,587]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:47,587]  Header segment 55 trimis: [seq_nr: 267786] , [check:  28896] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:47,588]  Header segment 56 trimis: [seq_nr: 269187] , [check:  938] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:47,588]  Header segment 57 trimis: [seq_nr: 270588] , [check:  30637] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:48,590]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:48,591]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:48,592]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:22:48,592]  
[LINE:331]# INFO     [2020-05-05 10:22:48,592]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:48,592]  
[LINE:222]# INFO     [2020-05-05 10:22:48,592]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:48,592]  Se transmite fereastra 55 - 57
[LINE:224]# INFO     [2020-05-05 10:22:48,592]  Mai sunt 46 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:48,592]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:48,593]  Header segment 55 trimis: [seq_nr: 267786] , [check:  28896] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:48,593]  Header segment 56 trimis: [seq_nr: 269187] , [check:  938] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:48,595]  Header segment 57 trimis: [seq_nr: 270588] , [check:  30637] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:49,596]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:49,596]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:22:49,596]  Header receptor pt segment primit: [ack_nr: 270587] , [check:  7932] , [window: 4]
[LINE:290]# INFO     [2020-05-05 10:22:49,597]  Idx segmente confirmate: [56]
[LINE:330]# INFO     [2020-05-05 10:22:49,597]  
[LINE:331]# INFO     [2020-05-05 10:22:49,598]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:49,598]  
[LINE:222]# INFO     [2020-05-05 10:22:49,598]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:49,598]  Se transmite fereastra 55 - 58
[LINE:224]# INFO     [2020-05-05 10:22:49,598]  Mai sunt 46 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:49,598]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:49,598]  Header segment 55 trimis: [seq_nr: 267786] , [check:  28896] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:49,601]  Header segment 57 trimis: [seq_nr: 270587] , [check:  30638] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:49,602]  Header segment 58 trimis: [seq_nr: 271988] , [check:  1173] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:50,604]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:50,604]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:22:50,604]  Header receptor pt segment primit: [ack_nr: 269186] , [check:  1144] , [window: 1]
[LINE:290]# INFO     [2020-05-05 10:22:50,605]  Idx segmente confirmate: [55, 56]
[LINE:330]# INFO     [2020-05-05 10:22:50,605]  
[LINE:331]# INFO     [2020-05-05 10:22:50,606]  Fereastra a avansat cu 2 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:50,606]  
[LINE:222]# INFO     [2020-05-05 10:22:50,606]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:50,606]  Se transmite fereastra 57 - 57
[LINE:224]# INFO     [2020-05-05 10:22:50,606]  Mai sunt 44 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:50,606]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:50,606]  Header segment 57 trimis: [seq_nr: 270586] , [check:  30639] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:51,608]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:51,608]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:51,609]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:22:51,609]  
[LINE:331]# INFO     [2020-05-05 10:22:51,609]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:51,609]  
[LINE:222]# INFO     [2020-05-05 10:22:51,609]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:51,610]  Se transmite fereastra 57 - 57
[LINE:224]# INFO     [2020-05-05 10:22:51,610]  Mai sunt 44 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:51,610]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:51,610]  Header segment 57 trimis: [seq_nr: 270586] , [check:  30639] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:52,614]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:52,615]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:22:52,615]  Header receptor pt segment primit: [ack_nr: 271986] , [check:  6533] , [window: 4]
[LINE:290]# INFO     [2020-05-05 10:22:52,616]  Idx segmente confirmate: [57]
[LINE:330]# INFO     [2020-05-05 10:22:52,616]  
[LINE:331]# INFO     [2020-05-05 10:22:52,616]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:52,616]  
[LINE:222]# INFO     [2020-05-05 10:22:52,616]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:52,616]  Se transmite fereastra 58 - 61
[LINE:224]# INFO     [2020-05-05 10:22:52,617]  Mai sunt 43 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:52,617]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:52,617]  Header segment 58 trimis: [seq_nr: 271986] , [check:  1175] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:52,619]  Header segment 59 trimis: [seq_nr: 273387] , [check:  598] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:52,620]  Header segment 60 trimis: [seq_nr: 274788] , [check:  25264] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:52,620]  Header segment 61 trimis: [seq_nr: 276189] , [check:  16789] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:53,623]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:53,623]  Confirmari preluate = 2
[LINE:270]# INFO     [2020-05-05 10:22:53,624]  Header receptor pt segment primit: [ack_nr: 273386] , [check:  5136] , [window: 1]
[LINE:270]# INFO     [2020-05-05 10:22:53,624]  Header receptor pt segment primit: [ack_nr: 277589] , [check:  932] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:22:53,625]  Idx segmente confirmate: [58, 61]
[LINE:330]# INFO     [2020-05-05 10:22:53,625]  
[LINE:331]# INFO     [2020-05-05 10:22:53,625]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:53,625]  
[LINE:222]# INFO     [2020-05-05 10:22:53,625]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:53,626]  Se transmite fereastra 59 - 60
[LINE:224]# INFO     [2020-05-05 10:22:53,626]  Mai sunt 42 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:53,626]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:53,626]  Header segment 59 trimis: [seq_nr: 273386] , [check:  599] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:53,626]  Header segment 60 trimis: [seq_nr: 274787] , [check:  25265] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:54,627]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:54,628]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:54,629]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:22:54,629]  
[LINE:331]# INFO     [2020-05-05 10:22:54,629]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:54,630]  
[LINE:222]# INFO     [2020-05-05 10:22:54,630]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:54,630]  Se transmite fereastra 59 - 60
[LINE:224]# INFO     [2020-05-05 10:22:54,630]  Mai sunt 42 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:54,630]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:54,630]  Header segment 59 trimis: [seq_nr: 273386] , [check:  599] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:54,631]  Header segment 60 trimis: [seq_nr: 274787] , [check:  25265] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:55,632]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:55,632]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:55,633]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:22:55,633]  
[LINE:331]# INFO     [2020-05-05 10:22:55,634]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:55,634]  
[LINE:222]# INFO     [2020-05-05 10:22:55,634]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:55,634]  Se transmite fereastra 59 - 60
[LINE:224]# INFO     [2020-05-05 10:22:55,634]  Mai sunt 42 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:55,634]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:55,634]  Header segment 59 trimis: [seq_nr: 273386] , [check:  599] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:55,635]  Header segment 60 trimis: [seq_nr: 274787] , [check:  25265] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:56,636]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:56,636]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:56,637]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:22:56,637]  
[LINE:331]# INFO     [2020-05-05 10:22:56,638]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:56,638]  
[LINE:222]# INFO     [2020-05-05 10:22:56,638]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:56,638]  Se transmite fereastra 59 - 60
[LINE:224]# INFO     [2020-05-05 10:22:56,638]  Mai sunt 42 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:56,638]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:56,638]  Header segment 59 trimis: [seq_nr: 273386] , [check:  599] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:56,639]  Header segment 60 trimis: [seq_nr: 274787] , [check:  25265] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:57,640]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:57,641]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:57,642]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:22:57,642]  
[LINE:331]# INFO     [2020-05-05 10:22:57,642]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:57,642]  
[LINE:222]# INFO     [2020-05-05 10:22:57,643]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:57,643]  Se transmite fereastra 59 - 60
[LINE:224]# INFO     [2020-05-05 10:22:57,643]  Mai sunt 42 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:57,643]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:57,643]  Header segment 59 trimis: [seq_nr: 273386] , [check:  599] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:57,643]  Header segment 60 trimis: [seq_nr: 274787] , [check:  25265] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:58,644]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:58,644]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:58,646]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:22:58,646]  
[LINE:331]# INFO     [2020-05-05 10:22:58,646]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:58,646]  
[LINE:222]# INFO     [2020-05-05 10:22:58,646]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:58,646]  Se transmite fereastra 59 - 60
[LINE:224]# INFO     [2020-05-05 10:22:58,646]  Mai sunt 42 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:58,646]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:58,647]  Header segment 59 trimis: [seq_nr: 273386] , [check:  599] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:58,647]  Header segment 60 trimis: [seq_nr: 274787] , [check:  25265] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:22:59,649]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:22:59,649]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:22:59,650]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:22:59,650]  
[LINE:331]# INFO     [2020-05-05 10:22:59,651]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:22:59,651]  
[LINE:222]# INFO     [2020-05-05 10:22:59,651]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:22:59,651]  Se transmite fereastra 59 - 60
[LINE:224]# INFO     [2020-05-05 10:22:59,651]  Mai sunt 42 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:22:59,651]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:22:59,651]  Header segment 59 trimis: [seq_nr: 273386] , [check:  599] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:22:59,652]  Header segment 60 trimis: [seq_nr: 274787] , [check:  25265] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:00,654]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:00,654]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:00,655]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:00,656]  
[LINE:331]# INFO     [2020-05-05 10:23:00,656]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:00,656]  
[LINE:222]# INFO     [2020-05-05 10:23:00,656]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:00,656]  Se transmite fereastra 59 - 60
[LINE:224]# INFO     [2020-05-05 10:23:00,656]  Mai sunt 42 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:00,656]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:00,656]  Header segment 59 trimis: [seq_nr: 273386] , [check:  599] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:23:00,657]  Header segment 60 trimis: [seq_nr: 274787] , [check:  25265] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:01,658]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:01,659]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:01,660]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:01,660]  
[LINE:331]# INFO     [2020-05-05 10:23:01,660]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:01,660]  
[LINE:222]# INFO     [2020-05-05 10:23:01,661]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:01,661]  Se transmite fereastra 59 - 60
[LINE:224]# INFO     [2020-05-05 10:23:01,661]  Mai sunt 42 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:01,661]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:01,661]  Header segment 59 trimis: [seq_nr: 273386] , [check:  599] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:23:01,662]  Header segment 60 trimis: [seq_nr: 274787] , [check:  25265] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:02,664]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:02,664]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:02,666]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:02,666]  
[LINE:331]# INFO     [2020-05-05 10:23:02,666]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:02,666]  
[LINE:222]# INFO     [2020-05-05 10:23:02,666]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:02,666]  Se transmite fereastra 59 - 60
[LINE:224]# INFO     [2020-05-05 10:23:02,666]  Mai sunt 42 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:02,666]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:02,667]  Header segment 59 trimis: [seq_nr: 273386] , [check:  599] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:23:02,667]  Header segment 60 trimis: [seq_nr: 274787] , [check:  25265] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:03,669]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:03,669]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:03,670]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:03,670]  
[LINE:331]# INFO     [2020-05-05 10:23:03,671]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:03,671]  
[LINE:222]# INFO     [2020-05-05 10:23:03,671]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:03,671]  Se transmite fereastra 59 - 60
[LINE:224]# INFO     [2020-05-05 10:23:03,671]  Mai sunt 42 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:03,671]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:03,672]  Header segment 59 trimis: [seq_nr: 273386] , [check:  599] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:23:03,672]  Header segment 60 trimis: [seq_nr: 274787] , [check:  25265] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:04,674]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:04,674]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:23:04,674]  Header receptor pt segment primit: [ack_nr: 274786] , [check:  3736] , [window: 1]
[LINE:290]# INFO     [2020-05-05 10:23:04,676]  Idx segmente confirmate: [59, 61]
[LINE:330]# INFO     [2020-05-05 10:23:04,676]  
[LINE:331]# INFO     [2020-05-05 10:23:04,676]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:04,676]  
[LINE:222]# INFO     [2020-05-05 10:23:04,676]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:04,676]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:04,676]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:04,677]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:04,677]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:05,678]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:05,679]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:05,680]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:05,680]  
[LINE:331]# INFO     [2020-05-05 10:23:05,680]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:05,680]  
[LINE:222]# INFO     [2020-05-05 10:23:05,680]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:05,680]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:05,680]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:05,681]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:05,681]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:06,682]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:06,683]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:06,685]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:06,685]  
[LINE:331]# INFO     [2020-05-05 10:23:06,685]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:06,685]  
[LINE:222]# INFO     [2020-05-05 10:23:06,685]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:06,686]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:06,686]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:06,686]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:06,686]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:07,688]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:07,688]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:07,690]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:07,690]  
[LINE:331]# INFO     [2020-05-05 10:23:07,690]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:07,690]  
[LINE:222]# INFO     [2020-05-05 10:23:07,691]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:07,691]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:07,691]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:07,691]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:07,692]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:08,692]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:08,692]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:08,694]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:08,694]  
[LINE:331]# INFO     [2020-05-05 10:23:08,694]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:08,694]  
[LINE:222]# INFO     [2020-05-05 10:23:08,694]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:08,694]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:08,694]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:08,694]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:08,695]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:09,696]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:09,696]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:09,698]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:09,698]  
[LINE:331]# INFO     [2020-05-05 10:23:09,698]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:09,698]  
[LINE:222]# INFO     [2020-05-05 10:23:09,698]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:09,698]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:09,698]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:09,698]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:09,699]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:10,700]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:10,700]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:10,701]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:10,701]  
[LINE:331]# INFO     [2020-05-05 10:23:10,702]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:10,702]  
[LINE:222]# INFO     [2020-05-05 10:23:10,702]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:10,702]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:10,702]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:10,702]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:10,702]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:11,704]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:11,704]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:11,705]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:11,706]  
[LINE:331]# INFO     [2020-05-05 10:23:11,706]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:11,706]  
[LINE:222]# INFO     [2020-05-05 10:23:11,706]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:11,706]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:11,706]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:11,706]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:11,707]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:12,708]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:12,708]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:12,711]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:12,711]  
[LINE:331]# INFO     [2020-05-05 10:23:12,712]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:12,712]  
[LINE:222]# INFO     [2020-05-05 10:23:12,712]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:12,712]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:12,712]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:12,712]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:12,713]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:13,715]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:13,715]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:13,716]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:13,717]  
[LINE:331]# INFO     [2020-05-05 10:23:13,717]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:13,717]  
[LINE:222]# INFO     [2020-05-05 10:23:13,717]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:13,717]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:13,717]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:13,717]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:13,717]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:14,719]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:14,719]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:14,721]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:14,721]  
[LINE:331]# INFO     [2020-05-05 10:23:14,721]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:14,721]  
[LINE:222]# INFO     [2020-05-05 10:23:14,721]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:14,721]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:14,721]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:14,721]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:14,722]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:15,723]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:15,724]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:15,726]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:15,726]  
[LINE:331]# INFO     [2020-05-05 10:23:15,726]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:15,726]  
[LINE:222]# INFO     [2020-05-05 10:23:15,727]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:15,727]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:15,727]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:15,727]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:15,728]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:16,730]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:16,730]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:16,731]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:16,732]  
[LINE:331]# INFO     [2020-05-05 10:23:16,732]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:16,732]  
[LINE:222]# INFO     [2020-05-05 10:23:16,732]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:16,732]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:16,732]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:16,732]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:16,733]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:17,734]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:17,735]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:17,736]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:17,736]  
[LINE:331]# INFO     [2020-05-05 10:23:17,736]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:17,736]  
[LINE:222]# INFO     [2020-05-05 10:23:17,736]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:17,736]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:17,737]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:17,737]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:17,737]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:18,739]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:18,739]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:18,741]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:18,742]  
[LINE:331]# INFO     [2020-05-05 10:23:18,742]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:18,742]  
[LINE:222]# INFO     [2020-05-05 10:23:18,742]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:18,743]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:18,743]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:18,743]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:18,744]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:19,746]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:19,747]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:19,748]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:19,748]  
[LINE:331]# INFO     [2020-05-05 10:23:19,748]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:19,748]  
[LINE:222]# INFO     [2020-05-05 10:23:19,748]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:19,748]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:19,748]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:19,748]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:19,749]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:20,751]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:20,751]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:20,753]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:20,753]  
[LINE:331]# INFO     [2020-05-05 10:23:20,754]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:20,754]  
[LINE:222]# INFO     [2020-05-05 10:23:20,754]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:20,754]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:20,754]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:20,754]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:20,755]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:21,757]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:21,757]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:21,758]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:21,758]  
[LINE:331]# INFO     [2020-05-05 10:23:21,758]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:21,758]  
[LINE:222]# INFO     [2020-05-05 10:23:21,759]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:21,759]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:21,759]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:21,759]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:21,759]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:22,760]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:22,760]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:22,762]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:22,763]  
[LINE:331]# INFO     [2020-05-05 10:23:22,763]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:22,763]  
[LINE:222]# INFO     [2020-05-05 10:23:22,763]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:22,764]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:22,764]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:22,764]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:22,764]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:23,766]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:23,767]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:23,769]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:23,769]  
[LINE:331]# INFO     [2020-05-05 10:23:23,769]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:23,770]  
[LINE:222]# INFO     [2020-05-05 10:23:23,770]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:23,770]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:23,770]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:23,770]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:23,771]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:24,773]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:24,773]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:24,774]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:24,774]  
[LINE:331]# INFO     [2020-05-05 10:23:24,774]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:24,774]  
[LINE:222]# INFO     [2020-05-05 10:23:24,774]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:24,775]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:24,775]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:24,775]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:24,775]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:25,776]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:25,776]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:25,778]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:25,778]  
[LINE:331]# INFO     [2020-05-05 10:23:25,779]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:25,779]  
[LINE:222]# INFO     [2020-05-05 10:23:25,779]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:25,779]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:25,779]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:25,780]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:25,780]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:26,782]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:26,783]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:26,785]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:26,785]  
[LINE:331]# INFO     [2020-05-05 10:23:26,786]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:26,786]  
[LINE:222]# INFO     [2020-05-05 10:23:26,786]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:26,786]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:26,786]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:26,786]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:26,787]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:27,789]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:27,789]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:27,792]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:27,792]  
[LINE:331]# INFO     [2020-05-05 10:23:27,792]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:27,792]  
[LINE:222]# INFO     [2020-05-05 10:23:27,793]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:27,793]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:27,793]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:27,794]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:27,794]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:28,796]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:28,796]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:28,799]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:28,799]  
[LINE:331]# INFO     [2020-05-05 10:23:28,799]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:28,799]  
[LINE:222]# INFO     [2020-05-05 10:23:28,799]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:28,800]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:28,800]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:28,801]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:28,801]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:29,803]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:29,803]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:29,804]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:29,804]  
[LINE:331]# INFO     [2020-05-05 10:23:29,805]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:29,805]  
[LINE:222]# INFO     [2020-05-05 10:23:29,805]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:29,805]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:29,805]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:29,806]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:29,806]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:30,808]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:30,808]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:30,810]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:30,810]  
[LINE:331]# INFO     [2020-05-05 10:23:30,810]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:30,810]  
[LINE:222]# INFO     [2020-05-05 10:23:30,810]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:30,810]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:30,810]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:30,810]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:30,811]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:31,813]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:31,813]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:31,814]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:31,814]  
[LINE:331]# INFO     [2020-05-05 10:23:31,815]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:31,815]  
[LINE:222]# INFO     [2020-05-05 10:23:31,815]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:31,815]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:31,815]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:31,815]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:31,815]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:32,818]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:32,818]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:32,819]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:32,819]  
[LINE:331]# INFO     [2020-05-05 10:23:32,820]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:32,820]  
[LINE:222]# INFO     [2020-05-05 10:23:32,820]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:32,820]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:32,820]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:32,820]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:32,820]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:33,822]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:33,823]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:33,826]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:33,826]  
[LINE:331]# INFO     [2020-05-05 10:23:33,827]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:33,827]  
[LINE:222]# INFO     [2020-05-05 10:23:33,827]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:33,827]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:33,828]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:33,828]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:33,828]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:34,830]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:34,831]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:34,833]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:34,833]  
[LINE:331]# INFO     [2020-05-05 10:23:34,834]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:34,834]  
[LINE:222]# INFO     [2020-05-05 10:23:34,834]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:34,834]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:34,834]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:34,835]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:34,835]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:35,837]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:35,838]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:35,840]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:35,840]  
[LINE:331]# INFO     [2020-05-05 10:23:35,841]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:35,841]  
[LINE:222]# INFO     [2020-05-05 10:23:35,841]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:35,841]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:35,841]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:35,841]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:35,842]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:36,844]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:36,845]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:36,846]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:36,846]  
[LINE:331]# INFO     [2020-05-05 10:23:36,846]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:36,846]  
[LINE:222]# INFO     [2020-05-05 10:23:36,846]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:36,847]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:36,847]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:36,847]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:36,847]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:37,850]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:37,850]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:37,852]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:37,853]  
[LINE:331]# INFO     [2020-05-05 10:23:37,853]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:37,853]  
[LINE:222]# INFO     [2020-05-05 10:23:37,853]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:37,853]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:37,854]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:37,854]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:37,854]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:38,857]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:38,857]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:38,858]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:38,858]  
[LINE:331]# INFO     [2020-05-05 10:23:38,859]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:38,859]  
[LINE:222]# INFO     [2020-05-05 10:23:38,859]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:38,859]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:38,859]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:38,859]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:38,859]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:39,862]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:39,862]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:39,863]  Idx segmente confirmate: [61]
[LINE:330]# INFO     [2020-05-05 10:23:39,863]  
[LINE:331]# INFO     [2020-05-05 10:23:39,864]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:39,864]  
[LINE:222]# INFO     [2020-05-05 10:23:39,864]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:39,864]  Se transmite fereastra 60 - 60
[LINE:224]# INFO     [2020-05-05 10:23:39,864]  Mai sunt 41 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:39,864]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:39,864]  Header segment 60 trimis: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:40,867]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:40,867]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:23:40,868]  Header receptor pt segment primit: [ack_nr: 276186] , [check:  2332] , [window: 5]
[LINE:290]# INFO     [2020-05-05 10:23:40,870]  Idx segmente confirmate: [60, 61]
[LINE:330]# INFO     [2020-05-05 10:23:40,870]  
[LINE:331]# INFO     [2020-05-05 10:23:40,870]  Fereastra a avansat cu 2 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:40,871]  
[LINE:222]# INFO     [2020-05-05 10:23:40,871]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:40,871]  Se transmite fereastra 62 - 66
[LINE:224]# INFO     [2020-05-05 10:23:40,871]  Mai sunt 39 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:40,871]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:40,872]  Header segment 62 trimis: [seq_nr: 277586] , [check:  9919] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:23:40,872]  Header segment 63 trimis: [seq_nr: 278987] , [check:  479] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:23:40,873]  Header segment 64 trimis: [seq_nr: 280388] , [check:  7210] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:23:40,873]  Header segment 65 trimis: [seq_nr: 281789] , [check:  2899] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:23:40,874]  Header segment 66 trimis: [seq_nr: 283190] , [check:  4445] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:41,876]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:41,876]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:41,878]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:23:41,878]  
[LINE:331]# INFO     [2020-05-05 10:23:41,878]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:41,879]  
[LINE:222]# INFO     [2020-05-05 10:23:41,879]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:41,879]  Se transmite fereastra 62 - 66
[LINE:224]# INFO     [2020-05-05 10:23:41,879]  Mai sunt 39 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:41,879]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:41,880]  Header segment 62 trimis: [seq_nr: 277586] , [check:  9919] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:23:41,880]  Header segment 63 trimis: [seq_nr: 278987] , [check:  479] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:23:41,881]  Header segment 64 trimis: [seq_nr: 280388] , [check:  7210] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:23:41,881]  Header segment 65 trimis: [seq_nr: 281789] , [check:  2899] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:23:41,882]  Header segment 66 trimis: [seq_nr: 283190] , [check:  4445] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:42,884]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:42,884]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:23:42,885]  Header receptor pt segment primit: [ack_nr: 284590] , [check:  10313] , [window: 4]
[LINE:290]# INFO     [2020-05-05 10:23:42,887]  Idx segmente confirmate: [66]
[LINE:330]# INFO     [2020-05-05 10:23:42,887]  
[LINE:331]# INFO     [2020-05-05 10:23:42,887]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:42,887]  
[LINE:222]# INFO     [2020-05-05 10:23:42,887]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:42,888]  Se transmite fereastra 62 - 65
[LINE:224]# INFO     [2020-05-05 10:23:42,888]  Mai sunt 39 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:42,888]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:42,888]  Header segment 62 trimis: [seq_nr: 277586] , [check:  9919] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:23:42,889]  Header segment 63 trimis: [seq_nr: 278987] , [check:  479] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:23:42,890]  Header segment 64 trimis: [seq_nr: 280388] , [check:  7210] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:23:42,891]  Header segment 65 trimis: [seq_nr: 281789] , [check:  2899] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:43,892]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:43,892]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:23:43,892]  Header receptor pt segment primit: [ack_nr: 278986] , [check:  15920] , [window: 1]
[LINE:290]# INFO     [2020-05-05 10:23:43,893]  Idx segmente confirmate: [62, 66]
[LINE:330]# INFO     [2020-05-05 10:23:43,894]  
[LINE:331]# INFO     [2020-05-05 10:23:43,894]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:43,894]  
[LINE:222]# INFO     [2020-05-05 10:23:43,894]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:43,894]  Se transmite fereastra 63 - 63
[LINE:224]# INFO     [2020-05-05 10:23:43,894]  Mai sunt 38 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:43,894]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:43,895]  Header segment 63 trimis: [seq_nr: 278986] , [check:  480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:44,896]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:44,896]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:44,897]  Idx segmente confirmate: [66]
[LINE:330]# INFO     [2020-05-05 10:23:44,897]  
[LINE:331]# INFO     [2020-05-05 10:23:44,897]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:44,898]  
[LINE:222]# INFO     [2020-05-05 10:23:44,898]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:44,898]  Se transmite fereastra 63 - 63
[LINE:224]# INFO     [2020-05-05 10:23:44,898]  Mai sunt 38 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:44,898]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:44,898]  Header segment 63 trimis: [seq_nr: 278986] , [check:  480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:45,900]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:45,901]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:45,903]  Idx segmente confirmate: [66]
[LINE:330]# INFO     [2020-05-05 10:23:45,903]  
[LINE:331]# INFO     [2020-05-05 10:23:45,903]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:45,903]  
[LINE:222]# INFO     [2020-05-05 10:23:45,903]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:45,904]  Se transmite fereastra 63 - 63
[LINE:224]# INFO     [2020-05-05 10:23:45,904]  Mai sunt 38 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:45,904]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:45,904]  Header segment 63 trimis: [seq_nr: 278986] , [check:  480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:46,907]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:46,907]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:46,909]  Idx segmente confirmate: [66]
[LINE:330]# INFO     [2020-05-05 10:23:46,910]  
[LINE:331]# INFO     [2020-05-05 10:23:46,910]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:46,910]  
[LINE:222]# INFO     [2020-05-05 10:23:46,910]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:46,910]  Se transmite fereastra 63 - 63
[LINE:224]# INFO     [2020-05-05 10:23:46,910]  Mai sunt 38 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:46,911]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:46,911]  Header segment 63 trimis: [seq_nr: 278986] , [check:  480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:47,913]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:47,913]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:47,915]  Idx segmente confirmate: [66]
[LINE:330]# INFO     [2020-05-05 10:23:47,915]  
[LINE:331]# INFO     [2020-05-05 10:23:47,916]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:47,916]  
[LINE:222]# INFO     [2020-05-05 10:23:47,916]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:47,916]  Se transmite fereastra 63 - 63
[LINE:224]# INFO     [2020-05-05 10:23:47,916]  Mai sunt 38 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:47,917]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:47,917]  Header segment 63 trimis: [seq_nr: 278986] , [check:  480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:48,919]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:48,920]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:48,921]  Idx segmente confirmate: [66]
[LINE:330]# INFO     [2020-05-05 10:23:48,921]  
[LINE:331]# INFO     [2020-05-05 10:23:48,921]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:48,921]  
[LINE:222]# INFO     [2020-05-05 10:23:48,921]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:48,921]  Se transmite fereastra 63 - 63
[LINE:224]# INFO     [2020-05-05 10:23:48,921]  Mai sunt 38 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:48,922]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:48,922]  Header segment 63 trimis: [seq_nr: 278986] , [check:  480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:49,924]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:49,924]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:49,925]  Idx segmente confirmate: [66]
[LINE:330]# INFO     [2020-05-05 10:23:49,925]  
[LINE:331]# INFO     [2020-05-05 10:23:49,925]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:49,925]  
[LINE:222]# INFO     [2020-05-05 10:23:49,926]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:49,926]  Se transmite fereastra 63 - 63
[LINE:224]# INFO     [2020-05-05 10:23:49,926]  Mai sunt 38 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:49,926]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:49,926]  Header segment 63 trimis: [seq_nr: 278986] , [check:  480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:50,928]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:50,929]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:50,930]  Idx segmente confirmate: [66]
[LINE:330]# INFO     [2020-05-05 10:23:50,930]  
[LINE:331]# INFO     [2020-05-05 10:23:50,930]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:50,930]  
[LINE:222]# INFO     [2020-05-05 10:23:50,930]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:50,930]  Se transmite fereastra 63 - 63
[LINE:224]# INFO     [2020-05-05 10:23:50,930]  Mai sunt 38 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:50,931]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:50,931]  Header segment 63 trimis: [seq_nr: 278986] , [check:  480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:51,932]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:51,932]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:51,933]  Idx segmente confirmate: [66]
[LINE:330]# INFO     [2020-05-05 10:23:51,933]  
[LINE:331]# INFO     [2020-05-05 10:23:51,934]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:51,934]  
[LINE:222]# INFO     [2020-05-05 10:23:51,934]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:51,934]  Se transmite fereastra 63 - 63
[LINE:224]# INFO     [2020-05-05 10:23:51,934]  Mai sunt 38 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:51,934]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:51,934]  Header segment 63 trimis: [seq_nr: 278986] , [check:  480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:52,937]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:52,937]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:52,938]  Idx segmente confirmate: [66]
[LINE:330]# INFO     [2020-05-05 10:23:52,938]  
[LINE:331]# INFO     [2020-05-05 10:23:52,939]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:52,939]  
[LINE:222]# INFO     [2020-05-05 10:23:52,939]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:52,939]  Se transmite fereastra 63 - 63
[LINE:224]# INFO     [2020-05-05 10:23:52,939]  Mai sunt 38 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:52,940]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:52,940]  Header segment 63 trimis: [seq_nr: 278986] , [check:  480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:53,942]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:53,942]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:53,944]  Idx segmente confirmate: [66]
[LINE:330]# INFO     [2020-05-05 10:23:53,944]  
[LINE:331]# INFO     [2020-05-05 10:23:53,944]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:53,944]  
[LINE:222]# INFO     [2020-05-05 10:23:53,944]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:53,945]  Se transmite fereastra 63 - 63
[LINE:224]# INFO     [2020-05-05 10:23:53,945]  Mai sunt 38 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:53,945]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:53,945]  Header segment 63 trimis: [seq_nr: 278986] , [check:  480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:54,947]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:54,948]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:54,950]  Idx segmente confirmate: [66]
[LINE:330]# INFO     [2020-05-05 10:23:54,951]  
[LINE:331]# INFO     [2020-05-05 10:23:54,951]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:54,951]  
[LINE:222]# INFO     [2020-05-05 10:23:54,951]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:54,951]  Se transmite fereastra 63 - 63
[LINE:224]# INFO     [2020-05-05 10:23:54,952]  Mai sunt 38 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:54,952]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:54,952]  Header segment 63 trimis: [seq_nr: 278986] , [check:  480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:55,953]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:55,953]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:55,955]  Idx segmente confirmate: [66]
[LINE:330]# INFO     [2020-05-05 10:23:55,955]  
[LINE:331]# INFO     [2020-05-05 10:23:55,955]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:55,955]  
[LINE:222]# INFO     [2020-05-05 10:23:55,955]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:55,955]  Se transmite fereastra 63 - 63
[LINE:224]# INFO     [2020-05-05 10:23:55,955]  Mai sunt 38 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:55,955]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:55,956]  Header segment 63 trimis: [seq_nr: 278986] , [check:  480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:56,958]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:56,958]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:56,961]  Idx segmente confirmate: [66]
[LINE:330]# INFO     [2020-05-05 10:23:56,961]  
[LINE:331]# INFO     [2020-05-05 10:23:56,961]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:56,961]  
[LINE:222]# INFO     [2020-05-05 10:23:56,961]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:56,962]  Se transmite fereastra 63 - 63
[LINE:224]# INFO     [2020-05-05 10:23:56,962]  Mai sunt 38 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:56,962]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:56,962]  Header segment 63 trimis: [seq_nr: 278986] , [check:  480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:57,965]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:57,965]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:57,966]  Idx segmente confirmate: [66]
[LINE:330]# INFO     [2020-05-05 10:23:57,966]  
[LINE:331]# INFO     [2020-05-05 10:23:57,966]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:57,967]  
[LINE:222]# INFO     [2020-05-05 10:23:57,967]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:57,967]  Se transmite fereastra 63 - 63
[LINE:224]# INFO     [2020-05-05 10:23:57,967]  Mai sunt 38 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:57,967]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:57,967]  Header segment 63 trimis: [seq_nr: 278986] , [check:  480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:58,968]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:58,969]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:23:58,971]  Idx segmente confirmate: [66]
[LINE:330]# INFO     [2020-05-05 10:23:58,971]  
[LINE:331]# INFO     [2020-05-05 10:23:58,972]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:58,972]  
[LINE:222]# INFO     [2020-05-05 10:23:58,972]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:58,973]  Se transmite fereastra 63 - 63
[LINE:224]# INFO     [2020-05-05 10:23:58,973]  Mai sunt 38 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:58,973]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:58,974]  Header segment 63 trimis: [seq_nr: 278986] , [check:  480] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:23:59,976]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:23:59,976]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:23:59,976]  Header receptor pt segment primit: [ack_nr: 280386] , [check:  14519] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:23:59,978]  Idx segmente confirmate: [63, 66]
[LINE:330]# INFO     [2020-05-05 10:23:59,978]  
[LINE:331]# INFO     [2020-05-05 10:23:59,978]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:23:59,978]  
[LINE:222]# INFO     [2020-05-05 10:23:59,978]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:23:59,978]  Se transmite fereastra 64 - 65
[LINE:224]# INFO     [2020-05-05 10:23:59,979]  Mai sunt 37 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:23:59,979]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:23:59,979]  Header segment 64 trimis: [seq_nr: 280386] , [check:  7212] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:23:59,979]  Header segment 65 trimis: [seq_nr: 281787] , [check:  2901] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:00,981]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:00,982]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:00,983]  Idx segmente confirmate: [66]
[LINE:330]# INFO     [2020-05-05 10:24:00,983]  
[LINE:331]# INFO     [2020-05-05 10:24:00,983]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:00,984]  
[LINE:222]# INFO     [2020-05-05 10:24:00,984]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:00,984]  Se transmite fereastra 64 - 65
[LINE:224]# INFO     [2020-05-05 10:24:00,984]  Mai sunt 37 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:00,984]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:00,984]  Header segment 64 trimis: [seq_nr: 280386] , [check:  7212] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:00,985]  Header segment 65 trimis: [seq_nr: 281787] , [check:  2901] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:01,985]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:01,985]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:24:01,986]  Header receptor pt segment primit: [ack_nr: 283187] , [check:  11718] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:24:01,987]  Idx segmente confirmate: [65, 66]
[LINE:330]# INFO     [2020-05-05 10:24:01,987]  
[LINE:331]# INFO     [2020-05-05 10:24:01,987]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:01,987]  
[LINE:222]# INFO     [2020-05-05 10:24:01,987]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:01,987]  Se transmite fereastra 64 - 65
[LINE:224]# INFO     [2020-05-05 10:24:01,987]  Mai sunt 37 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:01,987]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:01,988]  Header segment 64 trimis: [seq_nr: 280386] , [check:  7212] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:02,989]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:02,990]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:24:02,990]  Header receptor pt segment primit: [ack_nr: 281786] , [check:  13118] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:24:02,991]  Idx segmente confirmate: [64, 65, 66]
[LINE:330]# INFO     [2020-05-05 10:24:02,991]  
[LINE:331]# INFO     [2020-05-05 10:24:02,992]  Fereastra a avansat cu 3 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:02,992]  
[LINE:222]# INFO     [2020-05-05 10:24:02,992]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:02,992]  Se transmite fereastra 67 - 69
[LINE:224]# INFO     [2020-05-05 10:24:02,992]  Mai sunt 34 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:02,992]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:02,992]  Header segment 67 trimis: [seq_nr: 284586] , [check:  9936] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:02,993]  Header segment 68 trimis: [seq_nr: 285987] , [check:  1440] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:02,993]  Header segment 69 trimis: [seq_nr: 287388] , [check:  4962] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:03,996]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:03,996]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:03,997]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:24:03,997]  
[LINE:331]# INFO     [2020-05-05 10:24:03,997]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:03,997]  
[LINE:222]# INFO     [2020-05-05 10:24:03,997]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:03,997]  Se transmite fereastra 67 - 69
[LINE:224]# INFO     [2020-05-05 10:24:03,998]  Mai sunt 34 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:03,998]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:03,998]  Header segment 67 trimis: [seq_nr: 284586] , [check:  9936] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:03,998]  Header segment 68 trimis: [seq_nr: 285987] , [check:  1440] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:03,999]  Header segment 69 trimis: [seq_nr: 287388] , [check:  4962] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:05,000]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:05,001]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:05,002]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:24:05,002]  
[LINE:331]# INFO     [2020-05-05 10:24:05,002]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:05,002]  
[LINE:222]# INFO     [2020-05-05 10:24:05,002]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:05,003]  Se transmite fereastra 67 - 69
[LINE:224]# INFO     [2020-05-05 10:24:05,003]  Mai sunt 34 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:05,003]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:05,003]  Header segment 67 trimis: [seq_nr: 284586] , [check:  9936] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:05,004]  Header segment 68 trimis: [seq_nr: 285987] , [check:  1440] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:05,004]  Header segment 69 trimis: [seq_nr: 287388] , [check:  4962] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:06,006]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:06,006]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:06,008]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:24:06,008]  
[LINE:331]# INFO     [2020-05-05 10:24:06,008]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:06,008]  
[LINE:222]# INFO     [2020-05-05 10:24:06,008]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:06,008]  Se transmite fereastra 67 - 69
[LINE:224]# INFO     [2020-05-05 10:24:06,009]  Mai sunt 34 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:06,009]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:06,009]  Header segment 67 trimis: [seq_nr: 284586] , [check:  9936] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:06,009]  Header segment 68 trimis: [seq_nr: 285987] , [check:  1440] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:06,010]  Header segment 69 trimis: [seq_nr: 287388] , [check:  4962] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:07,011]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:07,012]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:07,014]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:24:07,014]  
[LINE:331]# INFO     [2020-05-05 10:24:07,014]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:07,015]  
[LINE:222]# INFO     [2020-05-05 10:24:07,015]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:07,015]  Se transmite fereastra 67 - 69
[LINE:224]# INFO     [2020-05-05 10:24:07,015]  Mai sunt 34 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:07,015]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:07,016]  Header segment 67 trimis: [seq_nr: 284586] , [check:  9936] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:07,016]  Header segment 68 trimis: [seq_nr: 285987] , [check:  1440] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:07,017]  Header segment 69 trimis: [seq_nr: 287388] , [check:  4962] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:08,019]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:08,019]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:24:08,020]  Header receptor pt segment primit: [ack_nr: 287387] , [check:  7518] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:24:08,022]  Idx segmente confirmate: [68]
[LINE:330]# INFO     [2020-05-05 10:24:08,022]  
[LINE:331]# INFO     [2020-05-05 10:24:08,022]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:08,022]  
[LINE:222]# INFO     [2020-05-05 10:24:08,023]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:08,023]  Se transmite fereastra 67 - 68
[LINE:224]# INFO     [2020-05-05 10:24:08,023]  Mai sunt 34 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:08,023]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:08,023]  Header segment 67 trimis: [seq_nr: 284586] , [check:  9936] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:09,026]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:09,026]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:09,029]  Idx segmente confirmate: [68]
[LINE:330]# INFO     [2020-05-05 10:24:09,029]  
[LINE:331]# INFO     [2020-05-05 10:24:09,029]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:09,029]  
[LINE:222]# INFO     [2020-05-05 10:24:09,030]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:09,030]  Se transmite fereastra 67 - 68
[LINE:224]# INFO     [2020-05-05 10:24:09,030]  Mai sunt 34 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:09,030]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:09,031]  Header segment 67 trimis: [seq_nr: 284586] , [check:  9936] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:10,033]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:10,033]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:10,034]  Idx segmente confirmate: [68]
[LINE:330]# INFO     [2020-05-05 10:24:10,035]  
[LINE:331]# INFO     [2020-05-05 10:24:10,035]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:10,035]  
[LINE:222]# INFO     [2020-05-05 10:24:10,035]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:10,035]  Se transmite fereastra 67 - 68
[LINE:224]# INFO     [2020-05-05 10:24:10,035]  Mai sunt 34 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:10,036]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:10,036]  Header segment 67 trimis: [seq_nr: 284586] , [check:  9936] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:11,037]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:11,037]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:11,039]  Idx segmente confirmate: [68]
[LINE:330]# INFO     [2020-05-05 10:24:11,039]  
[LINE:331]# INFO     [2020-05-05 10:24:11,039]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:11,039]  
[LINE:222]# INFO     [2020-05-05 10:24:11,039]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:11,039]  Se transmite fereastra 67 - 68
[LINE:224]# INFO     [2020-05-05 10:24:11,039]  Mai sunt 34 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:11,039]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:11,040]  Header segment 67 trimis: [seq_nr: 284586] , [check:  9936] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:12,041]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:12,042]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:24:12,042]  Header receptor pt segment primit: [ack_nr: 285986] , [check:  8920] , [window: 1]
[LINE:290]# INFO     [2020-05-05 10:24:12,044]  Idx segmente confirmate: [67, 68]
[LINE:330]# INFO     [2020-05-05 10:24:12,045]  
[LINE:331]# INFO     [2020-05-05 10:24:12,045]  Fereastra a avansat cu 2 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:12,045]  
[LINE:222]# INFO     [2020-05-05 10:24:12,045]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:12,046]  Se transmite fereastra 69 - 69
[LINE:224]# INFO     [2020-05-05 10:24:12,046]  Mai sunt 32 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:12,046]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:12,046]  Header segment 69 trimis: [seq_nr: 287386] , [check:  4964] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:13,049]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:13,049]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:13,051]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:24:13,051]  
[LINE:331]# INFO     [2020-05-05 10:24:13,051]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:13,051]  
[LINE:222]# INFO     [2020-05-05 10:24:13,051]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:13,051]  Se transmite fereastra 69 - 69
[LINE:224]# INFO     [2020-05-05 10:24:13,051]  Mai sunt 32 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:13,051]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:13,052]  Header segment 69 trimis: [seq_nr: 287386] , [check:  4964] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:14,053]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:14,054]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:24:14,054]  Header receptor pt segment primit: [ack_nr: 288786] , [check:  6117] , [window: 4]
[LINE:290]# INFO     [2020-05-05 10:24:14,055]  Idx segmente confirmate: [69]
[LINE:330]# INFO     [2020-05-05 10:24:14,055]  
[LINE:331]# INFO     [2020-05-05 10:24:14,055]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:14,056]  
[LINE:222]# INFO     [2020-05-05 10:24:14,056]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:14,056]  Se transmite fereastra 70 - 73
[LINE:224]# INFO     [2020-05-05 10:24:14,056]  Mai sunt 31 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:14,056]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:14,057]  Header segment 70 trimis: [seq_nr: 288786] , [check:  5884] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:14,057]  Header segment 71 trimis: [seq_nr: 290187] , [check:  4204] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:14,058]  Header segment 72 trimis: [seq_nr: 291588] , [check:  14489] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:14,058]  Header segment 73 trimis: [seq_nr: 292989] , [check:  13737] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:15,059]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:15,060]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:24:15,060]  Header receptor pt segment primit: [ack_nr: 291587] , [check:  3317] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:24:15,061]  Idx segmente confirmate: [71]
[LINE:330]# INFO     [2020-05-05 10:24:15,061]  
[LINE:331]# INFO     [2020-05-05 10:24:15,061]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:15,062]  
[LINE:222]# INFO     [2020-05-05 10:24:15,062]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:15,062]  Se transmite fereastra 70 - 72
[LINE:224]# INFO     [2020-05-05 10:24:15,062]  Mai sunt 31 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:15,062]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:15,063]  Header segment 70 trimis: [seq_nr: 288786] , [check:  5884] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:15,063]  Header segment 72 trimis: [seq_nr: 291587] , [check:  14490] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:16,064]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:16,065]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:24:16,065]  Header receptor pt segment primit: [ack_nr: 292987] , [check:  1915] , [window: 5]
[LINE:290]# INFO     [2020-05-05 10:24:16,066]  Idx segmente confirmate: [71, 72]
[LINE:330]# INFO     [2020-05-05 10:24:16,066]  
[LINE:331]# INFO     [2020-05-05 10:24:16,066]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:16,067]  
[LINE:222]# INFO     [2020-05-05 10:24:16,067]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:16,067]  Se transmite fereastra 70 - 74
[LINE:224]# INFO     [2020-05-05 10:24:16,067]  Mai sunt 31 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:16,067]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:16,067]  Header segment 70 trimis: [seq_nr: 288786] , [check:  5884] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:16,071]  Header segment 73 trimis: [seq_nr: 292987] , [check:  13739] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:16,072]  Header segment 74 trimis: [seq_nr: 294388] , [check:  19001] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:17,072]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:17,072]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:17,073]  Idx segmente confirmate: [71, 72]
[LINE:330]# INFO     [2020-05-05 10:24:17,074]  
[LINE:331]# INFO     [2020-05-05 10:24:17,074]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:17,074]  
[LINE:222]# INFO     [2020-05-05 10:24:17,074]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:17,074]  Se transmite fereastra 70 - 74
[LINE:224]# INFO     [2020-05-05 10:24:17,074]  Mai sunt 31 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:17,074]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:17,074]  Header segment 70 trimis: [seq_nr: 288786] , [check:  5884] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:17,075]  Header segment 73 trimis: [seq_nr: 292987] , [check:  13739] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:17,075]  Header segment 74 trimis: [seq_nr: 294388] , [check:  19001] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:18,077]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:18,077]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:24:18,078]  Header receptor pt segment primit: [ack_nr: 290186] , [check:  4718] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:24:18,080]  Idx segmente confirmate: [70, 71, 72]
[LINE:330]# INFO     [2020-05-05 10:24:18,081]  
[LINE:331]# INFO     [2020-05-05 10:24:18,081]  Fereastra a avansat cu 3 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:18,081]  
[LINE:222]# INFO     [2020-05-05 10:24:18,081]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:18,081]  Se transmite fereastra 73 - 75
[LINE:224]# INFO     [2020-05-05 10:24:18,082]  Mai sunt 28 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:18,082]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:18,082]  Header segment 73 trimis: [seq_nr: 292986] , [check:  13740] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:18,083]  Header segment 74 trimis: [seq_nr: 294387] , [check:  19002] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:18,085]  Header segment 75 trimis: [seq_nr: 295788] , [check:  2916] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:19,087]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:19,088]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:24:19,088]  Header receptor pt segment primit: [ack_nr: 295787] , [check:  31883] , [window: 5]
[LINE:290]# INFO     [2020-05-05 10:24:19,089]  Idx segmente confirmate: [74]
[LINE:330]# INFO     [2020-05-05 10:24:19,089]  
[LINE:331]# INFO     [2020-05-05 10:24:19,089]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:19,089]  
[LINE:222]# INFO     [2020-05-05 10:24:19,090]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:19,090]  Se transmite fereastra 73 - 77
[LINE:224]# INFO     [2020-05-05 10:24:19,090]  Mai sunt 28 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:19,090]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:19,090]  Header segment 73 trimis: [seq_nr: 292986] , [check:  13740] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:19,091]  Header segment 75 trimis: [seq_nr: 295787] , [check:  2917] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:19,091]  Header segment 76 trimis: [seq_nr: 297188] , [check:  1482] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:19,091]  Header segment 77 trimis: [seq_nr: 298589] , [check:  11175] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:20,092]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:20,092]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:20,093]  Idx segmente confirmate: [74]
[LINE:330]# INFO     [2020-05-05 10:24:20,093]  
[LINE:331]# INFO     [2020-05-05 10:24:20,094]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:20,094]  
[LINE:222]# INFO     [2020-05-05 10:24:20,094]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:20,094]  Se transmite fereastra 73 - 77
[LINE:224]# INFO     [2020-05-05 10:24:20,094]  Mai sunt 28 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:20,094]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:20,095]  Header segment 73 trimis: [seq_nr: 292986] , [check:  13740] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:20,095]  Header segment 75 trimis: [seq_nr: 295787] , [check:  2917] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:20,096]  Header segment 76 trimis: [seq_nr: 297188] , [check:  1482] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:20,096]  Header segment 77 trimis: [seq_nr: 298589] , [check:  11175] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:21,098]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:21,099]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:24:21,099]  Header receptor pt segment primit: [ack_nr: 294386] , [check:  517] , [window: 4]
[LINE:290]# INFO     [2020-05-05 10:24:21,100]  Idx segmente confirmate: [73, 74]
[LINE:330]# INFO     [2020-05-05 10:24:21,100]  
[LINE:331]# INFO     [2020-05-05 10:24:21,100]  Fereastra a avansat cu 2 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:21,100]  
[LINE:222]# INFO     [2020-05-05 10:24:21,101]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:21,101]  Se transmite fereastra 75 - 78
[LINE:224]# INFO     [2020-05-05 10:24:21,101]  Mai sunt 26 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:21,101]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:21,101]  Header segment 75 trimis: [seq_nr: 295786] , [check:  2918] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:21,102]  Header segment 76 trimis: [seq_nr: 297187] , [check:  1483] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:21,102]  Header segment 77 trimis: [seq_nr: 298588] , [check:  11176] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:21,102]  Header segment 78 trimis: [seq_nr: 299989] , [check:  31322] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:22,104]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:22,105]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:24:22,105]  Header receptor pt segment primit: [ack_nr: 301389] , [check:  26282] , [window: 4]
[LINE:290]# INFO     [2020-05-05 10:24:22,106]  Idx segmente confirmate: [78]
[LINE:330]# INFO     [2020-05-05 10:24:22,107]  
[LINE:331]# INFO     [2020-05-05 10:24:22,107]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:22,107]  
[LINE:222]# INFO     [2020-05-05 10:24:22,107]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:22,107]  Se transmite fereastra 75 - 78
[LINE:224]# INFO     [2020-05-05 10:24:22,107]  Mai sunt 26 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:22,107]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:22,108]  Header segment 75 trimis: [seq_nr: 295786] , [check:  2918] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:22,108]  Header segment 76 trimis: [seq_nr: 297187] , [check:  1483] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:22,108]  Header segment 77 trimis: [seq_nr: 298588] , [check:  11176] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:23,110]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:23,111]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:23,112]  Idx segmente confirmate: [78]
[LINE:330]# INFO     [2020-05-05 10:24:23,112]  
[LINE:331]# INFO     [2020-05-05 10:24:23,112]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:23,112]  
[LINE:222]# INFO     [2020-05-05 10:24:23,112]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:23,113]  Se transmite fereastra 75 - 78
[LINE:224]# INFO     [2020-05-05 10:24:23,113]  Mai sunt 26 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:23,113]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:23,113]  Header segment 75 trimis: [seq_nr: 295786] , [check:  2918] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:23,114]  Header segment 76 trimis: [seq_nr: 297187] , [check:  1483] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:23,114]  Header segment 77 trimis: [seq_nr: 298588] , [check:  11176] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:24,115]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:24,116]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:24,118]  Idx segmente confirmate: [78]
[LINE:330]# INFO     [2020-05-05 10:24:24,118]  
[LINE:331]# INFO     [2020-05-05 10:24:24,119]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:24,119]  
[LINE:222]# INFO     [2020-05-05 10:24:24,119]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:24,119]  Se transmite fereastra 75 - 78
[LINE:224]# INFO     [2020-05-05 10:24:24,120]  Mai sunt 26 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:24,120]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:24,120]  Header segment 75 trimis: [seq_nr: 295786] , [check:  2918] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:24,121]  Header segment 76 trimis: [seq_nr: 297187] , [check:  1483] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:24,121]  Header segment 77 trimis: [seq_nr: 298588] , [check:  11176] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:25,123]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:25,124]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:25,125]  Idx segmente confirmate: [78]
[LINE:330]# INFO     [2020-05-05 10:24:25,125]  
[LINE:331]# INFO     [2020-05-05 10:24:25,125]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:25,125]  
[LINE:222]# INFO     [2020-05-05 10:24:25,125]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:25,125]  Se transmite fereastra 75 - 78
[LINE:224]# INFO     [2020-05-05 10:24:25,126]  Mai sunt 26 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:25,126]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:25,126]  Header segment 75 trimis: [seq_nr: 295786] , [check:  2918] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:25,126]  Header segment 76 trimis: [seq_nr: 297187] , [check:  1483] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:25,127]  Header segment 77 trimis: [seq_nr: 298588] , [check:  11176] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:26,128]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:26,129]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:24:26,129]  Header receptor pt segment primit: [ack_nr: 297186] , [check:  30484] , [window: 5]
[LINE:290]# INFO     [2020-05-05 10:24:26,131]  Idx segmente confirmate: [75, 78]
[LINE:330]# INFO     [2020-05-05 10:24:26,131]  
[LINE:331]# INFO     [2020-05-05 10:24:26,132]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:26,132]  
[LINE:222]# INFO     [2020-05-05 10:24:26,132]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:26,132]  Se transmite fereastra 76 - 80
[LINE:224]# INFO     [2020-05-05 10:24:26,132]  Mai sunt 25 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:26,132]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:26,133]  Header segment 76 trimis: [seq_nr: 297186] , [check:  1484] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:26,133]  Header segment 77 trimis: [seq_nr: 298587] , [check:  11177] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:26,134]  Header segment 79 trimis: [seq_nr: 301388] , [check:  2150] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:26,134]  Header segment 80 trimis: [seq_nr: 302789] , [check:  11017] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:27,136]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:27,136]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:27,137]  Idx segmente confirmate: [78]
[LINE:330]# INFO     [2020-05-05 10:24:27,138]  
[LINE:331]# INFO     [2020-05-05 10:24:27,138]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:27,138]  
[LINE:222]# INFO     [2020-05-05 10:24:27,138]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:27,138]  Se transmite fereastra 76 - 80
[LINE:224]# INFO     [2020-05-05 10:24:27,138]  Mai sunt 25 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:27,138]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:27,139]  Header segment 76 trimis: [seq_nr: 297186] , [check:  1484] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:27,139]  Header segment 77 trimis: [seq_nr: 298587] , [check:  11177] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:27,139]  Header segment 79 trimis: [seq_nr: 301388] , [check:  2150] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:27,140]  Header segment 80 trimis: [seq_nr: 302789] , [check:  11017] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:28,142]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:28,142]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:28,143]  Idx segmente confirmate: [78]
[LINE:330]# INFO     [2020-05-05 10:24:28,144]  
[LINE:331]# INFO     [2020-05-05 10:24:28,144]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:28,144]  
[LINE:222]# INFO     [2020-05-05 10:24:28,144]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:28,144]  Se transmite fereastra 76 - 80
[LINE:224]# INFO     [2020-05-05 10:24:28,144]  Mai sunt 25 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:28,144]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:28,145]  Header segment 76 trimis: [seq_nr: 297186] , [check:  1484] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:28,145]  Header segment 77 trimis: [seq_nr: 298587] , [check:  11177] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:28,145]  Header segment 79 trimis: [seq_nr: 301388] , [check:  2150] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:28,146]  Header segment 80 trimis: [seq_nr: 302789] , [check:  11017] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:29,147]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:29,148]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:29,149]  Idx segmente confirmate: [78]
[LINE:330]# INFO     [2020-05-05 10:24:29,149]  
[LINE:331]# INFO     [2020-05-05 10:24:29,149]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:29,149]  
[LINE:222]# INFO     [2020-05-05 10:24:29,149]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:29,150]  Se transmite fereastra 76 - 80
[LINE:224]# INFO     [2020-05-05 10:24:29,150]  Mai sunt 25 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:29,150]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:29,150]  Header segment 76 trimis: [seq_nr: 297186] , [check:  1484] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:29,150]  Header segment 77 trimis: [seq_nr: 298587] , [check:  11177] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:29,151]  Header segment 79 trimis: [seq_nr: 301388] , [check:  2150] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:29,151]  Header segment 80 trimis: [seq_nr: 302789] , [check:  11017] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:30,153]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:30,153]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:30,156]  Idx segmente confirmate: [78]
[LINE:330]# INFO     [2020-05-05 10:24:30,156]  
[LINE:331]# INFO     [2020-05-05 10:24:30,156]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:30,157]  
[LINE:222]# INFO     [2020-05-05 10:24:30,157]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:30,157]  Se transmite fereastra 76 - 80
[LINE:224]# INFO     [2020-05-05 10:24:30,158]  Mai sunt 25 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:30,158]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:30,159]  Header segment 76 trimis: [seq_nr: 297186] , [check:  1484] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:30,160]  Header segment 77 trimis: [seq_nr: 298587] , [check:  11177] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:30,162]  Header segment 79 trimis: [seq_nr: 301388] , [check:  2150] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:30,163]  Header segment 80 trimis: [seq_nr: 302789] , [check:  11017] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:31,165]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:31,165]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:31,166]  Idx segmente confirmate: [78]
[LINE:330]# INFO     [2020-05-05 10:24:31,167]  
[LINE:331]# INFO     [2020-05-05 10:24:31,167]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:31,167]  
[LINE:222]# INFO     [2020-05-05 10:24:31,167]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:31,167]  Se transmite fereastra 76 - 80
[LINE:224]# INFO     [2020-05-05 10:24:31,167]  Mai sunt 25 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:31,167]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:31,168]  Header segment 76 trimis: [seq_nr: 297186] , [check:  1484] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:31,168]  Header segment 77 trimis: [seq_nr: 298587] , [check:  11177] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:31,169]  Header segment 79 trimis: [seq_nr: 301388] , [check:  2150] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:31,169]  Header segment 80 trimis: [seq_nr: 302789] , [check:  11017] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:32,170]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:32,170]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:24:32,170]  Header receptor pt segment primit: [ack_nr: 298586] , [check:  29087] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:24:32,171]  Idx segmente confirmate: [76, 78]
[LINE:330]# INFO     [2020-05-05 10:24:32,172]  
[LINE:331]# INFO     [2020-05-05 10:24:32,172]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:32,172]  
[LINE:222]# INFO     [2020-05-05 10:24:32,172]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:32,172]  Se transmite fereastra 77 - 78
[LINE:224]# INFO     [2020-05-05 10:24:32,172]  Mai sunt 24 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:32,172]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:32,172]  Header segment 77 trimis: [seq_nr: 298586] , [check:  11178] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:33,174]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:33,175]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:33,177]  Idx segmente confirmate: [78]
[LINE:330]# INFO     [2020-05-05 10:24:33,178]  
[LINE:331]# INFO     [2020-05-05 10:24:33,178]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:33,178]  
[LINE:222]# INFO     [2020-05-05 10:24:33,178]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:33,178]  Se transmite fereastra 77 - 78
[LINE:224]# INFO     [2020-05-05 10:24:33,178]  Mai sunt 24 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:33,179]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:33,179]  Header segment 77 trimis: [seq_nr: 298586] , [check:  11178] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:34,181]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:34,182]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:24:34,182]  Header receptor pt segment primit: [ack_nr: 299986] , [check:  27687] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:24:34,183]  Idx segmente confirmate: [77, 78]
[LINE:330]# INFO     [2020-05-05 10:24:34,184]  
[LINE:331]# INFO     [2020-05-05 10:24:34,184]  Fereastra a avansat cu 2 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:34,184]  
[LINE:222]# INFO     [2020-05-05 10:24:34,184]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:34,184]  Se transmite fereastra 79 - 80
[LINE:224]# INFO     [2020-05-05 10:24:34,184]  Mai sunt 22 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:34,184]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:34,185]  Header segment 79 trimis: [seq_nr: 301386] , [check:  2152] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:34,185]  Header segment 80 trimis: [seq_nr: 302787] , [check:  11019] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:35,187]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:35,187]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:35,189]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:24:35,189]  
[LINE:331]# INFO     [2020-05-05 10:24:35,189]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:35,189]  
[LINE:222]# INFO     [2020-05-05 10:24:35,190]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:35,190]  Se transmite fereastra 79 - 80
[LINE:224]# INFO     [2020-05-05 10:24:35,190]  Mai sunt 22 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:35,190]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:35,191]  Header segment 79 trimis: [seq_nr: 301386] , [check:  2152] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:35,191]  Header segment 80 trimis: [seq_nr: 302787] , [check:  11019] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:36,193]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:36,194]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:36,197]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:24:36,197]  
[LINE:331]# INFO     [2020-05-05 10:24:36,197]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:36,198]  
[LINE:222]# INFO     [2020-05-05 10:24:36,198]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:36,198]  Se transmite fereastra 79 - 80
[LINE:224]# INFO     [2020-05-05 10:24:36,198]  Mai sunt 22 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:36,199]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:36,199]  Header segment 79 trimis: [seq_nr: 301386] , [check:  2152] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:36,200]  Header segment 80 trimis: [seq_nr: 302787] , [check:  11019] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:37,202]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:37,203]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:37,204]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:24:37,205]  
[LINE:331]# INFO     [2020-05-05 10:24:37,205]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:37,205]  
[LINE:222]# INFO     [2020-05-05 10:24:37,205]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:37,205]  Se transmite fereastra 79 - 80
[LINE:224]# INFO     [2020-05-05 10:24:37,205]  Mai sunt 22 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:37,205]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:37,206]  Header segment 79 trimis: [seq_nr: 301386] , [check:  2152] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:37,206]  Header segment 80 trimis: [seq_nr: 302787] , [check:  11019] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:38,208]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:38,208]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:24:38,208]  Header receptor pt segment primit: [ack_nr: 304187] , [check:  23484] , [window: 4]
[LINE:290]# INFO     [2020-05-05 10:24:38,210]  Idx segmente confirmate: [80]
[LINE:330]# INFO     [2020-05-05 10:24:38,210]  
[LINE:331]# INFO     [2020-05-05 10:24:38,210]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:38,211]  
[LINE:222]# INFO     [2020-05-05 10:24:38,211]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:38,211]  Se transmite fereastra 79 - 82
[LINE:224]# INFO     [2020-05-05 10:24:38,211]  Mai sunt 22 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:38,211]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:38,212]  Header segment 79 trimis: [seq_nr: 301386] , [check:  2152] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:38,212]  Header segment 81 trimis: [seq_nr: 304187] , [check:  5983] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:38,212]  Header segment 82 trimis: [seq_nr: 305588] , [check:  11321] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:39,214]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:39,214]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:24:39,215]  Header receptor pt segment primit: [ack_nr: 306988] , [check:  20686] , [window: 1]
[LINE:290]# INFO     [2020-05-05 10:24:39,218]  Idx segmente confirmate: [80, 82]
[LINE:330]# INFO     [2020-05-05 10:24:39,218]  
[LINE:331]# INFO     [2020-05-05 10:24:39,218]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:39,218]  
[LINE:222]# INFO     [2020-05-05 10:24:39,219]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:39,219]  Se transmite fereastra 79 - 79
[LINE:224]# INFO     [2020-05-05 10:24:39,219]  Mai sunt 22 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:39,220]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:39,220]  Header segment 79 trimis: [seq_nr: 301386] , [check:  2152] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:40,222]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:40,223]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:40,224]  Idx segmente confirmate: [80, 82]
[LINE:330]# INFO     [2020-05-05 10:24:40,224]  
[LINE:331]# INFO     [2020-05-05 10:24:40,224]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:40,225]  
[LINE:222]# INFO     [2020-05-05 10:24:40,225]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:40,225]  Se transmite fereastra 79 - 79
[LINE:224]# INFO     [2020-05-05 10:24:40,225]  Mai sunt 22 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:40,225]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:40,225]  Header segment 79 trimis: [seq_nr: 301386] , [check:  2152] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:41,230]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:41,230]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:24:41,230]  Header receptor pt segment primit: [ack_nr: 302786] , [check:  24885] , [window: 4]
[LINE:290]# INFO     [2020-05-05 10:24:41,233]  Idx segmente confirmate: [79, 80, 82]
[LINE:330]# INFO     [2020-05-05 10:24:41,233]  
[LINE:331]# INFO     [2020-05-05 10:24:41,233]  Fereastra a avansat cu 2 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:41,233]  
[LINE:222]# INFO     [2020-05-05 10:24:41,234]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:41,234]  Se transmite fereastra 81 - 84
[LINE:224]# INFO     [2020-05-05 10:24:41,234]  Mai sunt 20 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:41,234]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:41,235]  Header segment 81 trimis: [seq_nr: 304186] , [check:  5984] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:41,236]  Header segment 83 trimis: [seq_nr: 306987] , [check:  36] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:41,237]  Header segment 84 trimis: [seq_nr: 308388] , [check:  23109] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:42,237]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:42,238]  Confirmari preluate = 3
[LINE:270]# INFO     [2020-05-05 10:24:42,238]  Header receptor pt segment primit: [ack_nr: 305586] , [check:  22086] , [window: 3]
[LINE:270]# INFO     [2020-05-05 10:24:42,238]  Header receptor pt segment primit: [ack_nr: 308387] , [check:  19285] , [window: 3]
[LINE:270]# INFO     [2020-05-05 10:24:42,238]  Header receptor pt segment primit: [ack_nr: 309788] , [check:  17884] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:24:42,240]  Idx segmente confirmate: [81, 82, 83, 84]
[LINE:330]# INFO     [2020-05-05 10:24:42,240]  
[LINE:331]# INFO     [2020-05-05 10:24:42,240]  Fereastra a avansat cu 4 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:42,240]  
[LINE:222]# INFO     [2020-05-05 10:24:42,240]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:42,240]  Se transmite fereastra 85 - 87
[LINE:224]# INFO     [2020-05-05 10:24:42,240]  Mai sunt 16 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:42,241]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:42,241]  Header segment 85 trimis: [seq_nr: 309786] , [check:  11435] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:42,241]  Header segment 86 trimis: [seq_nr: 311187] , [check:  1109] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:42,241]  Header segment 87 trimis: [seq_nr: 312588] , [check:  6121] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:43,244]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:43,244]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:43,247]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:24:43,247]  
[LINE:331]# INFO     [2020-05-05 10:24:43,247]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:43,248]  
[LINE:222]# INFO     [2020-05-05 10:24:43,248]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:43,248]  Se transmite fereastra 85 - 87
[LINE:224]# INFO     [2020-05-05 10:24:43,248]  Mai sunt 16 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:43,248]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:43,249]  Header segment 85 trimis: [seq_nr: 309786] , [check:  11435] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:43,249]  Header segment 86 trimis: [seq_nr: 311187] , [check:  1109] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:43,250]  Header segment 87 trimis: [seq_nr: 312588] , [check:  6121] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:44,252]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:44,252]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:44,254]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:24:44,254]  
[LINE:331]# INFO     [2020-05-05 10:24:44,254]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:44,254]  
[LINE:222]# INFO     [2020-05-05 10:24:44,254]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:44,255]  Se transmite fereastra 85 - 87
[LINE:224]# INFO     [2020-05-05 10:24:44,255]  Mai sunt 16 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:44,255]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:44,255]  Header segment 85 trimis: [seq_nr: 309786] , [check:  11435] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:44,256]  Header segment 86 trimis: [seq_nr: 311187] , [check:  1109] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:44,256]  Header segment 87 trimis: [seq_nr: 312588] , [check:  6121] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:45,257]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:45,258]  Confirmari preluate = 2
[LINE:270]# INFO     [2020-05-05 10:24:45,258]  Header receptor pt segment primit: [ack_nr: 313988] , [check:  13686] , [window: 1]
[LINE:270]# INFO     [2020-05-05 10:24:45,258]  Header receptor pt segment primit: [ack_nr: 311186] , [check:  16488] , [window: 1]
[LINE:290]# INFO     [2020-05-05 10:24:45,260]  Idx segmente confirmate: [85, 87]
[LINE:330]# INFO     [2020-05-05 10:24:45,260]  
[LINE:331]# INFO     [2020-05-05 10:24:45,260]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:45,260]  
[LINE:222]# INFO     [2020-05-05 10:24:45,260]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:45,260]  Se transmite fereastra 86 - 86
[LINE:224]# INFO     [2020-05-05 10:24:45,260]  Mai sunt 15 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:45,260]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:45,261]  Header segment 86 trimis: [seq_nr: 311186] , [check:  1110] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:46,263]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:46,263]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:46,264]  Idx segmente confirmate: [87]
[LINE:330]# INFO     [2020-05-05 10:24:46,264]  
[LINE:331]# INFO     [2020-05-05 10:24:46,265]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:46,265]  
[LINE:222]# INFO     [2020-05-05 10:24:46,265]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:46,265]  Se transmite fereastra 86 - 86
[LINE:224]# INFO     [2020-05-05 10:24:46,265]  Mai sunt 15 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:46,265]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:46,265]  Header segment 86 trimis: [seq_nr: 311186] , [check:  1110] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:47,267]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:47,268]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:47,269]  Idx segmente confirmate: [87]
[LINE:330]# INFO     [2020-05-05 10:24:47,269]  
[LINE:331]# INFO     [2020-05-05 10:24:47,270]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:47,270]  
[LINE:222]# INFO     [2020-05-05 10:24:47,270]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:47,270]  Se transmite fereastra 86 - 86
[LINE:224]# INFO     [2020-05-05 10:24:47,270]  Mai sunt 15 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:47,270]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:47,270]  Header segment 86 trimis: [seq_nr: 311186] , [check:  1110] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:48,273]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:48,273]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:48,276]  Idx segmente confirmate: [87]
[LINE:330]# INFO     [2020-05-05 10:24:48,276]  
[LINE:331]# INFO     [2020-05-05 10:24:48,276]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:48,276]  
[LINE:222]# INFO     [2020-05-05 10:24:48,276]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:48,277]  Se transmite fereastra 86 - 86
[LINE:224]# INFO     [2020-05-05 10:24:48,277]  Mai sunt 15 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:48,277]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:48,277]  Header segment 86 trimis: [seq_nr: 311186] , [check:  1110] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:49,279]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:49,280]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:49,282]  Idx segmente confirmate: [87]
[LINE:330]# INFO     [2020-05-05 10:24:49,282]  
[LINE:331]# INFO     [2020-05-05 10:24:49,283]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:49,283]  
[LINE:222]# INFO     [2020-05-05 10:24:49,283]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:49,283]  Se transmite fereastra 86 - 86
[LINE:224]# INFO     [2020-05-05 10:24:49,283]  Mai sunt 15 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:49,284]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:49,284]  Header segment 86 trimis: [seq_nr: 311186] , [check:  1110] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:50,286]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:50,286]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:50,288]  Idx segmente confirmate: [87]
[LINE:330]# INFO     [2020-05-05 10:24:50,288]  
[LINE:331]# INFO     [2020-05-05 10:24:50,288]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:50,288]  
[LINE:222]# INFO     [2020-05-05 10:24:50,288]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:50,288]  Se transmite fereastra 86 - 86
[LINE:224]# INFO     [2020-05-05 10:24:50,288]  Mai sunt 15 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:50,288]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:50,289]  Header segment 86 trimis: [seq_nr: 311186] , [check:  1110] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:51,290]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:51,291]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:24:51,291]  Header receptor pt segment primit: [ack_nr: 312586] , [check:  15086] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:24:51,292]  Idx segmente confirmate: [86, 87]
[LINE:330]# INFO     [2020-05-05 10:24:51,293]  
[LINE:331]# INFO     [2020-05-05 10:24:51,293]  Fereastra a avansat cu 2 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:51,293]  
[LINE:222]# INFO     [2020-05-05 10:24:51,293]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:51,293]  Se transmite fereastra 88 - 90
[LINE:224]# INFO     [2020-05-05 10:24:51,293]  Mai sunt 13 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:51,293]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:51,294]  Header segment 88 trimis: [seq_nr: 313986] , [check:  9377] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:51,294]  Header segment 89 trimis: [seq_nr: 315387] , [check:  17824] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:51,294]  Header segment 90 trimis: [seq_nr: 316788] , [check:  932] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:52,296]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:52,297]  Confirmari preluate = 2
[LINE:270]# INFO     [2020-05-05 10:24:52,297]  Header receptor pt segment primit: [ack_nr: 316787] , [check:  10884] , [window: 4]
[LINE:270]# INFO     [2020-05-05 10:24:52,297]  Header receptor pt segment primit: [ack_nr: 318188] , [check:  9483] , [window: 4]
[LINE:290]# INFO     [2020-05-05 10:24:52,300]  Idx segmente confirmate: [89, 90]
[LINE:330]# INFO     [2020-05-05 10:24:52,300]  
[LINE:331]# INFO     [2020-05-05 10:24:52,301]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:52,301]  
[LINE:222]# INFO     [2020-05-05 10:24:52,301]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:52,302]  Se transmite fereastra 88 - 91
[LINE:224]# INFO     [2020-05-05 10:24:52,302]  Mai sunt 13 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:52,302]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:52,303]  Header segment 88 trimis: [seq_nr: 313986] , [check:  9377] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:52,304]  Header segment 91 trimis: [seq_nr: 318187] , [check:  26517] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:53,306]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:53,307]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:53,308]  Idx segmente confirmate: [89, 90]
[LINE:330]# INFO     [2020-05-05 10:24:53,309]  
[LINE:331]# INFO     [2020-05-05 10:24:53,309]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:53,309]  
[LINE:222]# INFO     [2020-05-05 10:24:53,309]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:53,309]  Se transmite fereastra 88 - 91
[LINE:224]# INFO     [2020-05-05 10:24:53,309]  Mai sunt 13 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:53,309]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:53,310]  Header segment 88 trimis: [seq_nr: 313986] , [check:  9377] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:53,310]  Header segment 91 trimis: [seq_nr: 318187] , [check:  26517] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:54,312]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:54,312]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:54,315]  Idx segmente confirmate: [89, 90]
[LINE:330]# INFO     [2020-05-05 10:24:54,315]  
[LINE:331]# INFO     [2020-05-05 10:24:54,316]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:54,316]  
[LINE:222]# INFO     [2020-05-05 10:24:54,316]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:54,316]  Se transmite fereastra 88 - 91
[LINE:224]# INFO     [2020-05-05 10:24:54,316]  Mai sunt 13 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:54,317]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:54,317]  Header segment 88 trimis: [seq_nr: 313986] , [check:  9377] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:54,318]  Header segment 91 trimis: [seq_nr: 318187] , [check:  26517] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:55,319]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:55,320]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:55,322]  Idx segmente confirmate: [89, 90]
[LINE:330]# INFO     [2020-05-05 10:24:55,322]  
[LINE:331]# INFO     [2020-05-05 10:24:55,322]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:55,322]  
[LINE:222]# INFO     [2020-05-05 10:24:55,322]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:55,323]  Se transmite fereastra 88 - 91
[LINE:224]# INFO     [2020-05-05 10:24:55,323]  Mai sunt 13 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:55,323]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:55,323]  Header segment 88 trimis: [seq_nr: 313986] , [check:  9377] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:55,324]  Header segment 91 trimis: [seq_nr: 318187] , [check:  26517] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:56,326]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:56,326]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:56,328]  Idx segmente confirmate: [89, 90]
[LINE:330]# INFO     [2020-05-05 10:24:56,328]  
[LINE:331]# INFO     [2020-05-05 10:24:56,328]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:56,328]  
[LINE:222]# INFO     [2020-05-05 10:24:56,328]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:56,328]  Se transmite fereastra 88 - 91
[LINE:224]# INFO     [2020-05-05 10:24:56,328]  Mai sunt 13 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:56,328]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:56,329]  Header segment 88 trimis: [seq_nr: 313986] , [check:  9377] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:56,329]  Header segment 91 trimis: [seq_nr: 318187] , [check:  26517] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:57,331]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:57,332]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:57,333]  Idx segmente confirmate: [89, 90]
[LINE:330]# INFO     [2020-05-05 10:24:57,333]  
[LINE:331]# INFO     [2020-05-05 10:24:57,333]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:57,334]  
[LINE:222]# INFO     [2020-05-05 10:24:57,334]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:57,334]  Se transmite fereastra 88 - 91
[LINE:224]# INFO     [2020-05-05 10:24:57,334]  Mai sunt 13 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:57,334]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:57,335]  Header segment 88 trimis: [seq_nr: 313986] , [check:  9377] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:57,335]  Header segment 91 trimis: [seq_nr: 318187] , [check:  26517] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:58,337]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:58,337]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:58,339]  Idx segmente confirmate: [89, 90]
[LINE:330]# INFO     [2020-05-05 10:24:58,339]  
[LINE:331]# INFO     [2020-05-05 10:24:58,339]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:58,339]  
[LINE:222]# INFO     [2020-05-05 10:24:58,339]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:58,339]  Se transmite fereastra 88 - 91
[LINE:224]# INFO     [2020-05-05 10:24:58,339]  Mai sunt 13 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:58,339]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:58,340]  Header segment 88 trimis: [seq_nr: 313986] , [check:  9377] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:58,340]  Header segment 91 trimis: [seq_nr: 318187] , [check:  26517] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:24:59,342]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:24:59,342]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:24:59,344]  Idx segmente confirmate: [89, 90]
[LINE:330]# INFO     [2020-05-05 10:24:59,344]  
[LINE:331]# INFO     [2020-05-05 10:24:59,344]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:24:59,344]  
[LINE:222]# INFO     [2020-05-05 10:24:59,344]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:24:59,344]  Se transmite fereastra 88 - 91
[LINE:224]# INFO     [2020-05-05 10:24:59,344]  Mai sunt 13 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:24:59,344]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:24:59,344]  Header segment 88 trimis: [seq_nr: 313986] , [check:  9377] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:24:59,345]  Header segment 91 trimis: [seq_nr: 318187] , [check:  26517] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:00,346]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:00,346]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:00,348]  Idx segmente confirmate: [89, 90]
[LINE:330]# INFO     [2020-05-05 10:25:00,348]  
[LINE:331]# INFO     [2020-05-05 10:25:00,349]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:00,349]  
[LINE:222]# INFO     [2020-05-05 10:25:00,349]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:00,349]  Se transmite fereastra 88 - 91
[LINE:224]# INFO     [2020-05-05 10:25:00,349]  Mai sunt 13 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:00,349]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:00,350]  Header segment 88 trimis: [seq_nr: 313986] , [check:  9377] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:25:00,350]  Header segment 91 trimis: [seq_nr: 318187] , [check:  26517] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:01,351]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:01,352]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:25:01,352]  Header receptor pt segment primit: [ack_nr: 319587] , [check:  8086] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:25:01,354]  Idx segmente confirmate: [89, 90, 91]
[LINE:330]# INFO     [2020-05-05 10:25:01,354]  
[LINE:331]# INFO     [2020-05-05 10:25:01,355]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:01,355]  
[LINE:222]# INFO     [2020-05-05 10:25:01,355]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:01,355]  Se transmite fereastra 88 - 89
[LINE:224]# INFO     [2020-05-05 10:25:01,355]  Mai sunt 13 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:01,356]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:01,356]  Header segment 88 trimis: [seq_nr: 313986] , [check:  9377] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:02,358]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:02,358]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:02,360]  Idx segmente confirmate: [89, 90, 91]
[LINE:330]# INFO     [2020-05-05 10:25:02,360]  
[LINE:331]# INFO     [2020-05-05 10:25:02,360]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:02,360]  
[LINE:222]# INFO     [2020-05-05 10:25:02,360]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:02,361]  Se transmite fereastra 88 - 89
[LINE:224]# INFO     [2020-05-05 10:25:02,361]  Mai sunt 13 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:02,361]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:02,361]  Header segment 88 trimis: [seq_nr: 313986] , [check:  9377] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:03,363]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:03,363]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:03,365]  Idx segmente confirmate: [89, 90, 91]
[LINE:330]# INFO     [2020-05-05 10:25:03,365]  
[LINE:331]# INFO     [2020-05-05 10:25:03,365]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:03,365]  
[LINE:222]# INFO     [2020-05-05 10:25:03,365]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:03,365]  Se transmite fereastra 88 - 89
[LINE:224]# INFO     [2020-05-05 10:25:03,365]  Mai sunt 13 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:03,365]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:03,366]  Header segment 88 trimis: [seq_nr: 313986] , [check:  9377] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:04,367]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:04,368]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:04,371]  Idx segmente confirmate: [89, 90, 91]
[LINE:330]# INFO     [2020-05-05 10:25:04,371]  
[LINE:331]# INFO     [2020-05-05 10:25:04,371]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:04,371]  
[LINE:222]# INFO     [2020-05-05 10:25:04,371]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:04,371]  Se transmite fereastra 88 - 89
[LINE:224]# INFO     [2020-05-05 10:25:04,372]  Mai sunt 13 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:04,372]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:04,372]  Header segment 88 trimis: [seq_nr: 313986] , [check:  9377] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:05,374]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:05,374]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:05,377]  Idx segmente confirmate: [89, 90, 91]
[LINE:330]# INFO     [2020-05-05 10:25:05,377]  
[LINE:331]# INFO     [2020-05-05 10:25:05,377]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:05,378]  
[LINE:222]# INFO     [2020-05-05 10:25:05,378]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:05,378]  Se transmite fereastra 88 - 89
[LINE:224]# INFO     [2020-05-05 10:25:05,378]  Mai sunt 13 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:05,378]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:05,379]  Header segment 88 trimis: [seq_nr: 313986] , [check:  9377] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:06,381]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:06,381]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:06,383]  Idx segmente confirmate: [89, 90, 91]
[LINE:330]# INFO     [2020-05-05 10:25:06,383]  
[LINE:331]# INFO     [2020-05-05 10:25:06,383]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:06,383]  
[LINE:222]# INFO     [2020-05-05 10:25:06,383]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:06,383]  Se transmite fereastra 88 - 89
[LINE:224]# INFO     [2020-05-05 10:25:06,384]  Mai sunt 13 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:06,384]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:06,384]  Header segment 88 trimis: [seq_nr: 313986] , [check:  9377] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:07,386]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:07,386]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:07,388]  Idx segmente confirmate: [89, 90, 91]
[LINE:330]# INFO     [2020-05-05 10:25:07,388]  
[LINE:331]# INFO     [2020-05-05 10:25:07,388]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:07,388]  
[LINE:222]# INFO     [2020-05-05 10:25:07,388]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:07,388]  Se transmite fereastra 88 - 89
[LINE:224]# INFO     [2020-05-05 10:25:07,389]  Mai sunt 13 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:07,389]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:07,389]  Header segment 88 trimis: [seq_nr: 313986] , [check:  9377] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:08,391]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:08,391]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:25:08,392]  Header receptor pt segment primit: [ack_nr: 315386] , [check:  12285] , [window: 4]
[LINE:290]# INFO     [2020-05-05 10:25:08,393]  Idx segmente confirmate: [88, 89, 90, 91]
[LINE:330]# INFO     [2020-05-05 10:25:08,393]  
[LINE:331]# INFO     [2020-05-05 10:25:08,393]  Fereastra a avansat cu 4 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:08,394]  
[LINE:222]# INFO     [2020-05-05 10:25:08,394]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:08,394]  Se transmite fereastra 92 - 95
[LINE:224]# INFO     [2020-05-05 10:25:08,394]  Mai sunt 9 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:08,394]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:08,394]  Header segment 92 trimis: [seq_nr: 319586] , [check:  6033] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:25:08,395]  Header segment 93 trimis: [seq_nr: 320987] , [check:  1422] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:25:08,395]  Header segment 94 trimis: [seq_nr: 322388] , [check:  2080] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:25:08,396]  Header segment 95 trimis: [seq_nr: 323789] , [check:  8175] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:09,398]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:09,398]  Confirmari preluate = 2
[LINE:270]# INFO     [2020-05-05 10:25:09,398]  Header receptor pt segment primit: [ack_nr: 320986] , [check:  6686] , [window: 3]
[LINE:270]# INFO     [2020-05-05 10:25:09,398]  Header receptor pt segment primit: [ack_nr: 322387] , [check:  5287] , [window: 1]
[LINE:290]# INFO     [2020-05-05 10:25:09,400]  Idx segmente confirmate: [92, 93]
[LINE:330]# INFO     [2020-05-05 10:25:09,400]  
[LINE:331]# INFO     [2020-05-05 10:25:09,400]  Fereastra a avansat cu 2 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:09,400]  
[LINE:222]# INFO     [2020-05-05 10:25:09,400]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:09,400]  Se transmite fereastra 94 - 94
[LINE:224]# INFO     [2020-05-05 10:25:09,401]  Mai sunt 7 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:09,401]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:09,401]  Header segment 94 trimis: [seq_nr: 322386] , [check:  2082] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:10,402]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:10,403]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:10,406]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:25:10,406]  
[LINE:331]# INFO     [2020-05-05 10:25:10,406]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:10,407]  
[LINE:222]# INFO     [2020-05-05 10:25:10,407]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:10,407]  Se transmite fereastra 94 - 94
[LINE:224]# INFO     [2020-05-05 10:25:10,407]  Mai sunt 7 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:10,408]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:10,409]  Header segment 94 trimis: [seq_nr: 322386] , [check:  2082] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:11,411]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:11,411]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:11,413]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:25:11,413]  
[LINE:331]# INFO     [2020-05-05 10:25:11,413]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:11,413]  
[LINE:222]# INFO     [2020-05-05 10:25:11,413]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:11,413]  Se transmite fereastra 94 - 94
[LINE:224]# INFO     [2020-05-05 10:25:11,413]  Mai sunt 7 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:11,413]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:11,414]  Header segment 94 trimis: [seq_nr: 322386] , [check:  2082] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:12,415]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:12,416]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:12,417]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:25:12,417]  
[LINE:331]# INFO     [2020-05-05 10:25:12,417]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:12,418]  
[LINE:222]# INFO     [2020-05-05 10:25:12,418]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:12,418]  Se transmite fereastra 94 - 94
[LINE:224]# INFO     [2020-05-05 10:25:12,418]  Mai sunt 7 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:12,418]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:12,418]  Header segment 94 trimis: [seq_nr: 322386] , [check:  2082] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:13,420]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:13,420]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:13,421]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:25:13,422]  
[LINE:331]# INFO     [2020-05-05 10:25:13,422]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:13,422]  
[LINE:222]# INFO     [2020-05-05 10:25:13,422]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:13,422]  Se transmite fereastra 94 - 94
[LINE:224]# INFO     [2020-05-05 10:25:13,422]  Mai sunt 7 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:13,422]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:13,422]  Header segment 94 trimis: [seq_nr: 322386] , [check:  2082] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:14,424]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:14,424]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:14,426]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:25:14,426]  
[LINE:331]# INFO     [2020-05-05 10:25:14,426]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:14,426]  
[LINE:222]# INFO     [2020-05-05 10:25:14,426]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:14,426]  Se transmite fereastra 94 - 94
[LINE:224]# INFO     [2020-05-05 10:25:14,427]  Mai sunt 7 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:14,427]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:14,427]  Header segment 94 trimis: [seq_nr: 322386] , [check:  2082] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:15,428]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:15,428]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:15,430]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:25:15,430]  
[LINE:331]# INFO     [2020-05-05 10:25:15,431]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:15,431]  
[LINE:222]# INFO     [2020-05-05 10:25:15,431]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:15,431]  Se transmite fereastra 94 - 94
[LINE:224]# INFO     [2020-05-05 10:25:15,431]  Mai sunt 7 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:15,431]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:15,431]  Header segment 94 trimis: [seq_nr: 322386] , [check:  2082] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:16,433]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:16,433]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:16,435]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:25:16,435]  
[LINE:331]# INFO     [2020-05-05 10:25:16,435]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:16,435]  
[LINE:222]# INFO     [2020-05-05 10:25:16,435]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:16,436]  Se transmite fereastra 94 - 94
[LINE:224]# INFO     [2020-05-05 10:25:16,436]  Mai sunt 7 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:16,436]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:16,436]  Header segment 94 trimis: [seq_nr: 322386] , [check:  2082] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:17,438]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:17,438]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:17,440]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:25:17,440]  
[LINE:331]# INFO     [2020-05-05 10:25:17,440]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:17,440]  
[LINE:222]# INFO     [2020-05-05 10:25:17,440]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:17,441]  Se transmite fereastra 94 - 94
[LINE:224]# INFO     [2020-05-05 10:25:17,441]  Mai sunt 7 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:17,441]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:17,441]  Header segment 94 trimis: [seq_nr: 322386] , [check:  2082] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:18,443]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:18,443]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:18,446]  Idx segmente confirmate: []
[LINE:330]# INFO     [2020-05-05 10:25:18,446]  
[LINE:331]# INFO     [2020-05-05 10:25:18,446]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:18,447]  
[LINE:222]# INFO     [2020-05-05 10:25:18,447]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:18,447]  Se transmite fereastra 94 - 94
[LINE:224]# INFO     [2020-05-05 10:25:18,447]  Mai sunt 7 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:18,447]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:18,448]  Header segment 94 trimis: [seq_nr: 322386] , [check:  2082] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:19,450]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:19,451]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:25:19,451]  Header receptor pt segment primit: [ack_nr: 323786] , [check:  3886] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:25:19,454]  Idx segmente confirmate: [94]
[LINE:330]# INFO     [2020-05-05 10:25:19,454]  
[LINE:331]# INFO     [2020-05-05 10:25:19,454]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:19,454]  
[LINE:222]# INFO     [2020-05-05 10:25:19,454]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:19,455]  Se transmite fereastra 95 - 97
[LINE:224]# INFO     [2020-05-05 10:25:19,455]  Mai sunt 6 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:19,455]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:19,455]  Header segment 95 trimis: [seq_nr: 323786] , [check:  8178] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:25:19,456]  Header segment 96 trimis: [seq_nr: 325187] , [check:  24131] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:25:19,457]  Header segment 97 trimis: [seq_nr: 326588] , [check:  8915] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:20,459]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:20,459]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:25:20,460]  Header receptor pt segment primit: [ack_nr: 327988] , [check:  194] , [window: 4]
[LINE:290]# INFO     [2020-05-05 10:25:20,461]  Idx segmente confirmate: [97]
[LINE:330]# INFO     [2020-05-05 10:25:20,462]  
[LINE:331]# INFO     [2020-05-05 10:25:20,462]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:20,462]  
[LINE:222]# INFO     [2020-05-05 10:25:20,462]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:20,462]  Se transmite fereastra 95 - 98
[LINE:224]# INFO     [2020-05-05 10:25:20,462]  Mai sunt 6 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:20,462]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:20,463]  Header segment 95 trimis: [seq_nr: 323786] , [check:  8178] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:25:20,463]  Header segment 96 trimis: [seq_nr: 325187] , [check:  24131] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:25:20,463]  Header segment 98 trimis: [seq_nr: 327988] , [check:  23529] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:21,463]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:21,464]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:21,465]  Idx segmente confirmate: [97]
[LINE:330]# INFO     [2020-05-05 10:25:21,465]  
[LINE:331]# INFO     [2020-05-05 10:25:21,465]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:21,466]  
[LINE:222]# INFO     [2020-05-05 10:25:21,466]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:21,466]  Se transmite fereastra 95 - 98
[LINE:224]# INFO     [2020-05-05 10:25:21,466]  Mai sunt 6 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:21,466]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:21,466]  Header segment 95 trimis: [seq_nr: 323786] , [check:  8178] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:25:21,467]  Header segment 96 trimis: [seq_nr: 325187] , [check:  24131] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:25:21,467]  Header segment 98 trimis: [seq_nr: 327988] , [check:  23529] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:22,469]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:22,469]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:25:22,470]  Header receptor pt segment primit: [ack_nr: 329388] , [check:  330] , [window: 4]
[LINE:290]# INFO     [2020-05-05 10:25:22,471]  Idx segmente confirmate: [97, 98]
[LINE:330]# INFO     [2020-05-05 10:25:22,471]  
[LINE:331]# INFO     [2020-05-05 10:25:22,471]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:22,471]  
[LINE:222]# INFO     [2020-05-05 10:25:22,471]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:22,472]  Se transmite fereastra 95 - 98
[LINE:224]# INFO     [2020-05-05 10:25:22,472]  Mai sunt 6 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:22,472]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:22,472]  Header segment 95 trimis: [seq_nr: 323786] , [check:  8178] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:25:22,472]  Header segment 96 trimis: [seq_nr: 325187] , [check:  24131] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:23,474]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:23,474]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:23,476]  Idx segmente confirmate: [97, 98]
[LINE:330]# INFO     [2020-05-05 10:25:23,477]  
[LINE:331]# INFO     [2020-05-05 10:25:23,477]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:23,477]  
[LINE:222]# INFO     [2020-05-05 10:25:23,477]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:23,477]  Se transmite fereastra 95 - 98
[LINE:224]# INFO     [2020-05-05 10:25:23,477]  Mai sunt 6 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:23,478]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:23,478]  Header segment 95 trimis: [seq_nr: 323786] , [check:  8178] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:25:23,478]  Header segment 96 trimis: [seq_nr: 325187] , [check:  24131] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:24,480]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:24,480]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:24,482]  Idx segmente confirmate: [97, 98]
[LINE:330]# INFO     [2020-05-05 10:25:24,482]  
[LINE:331]# INFO     [2020-05-05 10:25:24,482]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:24,482]  
[LINE:222]# INFO     [2020-05-05 10:25:24,482]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:24,483]  Se transmite fereastra 95 - 98
[LINE:224]# INFO     [2020-05-05 10:25:24,483]  Mai sunt 6 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:24,483]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:24,483]  Header segment 95 trimis: [seq_nr: 323786] , [check:  8178] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:25:24,484]  Header segment 96 trimis: [seq_nr: 325187] , [check:  24131] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:25,486]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:25,486]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:25:25,487]  Header receptor pt segment primit: [ack_nr: 325186] , [check:  2486] , [window: 3]
[LINE:290]# INFO     [2020-05-05 10:25:25,488]  Idx segmente confirmate: [95, 97, 98]
[LINE:330]# INFO     [2020-05-05 10:25:25,488]  
[LINE:331]# INFO     [2020-05-05 10:25:25,488]  Fereastra a avansat cu 1 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:25,489]  
[LINE:222]# INFO     [2020-05-05 10:25:25,489]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:25,489]  Se transmite fereastra 96 - 98
[LINE:224]# INFO     [2020-05-05 10:25:25,489]  Mai sunt 5 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:25,489]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:25,489]  Header segment 96 trimis: [seq_nr: 325186] , [check:  24132] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:26,491]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:26,491]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:26,493]  Idx segmente confirmate: [97, 98]
[LINE:330]# INFO     [2020-05-05 10:25:26,493]  
[LINE:331]# INFO     [2020-05-05 10:25:26,493]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:26,493]  
[LINE:222]# INFO     [2020-05-05 10:25:26,493]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:26,493]  Se transmite fereastra 96 - 98
[LINE:224]# INFO     [2020-05-05 10:25:26,494]  Mai sunt 5 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:26,494]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:26,494]  Header segment 96 trimis: [seq_nr: 325186] , [check:  24132] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:27,496]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:27,496]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:27,498]  Idx segmente confirmate: [97, 98]
[LINE:330]# INFO     [2020-05-05 10:25:27,499]  
[LINE:331]# INFO     [2020-05-05 10:25:27,499]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:27,499]  
[LINE:222]# INFO     [2020-05-05 10:25:27,499]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:27,499]  Se transmite fereastra 96 - 98
[LINE:224]# INFO     [2020-05-05 10:25:27,499]  Mai sunt 5 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:27,499]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:27,500]  Header segment 96 trimis: [seq_nr: 325186] , [check:  24132] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:28,502]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:28,502]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:25:28,502]  Header receptor pt segment primit: [ack_nr: 326586] , [check:  1087] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:25:28,504]  Idx segmente confirmate: [96, 97, 98]
[LINE:330]# INFO     [2020-05-05 10:25:28,504]  
[LINE:331]# INFO     [2020-05-05 10:25:28,504]  Fereastra a avansat cu 3 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:28,504]  
[LINE:222]# INFO     [2020-05-05 10:25:28,504]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:28,504]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:28,504]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:28,505]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:28,505]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:136]# INFO     [2020-05-05 10:25:28,505]  Header segment 100 trimis: [seq_nr: 330787] , [check:  11082] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:29,507]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:29,508]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:25:29,508]  Header receptor pt segment primit: [ack_nr: 332010] , [check:  3854] , [window: 2]
[LINE:290]# INFO     [2020-05-05 10:25:29,510]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:29,510]  
[LINE:331]# INFO     [2020-05-05 10:25:29,510]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:29,510]  
[LINE:222]# INFO     [2020-05-05 10:25:29,510]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:29,511]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:29,511]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:29,511]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:29,511]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:30,513]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:30,513]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:30,515]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:30,515]  
[LINE:331]# INFO     [2020-05-05 10:25:30,515]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:30,515]  
[LINE:222]# INFO     [2020-05-05 10:25:30,515]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:30,515]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:30,515]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:30,515]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:30,516]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:31,517]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:31,518]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:31,521]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:31,521]  
[LINE:331]# INFO     [2020-05-05 10:25:31,521]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:31,521]  
[LINE:222]# INFO     [2020-05-05 10:25:31,522]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:31,522]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:31,522]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:31,522]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:31,522]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:32,525]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:32,525]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:32,528]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:32,528]  
[LINE:331]# INFO     [2020-05-05 10:25:32,529]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:32,529]  
[LINE:222]# INFO     [2020-05-05 10:25:32,529]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:32,530]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:32,531]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:32,532]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:32,532]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:33,534]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:33,534]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:33,536]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:33,536]  
[LINE:331]# INFO     [2020-05-05 10:25:33,536]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:33,537]  
[LINE:222]# INFO     [2020-05-05 10:25:33,537]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:33,537]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:33,537]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:33,537]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:33,537]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:34,539]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:34,539]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:34,541]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:34,541]  
[LINE:331]# INFO     [2020-05-05 10:25:34,541]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:34,541]  
[LINE:222]# INFO     [2020-05-05 10:25:34,541]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:34,542]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:34,542]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:34,542]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:34,542]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:35,544]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:35,544]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:35,547]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:35,547]  
[LINE:331]# INFO     [2020-05-05 10:25:35,547]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:35,547]  
[LINE:222]# INFO     [2020-05-05 10:25:35,547]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:35,547]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:35,548]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:35,548]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:35,548]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:36,550]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:36,550]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:36,552]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:36,552]  
[LINE:331]# INFO     [2020-05-05 10:25:36,552]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:36,553]  
[LINE:222]# INFO     [2020-05-05 10:25:36,553]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:36,553]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:36,553]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:36,553]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:36,553]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:37,555]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:37,556]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:37,557]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:37,557]  
[LINE:331]# INFO     [2020-05-05 10:25:37,558]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:37,558]  
[LINE:222]# INFO     [2020-05-05 10:25:37,558]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:37,558]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:37,558]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:37,558]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:37,558]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:38,560]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:38,561]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:38,564]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:38,565]  
[LINE:331]# INFO     [2020-05-05 10:25:38,565]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:38,566]  
[LINE:222]# INFO     [2020-05-05 10:25:38,566]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:38,566]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:38,566]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:38,567]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:38,567]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:39,569]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:39,569]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:39,571]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:39,571]  
[LINE:331]# INFO     [2020-05-05 10:25:39,571]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:39,571]  
[LINE:222]# INFO     [2020-05-05 10:25:39,572]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:39,572]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:39,572]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:39,572]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:39,572]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:40,574]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:40,574]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:40,577]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:40,577]  
[LINE:331]# INFO     [2020-05-05 10:25:40,577]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:40,577]  
[LINE:222]# INFO     [2020-05-05 10:25:40,577]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:40,577]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:40,577]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:40,578]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:40,578]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:41,580]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:41,580]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:41,583]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:41,583]  
[LINE:331]# INFO     [2020-05-05 10:25:41,583]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:41,584]  
[LINE:222]# INFO     [2020-05-05 10:25:41,584]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:41,584]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:41,584]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:41,584]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:41,585]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:42,586]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:42,587]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:42,588]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:42,589]  
[LINE:331]# INFO     [2020-05-05 10:25:42,589]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:42,589]  
[LINE:222]# INFO     [2020-05-05 10:25:42,589]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:42,589]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:42,589]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:42,589]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:42,589]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:43,591]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:43,592]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:43,593]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:43,593]  
[LINE:331]# INFO     [2020-05-05 10:25:43,594]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:43,594]  
[LINE:222]# INFO     [2020-05-05 10:25:43,594]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:43,594]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:43,594]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:43,594]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:43,594]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:44,596]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:44,597]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:44,600]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:44,600]  
[LINE:331]# INFO     [2020-05-05 10:25:44,600]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:44,600]  
[LINE:222]# INFO     [2020-05-05 10:25:44,601]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:44,601]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:44,601]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:44,601]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:44,602]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:45,603]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:45,603]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:45,605]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:45,605]  
[LINE:331]# INFO     [2020-05-05 10:25:45,605]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:45,605]  
[LINE:222]# INFO     [2020-05-05 10:25:45,606]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:45,606]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:45,606]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:45,606]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:45,606]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:46,608]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:46,609]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:46,612]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:46,612]  
[LINE:331]# INFO     [2020-05-05 10:25:46,612]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:46,612]  
[LINE:222]# INFO     [2020-05-05 10:25:46,613]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:46,613]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:46,613]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:46,613]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:46,614]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:47,616]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:47,616]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:47,618]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:47,618]  
[LINE:331]# INFO     [2020-05-05 10:25:47,618]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:47,618]  
[LINE:222]# INFO     [2020-05-05 10:25:47,618]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:47,618]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:47,619]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:47,619]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:47,619]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:48,619]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:48,620]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:48,622]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:48,622]  
[LINE:331]# INFO     [2020-05-05 10:25:48,622]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:48,622]  
[LINE:222]# INFO     [2020-05-05 10:25:48,622]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:48,622]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:48,622]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:48,623]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:48,623]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:49,625]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:49,625]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:49,628]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:49,628]  
[LINE:331]# INFO     [2020-05-05 10:25:49,629]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:49,629]  
[LINE:222]# INFO     [2020-05-05 10:25:49,629]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:49,629]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:49,630]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:49,630]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:49,630]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:50,632]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:50,632]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:50,634]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:50,634]  
[LINE:331]# INFO     [2020-05-05 10:25:50,634]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:50,634]  
[LINE:222]# INFO     [2020-05-05 10:25:50,635]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:50,635]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:50,635]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:50,635]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:50,635]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:51,637]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:51,638]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:51,640]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:51,640]  
[LINE:331]# INFO     [2020-05-05 10:25:51,640]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:51,640]  
[LINE:222]# INFO     [2020-05-05 10:25:51,640]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:51,640]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:51,641]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:51,641]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:51,641]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:52,643]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:52,643]  Confirmari preluate = 0
[LINE:290]# INFO     [2020-05-05 10:25:52,645]  Idx segmente confirmate: [100]
[LINE:330]# INFO     [2020-05-05 10:25:52,645]  
[LINE:331]# INFO     [2020-05-05 10:25:52,645]  Fereastra a avansat cu 0 pozitii.
[LINE:221]# INFO     [2020-05-05 10:25:52,645]  
[LINE:222]# INFO     [2020-05-05 10:25:52,645]  --------------------------------
[LINE:223]# INFO     [2020-05-05 10:25:52,645]  Se transmite fereastra 99 - 100
[LINE:224]# INFO     [2020-05-05 10:25:52,646]  Mai sunt 2 segmente de trimis pana la final
[LINE:225]# INFO     [2020-05-05 10:25:52,646]  --------------------------------
[LINE:136]# INFO     [2020-05-05 10:25:52,646]  Header segment 99 trimis: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:161]# INFO     [2020-05-05 10:25:53,648]  Preluare confirmari
[LINE:182]# INFO     [2020-05-05 10:25:53,649]  Confirmari preluate = 1
[LINE:270]# INFO     [2020-05-05 10:25:53,649]  Header receptor pt segment primit: [ack_nr: 330786] , [check:  979] , [window: 5]
[LINE:290]# INFO     [2020-05-05 10:25:53,653]  Idx segmente confirmate: [99, 100]
[LINE:313]# INFO     [2020-05-05 10:25:53,653]  
[LINE:314]# INFO     [2020-05-05 10:25:53,654]  S-au trimis toate segmentele
[LINE:152]# INFO     [2020-05-05 10:25:53,654]  Buffer golit
[LINE:94]# INFO     [2020-05-05 10:25:53,654]  Am trimis cererea de finalizare cu flagul F catre ('198.8.0.2', 10000)
[LINE:105]# INFO     [2020-05-05 10:25:53,657]  Header cerere trimisa: [seq_nr: 1458] , [check:  2124] , [flag: F]
[LINE:111]# INFO     [2020-05-05 10:25:53,657]  Cererea de finalizare cu flagul F a fost primita de ('198.8.0.2', 10000)
[LINE:112]# INFO     [2020-05-05 10:25:53,657]  Header receptor primit: [ack_nr: 1459] , [check:  583] , [window: 5]
[LINE:113]# INFO     [2020-05-05 10:25:53,657]  S-a incheiat conexiunea
[LINE:114]# INFO     [2020-05-05 10:25:53,658]  
root@55adb4a978fc:/elocal/tema-3-mc-network/src# 


```








### Receptor - mesaje de logging
Rulăm `docker-compose logs receptor` și punem rezultatul aici:
```
root@c15c0fd3b3c5:/elocal/tema-3-mc-network/src# python3 receptor.py -f img_primita.jpg
[LINE:76]# INFO     [2020-05-05 10:18:49,523]  Serverul a pornit pe 0.0.0.0 si portul 10000
[LINE:83]# INFO     [2020-05-05 10:18:49,524]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:19:00,429]  Am primit 23 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:19:00,429]  Header emitator primit: [seq_nr: 104414] , [check:  7520] , [flag: S]
[LINE:35]# INFO     [2020-05-05 10:19:00,430]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:19:00,431]  Header receptor trimis: [ack_nr: 104415] , [check:  26650] , [window: 5]
[LINE:45]# INFO     [2020-05-05 10:19:00,431]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:19:00,431]  
[LINE:83]# INFO     [2020-05-05 10:19:00,432]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:19:00,433]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:19:00,434]  Header emitator primit: [seq_nr: 190786] , [check:  6455] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:19:00,434]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:19:00,435]  Header receptor trimis: [ack_nr: 192186] , [check:  4417] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:19:00,435]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:19:00,435]  
[LINE:83]# INFO     [2020-05-05 10:19:00,436]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:19:01,441]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:19:01,442]  Header emitator primit: [seq_nr: 192186] , [check:  11562] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:19:01,442]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:19:01,444]  Header receptor trimis: [ack_nr: 193586] , [check:  3018] , [window: 1]
[LINE:45]# INFO     [2020-05-05 10:19:01,444]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:19:01,444]  
[LINE:83]# INFO     [2020-05-05 10:19:01,444]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:19:09,484]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:19:09,484]  Header emitator primit: [seq_nr: 193586] , [check:  8236] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:19:09,485]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:19:09,486]  Header receptor trimis: [ack_nr: 194986] , [check:  1618] , [window: 1]
[LINE:45]# INFO     [2020-05-05 10:19:09,487]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:19:09,487]  
[LINE:83]# INFO     [2020-05-05 10:19:09,488]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:19:13,505]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:19:13,506]  Header emitator primit: [seq_nr: 194986] , [check:  10228] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:19:13,506]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:19:13,507]  Header receptor trimis: [ack_nr: 196386] , [check:  218] , [window: 1]
[LINE:45]# INFO     [2020-05-05 10:19:13,508]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:19:13,508]  
[LINE:83]# INFO     [2020-05-05 10:19:13,508]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:19:16,517]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:19:16,517]  Header emitator primit: [seq_nr: 196386] , [check:  15705] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:19:16,518]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:19:16,518]  Header receptor trimis: [ack_nr: 197786] , [check:  864] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:19:16,518]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:19:16,518]  
[LINE:83]# INFO     [2020-05-05 10:19:16,518]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:19:17,523]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:19:17,523]  Header emitator primit: [seq_nr: 199187] , [check:  1204] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:19:17,524]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:19:17,525]  Header receptor trimis: [ack_nr: 200587] , [check:  110] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:19:17,525]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:19:17,525]  
[LINE:83]# INFO     [2020-05-05 10:19:17,526]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:19:19,534]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:19:19,534]  Header emitator primit: [seq_nr: 200587] , [check:  15355] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:19:19,535]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:19:19,536]  Header receptor trimis: [ack_nr: 201987] , [check:  2808] , [window: 1]
[LINE:45]# INFO     [2020-05-05 10:19:19,536]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:19:19,537]  
[LINE:83]# INFO     [2020-05-05 10:19:19,537]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:19:20,539]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:19:20,540]  Header emitator primit: [seq_nr: 197786] , [check:  23156] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:19:20,540]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:19:20,541]  Header receptor trimis: [ack_nr: 199186] , [check:  1512] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:19:20,541]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:19:20,542]  
[LINE:83]# INFO     [2020-05-05 10:19:20,542]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:19:27,576]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:19:27,577]  Header emitator primit: [seq_nr: 201986] , [check:  306] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:19:27,577]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:19:27,578]  Header receptor trimis: [ack_nr: 203386] , [check:  1406] , [window: 4]
[LINE:45]# INFO     [2020-05-05 10:19:27,578]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:19:27,578]  
[LINE:83]# INFO     [2020-05-05 10:19:27,578]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:19:28,584]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:19:28,584]  Header emitator primit: [seq_nr: 206188] , [check:  14938] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:19:28,585]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:19:28,586]  Header receptor trimis: [ack_nr: 207588] , [check:  5396] , [window: 4]
[LINE:45]# INFO     [2020-05-05 10:19:28,586]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:19:28,586]  
[LINE:83]# INFO     [2020-05-05 10:19:28,587]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:19:28,587]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:19:28,587]  Header emitator primit: [seq_nr: 207589] , [check:  10657] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:19:28,588]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:19:28,589]  Header receptor trimis: [ack_nr: 208989] , [check:  3998] , [window: 1]
[LINE:45]# INFO     [2020-05-05 10:19:28,589]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:19:28,590]  
[LINE:83]# INFO     [2020-05-05 10:19:28,590]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:19:29,592]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:19:29,592]  Header emitator primit: [seq_nr: 203386] , [check:  14533] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:19:29,593]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:19:29,595]  Header receptor trimis: [ack_nr: 204786] , [check:  7] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:19:29,595]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:19:29,595]  
[LINE:83]# INFO     [2020-05-05 10:19:29,595]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:19:53,776]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:19:53,776]  Header emitator primit: [seq_nr: 204786] , [check:  24480] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:19:53,777]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:19:53,777]  Header receptor trimis: [ack_nr: 206186] , [check:  6797] , [window: 5]
[LINE:45]# INFO     [2020-05-05 10:19:53,777]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:19:53,777]  
[LINE:83]# INFO     [2020-05-05 10:19:53,778]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:19:54,715]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:19:54,716]  Header emitator primit: [seq_nr: 213189] , [check:  3260] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:19:54,716]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:19:54,717]  Header receptor trimis: [ack_nr: 214589] , [check:  14778] , [window: 5]
[LINE:45]# INFO     [2020-05-05 10:19:54,718]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:19:54,718]  
[LINE:83]# INFO     [2020-05-05 10:19:54,718]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:19:55,719]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:19:55,719]  Header emitator primit: [seq_nr: 208986] , [check:  9895] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:19:55,720]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:19:55,720]  Header receptor trimis: [ack_nr: 210386] , [check:  2600] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:19:55,720]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:19:55,721]  
[LINE:83]# INFO     [2020-05-05 10:19:55,721]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:19:55,721]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:19:55,721]  Header emitator primit: [seq_nr: 214589] , [check:  5631] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:19:55,721]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:19:55,722]  Header receptor trimis: [ack_nr: 215989] , [check:  13380] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:19:55,722]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:19:55,722]  
[LINE:83]# INFO     [2020-05-05 10:19:55,722]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:19:58,734]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:19:58,734]  Header emitator primit: [seq_nr: 211787] , [check:  590] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:19:58,734]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:19:58,735]  Header receptor trimis: [ack_nr: 213187] , [check:  16181] , [window: 4]
[LINE:45]# INFO     [2020-05-05 10:19:58,735]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:19:58,735]  
[LINE:83]# INFO     [2020-05-05 10:19:58,735]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:20:01,747]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:20:01,748]  Header emitator primit: [seq_nr: 210386] , [check:  28497] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:20:01,748]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:20:01,749]  Header receptor trimis: [ack_nr: 211786] , [check:  1200] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:20:01,749]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:20:01,749]  
[LINE:83]# INFO     [2020-05-05 10:20:01,749]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:20:02,751]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:20:02,751]  Header emitator primit: [seq_nr: 217387] , [check:  10192] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:20:02,751]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:20:02,752]  Header receptor trimis: [ack_nr: 218787] , [check:  10582] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:20:02,752]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:20:02,752]  
[LINE:83]# INFO     [2020-05-05 10:20:02,753]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:20:06,769]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:20:06,769]  Header emitator primit: [seq_nr: 215986] , [check:  22279] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:20:06,769]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:20:06,770]  Header receptor trimis: [ack_nr: 217386] , [check:  11983] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:20:06,770]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:20:06,770]  
[LINE:83]# INFO     [2020-05-05 10:20:06,770]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:20:14,810]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:20:14,811]  Header emitator primit: [seq_nr: 220187] , [check:  9213] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:20:14,811]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:20:14,811]  Header receptor trimis: [ack_nr: 221587] , [check:  7780] , [window: 5]
[LINE:45]# INFO     [2020-05-05 10:20:14,812]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:20:14,812]  
[LINE:83]# INFO     [2020-05-05 10:20:14,812]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:20:15,816]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:20:15,816]  Header emitator primit: [seq_nr: 224389] , [check:  3262] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:20:15,817]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:20:15,818]  Header receptor trimis: [ack_nr: 225789] , [check:  3582] , [window: 1]
[LINE:45]# INFO     [2020-05-05 10:20:15,818]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:20:15,818]  
[LINE:83]# INFO     [2020-05-05 10:20:15,818]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:20:18,830]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:20:18,830]  Header emitator primit: [seq_nr: 218786] , [check:  23074] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:20:18,830]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:20:18,831]  Header receptor trimis: [ack_nr: 220186] , [check:  9184] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:20:18,831]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:20:18,831]  
[LINE:83]# INFO     [2020-05-05 10:20:18,831]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:20:20,838]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:20:20,838]  Header emitator primit: [seq_nr: 222987] , [check:  5707] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:20:20,839]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:20:20,840]  Header receptor trimis: [ack_nr: 224387] , [check:  4983] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:20:20,840]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:20:20,840]  
[LINE:83]# INFO     [2020-05-05 10:20:20,841]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:20:24,854]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:20:24,854]  Header emitator primit: [seq_nr: 221586] , [check:  15942] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:20:24,854]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:20:24,855]  Header receptor trimis: [ack_nr: 222986] , [check:  6385] , [window: 1]
[LINE:45]# INFO     [2020-05-05 10:20:24,855]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:20:24,855]  
[LINE:83]# INFO     [2020-05-05 10:20:24,855]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:20:26,864]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:20:26,864]  Header emitator primit: [seq_nr: 225786] , [check:  1120] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:20:26,864]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:20:26,865]  Header receptor trimis: [ack_nr: 227186] , [check:  2183] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:20:26,865]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:20:26,865]  
[LINE:83]# INFO     [2020-05-05 10:20:26,865]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:20:29,879]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:20:29,880]  Header emitator primit: [seq_nr: 227186] , [check:  1380] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:20:29,881]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:20:29,882]  Header receptor trimis: [ack_nr: 228586] , [check:  782] , [window: 4]
[LINE:45]# INFO     [2020-05-05 10:20:29,882]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:20:29,883]  
[LINE:83]# INFO     [2020-05-05 10:20:29,884]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:20:29,884]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:20:29,885]  Header emitator primit: [seq_nr: 229988] , [check:  4403] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:20:29,886]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:20:29,888]  Header receptor trimis: [ack_nr: 231388] , [check:  30749] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:20:29,888]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:20:29,889]  
[LINE:83]# INFO     [2020-05-05 10:20:29,890]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:20:34,906]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:20:34,906]  Header emitator primit: [seq_nr: 231387] , [check:  27295] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:20:34,906]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:20:34,907]  Header receptor trimis: [ack_nr: 232787] , [check:  29351] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:20:34,907]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:20:34,907]  
[LINE:83]# INFO     [2020-05-05 10:20:34,907]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:20:35,910]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:20:35,911]  Header emitator primit: [seq_nr: 228586] , [check:  15024] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:20:35,911]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:20:35,913]  Header receptor trimis: [ack_nr: 229986] , [check:  32150] , [window: 4]
[LINE:45]# INFO     [2020-05-05 10:20:35,913]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:20:35,913]  
[LINE:83]# INFO     [2020-05-05 10:20:35,913]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:20:38,927]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:20:38,927]  Header emitator primit: [seq_nr: 234187] , [check:  10482] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:20:38,928]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:20:38,929]  Header receptor trimis: [ack_nr: 235587] , [check:  26549] , [window: 4]
[LINE:45]# INFO     [2020-05-05 10:20:38,929]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:20:38,930]  
[LINE:83]# INFO     [2020-05-05 10:20:38,930]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:20:43,950]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:20:43,950]  Header emitator primit: [seq_nr: 232786] , [check:  3029] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:20:43,950]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:20:43,951]  Header receptor trimis: [ack_nr: 234186] , [check:  27951] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:20:43,951]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:20:43,951]  
[LINE:83]# INFO     [2020-05-05 10:20:43,951]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:20:53,001]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:20:53,001]  Header emitator primit: [seq_nr: 236987] , [check:  15686] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:20:53,002]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:20:53,003]  Header receptor trimis: [ack_nr: 238387] , [check:  23750] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:20:53,003]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:20:53,003]  
[LINE:83]# INFO     [2020-05-05 10:20:53,003]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:20:54,006]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:20:54,006]  Header emitator primit: [seq_nr: 235586] , [check:  26415] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:20:54,006]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:20:54,007]  Header receptor trimis: [ack_nr: 236986] , [check:  25152] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:20:54,007]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:20:54,007]  
[LINE:83]# INFO     [2020-05-05 10:20:54,007]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:20:56,017]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:20:56,017]  Header emitator primit: [seq_nr: 239787] , [check:  3305] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:20:56,018]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:20:56,018]  Header receptor trimis: [ack_nr: 241187] , [check:  20951] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:20:56,018]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:20:56,018]  
[LINE:83]# INFO     [2020-05-05 10:20:56,019]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:21:05,063]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:21:05,063]  Header emitator primit: [seq_nr: 238386] , [check:  20408] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:21:05,064]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:21:05,065]  Header receptor trimis: [ack_nr: 239786] , [check:  22350] , [window: 4]
[LINE:45]# INFO     [2020-05-05 10:21:05,065]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:21:05,065]  
[LINE:83]# INFO     [2020-05-05 10:21:05,066]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:21:13,116]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:21:13,117]  Header emitator primit: [seq_nr: 243988] , [check:  4297] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:21:13,117]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:21:13,118]  Header receptor trimis: [ack_nr: 245388] , [check:  16751] , [window: 1]
[LINE:45]# INFO     [2020-05-05 10:21:13,119]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:21:13,119]  
[LINE:83]# INFO     [2020-05-05 10:21:13,119]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:21:14,125]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:21:14,126]  Header emitator primit: [seq_nr: 241186] , [check:  10347] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:21:14,127]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:21:14,129]  Header receptor trimis: [ack_nr: 242586] , [check:  19551] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:21:14,129]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:21:14,129]  
[LINE:83]# INFO     [2020-05-05 10:21:14,130]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:21:17,140]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:21:17,140]  Header emitator primit: [seq_nr: 245387] , [check:  22041] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:21:17,141]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:21:17,141]  Header receptor trimis: [ack_nr: 246787] , [check:  15348] , [window: 5]
[LINE:45]# INFO     [2020-05-05 10:21:17,141]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:21:17,141]  
[LINE:83]# INFO     [2020-05-05 10:21:17,141]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:21:19,148]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:21:19,148]  Header emitator primit: [seq_nr: 242586] , [check:  1479] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:21:19,149]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:21:19,150]  Header receptor trimis: [ack_nr: 243986] , [check:  18152] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:21:19,150]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:21:19,150]  
[LINE:83]# INFO     [2020-05-05 10:21:19,151]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:21:23,169]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:21:23,169]  Header emitator primit: [seq_nr: 246786] , [check:  4600] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:21:23,169]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:21:23,170]  Header receptor trimis: [ack_nr: 248186] , [check:  13950] , [window: 4]
[LINE:45]# INFO     [2020-05-05 10:21:23,170]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:21:23,170]  
[LINE:83]# INFO     [2020-05-05 10:21:23,170]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:21:24,175]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:21:24,176]  Header emitator primit: [seq_nr: 252389] , [check:  5974] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:21:24,176]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:21:24,177]  Header receptor trimis: [ack_nr: 253789] , [check:  8348] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:21:24,177]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:21:24,177]  
[LINE:83]# INFO     [2020-05-05 10:21:24,177]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:21:25,182]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:21:25,183]  Header emitator primit: [seq_nr: 248186] , [check:  12921] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:21:25,184]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:21:25,186]  Header receptor trimis: [ack_nr: 249586] , [check:  12550] , [window: 4]
[LINE:45]# INFO     [2020-05-05 10:21:25,186]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:21:25,186]  
[LINE:83]# INFO     [2020-05-05 10:21:25,187]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:21:25,187]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:21:25,187]  Header emitator primit: [seq_nr: 250988] , [check:  7815] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:21:25,188]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:21:25,190]  Header receptor trimis: [ack_nr: 252388] , [check:  9749] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:21:25,190]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:21:25,190]  
[LINE:83]# INFO     [2020-05-05 10:21:25,191]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:21:27,202]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:21:27,202]  Header emitator primit: [seq_nr: 249586] , [check:  8130] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:21:27,203]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:21:27,204]  Header receptor trimis: [ack_nr: 250986] , [check:  11153] , [window: 1]
[LINE:45]# INFO     [2020-05-05 10:21:27,205]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:21:27,205]  
[LINE:83]# INFO     [2020-05-05 10:21:27,205]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:21:51,314]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:21:51,314]  Header emitator primit: [seq_nr: 253786] , [check:  11487] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:21:51,315]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:21:51,315]  Header receptor trimis: [ack_nr: 255186] , [check:  6953] , [window: 1]
[LINE:45]# INFO     [2020-05-05 10:21:51,315]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:21:51,315]  
[LINE:83]# INFO     [2020-05-05 10:21:51,316]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:21:58,348]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:21:58,348]  Header emitator primit: [seq_nr: 255186] , [check:  4035] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:21:58,349]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:21:58,349]  Header receptor trimis: [ack_nr: 256586] , [check:  5551] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:21:58,350]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:21:58,350]  
[LINE:83]# INFO     [2020-05-05 10:21:58,350]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:21:59,352]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:21:59,353]  Header emitator primit: [seq_nr: 256586] , [check:  15504] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:21:59,353]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:21:59,354]  Header receptor trimis: [ack_nr: 257986] , [check:  4152] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:21:59,354]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:21:59,354]  
[LINE:83]# INFO     [2020-05-05 10:21:59,354]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:22:02,366]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:22:02,366]  Header emitator primit: [seq_nr: 257986] , [check:  25124] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:22:02,366]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:22:02,366]  Header receptor trimis: [ack_nr: 259386] , [check:  2752] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:22:02,367]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:22:02,367]  
[LINE:83]# INFO     [2020-05-05 10:22:02,367]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:22:10,405]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:22:10,406]  Header emitator primit: [seq_nr: 259386] , [check:  107] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:22:10,406]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:22:10,407]  Header receptor trimis: [ack_nr: 260786] , [check:  1352] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:22:10,407]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:22:10,407]  
[LINE:83]# INFO     [2020-05-05 10:22:10,407]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:22:13,424]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:22:13,424]  Header emitator primit: [seq_nr: 262187] , [check:  5579] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:22:13,425]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:22:13,426]  Header receptor trimis: [ack_nr: 263587] , [check:  597] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:22:13,426]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:22:13,426]  
[LINE:83]# INFO     [2020-05-05 10:22:13,426]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:22:14,428]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:22:14,429]  Header emitator primit: [seq_nr: 263587] , [check:  15493] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:22:14,429]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:22:14,429]  Header receptor trimis: [ack_nr: 264987] , [check:  1245] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:22:14,430]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:22:14,430]  
[LINE:83]# INFO     [2020-05-05 10:22:14,430]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:22:35,529]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:22:35,529]  Header emitator primit: [seq_nr: 260786] , [check:  20778] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:22:35,530]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:22:35,531]  Header receptor trimis: [ack_nr: 262186] , [check:  16] , [window: 1]
[LINE:45]# INFO     [2020-05-05 10:22:35,531]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:22:35,532]  
[LINE:83]# INFO     [2020-05-05 10:22:35,532]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:22:43,564]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:22:43,565]  Header emitator primit: [seq_nr: 264986] , [check:  14237] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:22:43,565]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:22:43,566]  Header receptor trimis: [ack_nr: 266386] , [check:  3943] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:22:43,566]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:22:43,566]  
[LINE:83]# INFO     [2020-05-05 10:22:43,566]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:22:46,581]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:22:46,581]  Header emitator primit: [seq_nr: 266386] , [check:  12325] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:22:46,582]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:22:46,582]  Header receptor trimis: [ack_nr: 267786] , [check:  2542] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:22:46,582]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:22:46,583]  
[LINE:83]# INFO     [2020-05-05 10:22:46,583]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:22:48,593]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:22:48,594]  Header emitator primit: [seq_nr: 269187] , [check:  938] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:22:48,594]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:22:48,594]  Header receptor trimis: [ack_nr: 270587] , [check:  7932] , [window: 4]
[LINE:45]# INFO     [2020-05-05 10:22:48,594]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:22:48,595]  
[LINE:83]# INFO     [2020-05-05 10:22:48,595]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:22:49,599]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:22:49,599]  Header emitator primit: [seq_nr: 267786] , [check:  28896] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:22:49,600]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:22:49,600]  Header receptor trimis: [ack_nr: 269186] , [check:  1144] , [window: 1]
[LINE:45]# INFO     [2020-05-05 10:22:49,601]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:22:49,601]  
[LINE:83]# INFO     [2020-05-05 10:22:49,601]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:22:51,611]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:22:51,611]  Header emitator primit: [seq_nr: 270586] , [check:  30639] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:22:51,611]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:22:51,612]  Header receptor trimis: [ack_nr: 271986] , [check:  6533] , [window: 4]
[LINE:45]# INFO     [2020-05-05 10:22:51,612]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:22:51,612]  
[LINE:83]# INFO     [2020-05-05 10:22:51,613]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:22:52,617]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:22:52,617]  Header emitator primit: [seq_nr: 271986] , [check:  1175] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:22:52,618]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:22:52,619]  Header receptor trimis: [ack_nr: 273386] , [check:  5136] , [window: 1]
[LINE:45]# INFO     [2020-05-05 10:22:52,619]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:22:52,620]  
[LINE:83]# INFO     [2020-05-05 10:22:52,620]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:22:52,621]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:22:52,621]  Header emitator primit: [seq_nr: 276189] , [check:  16789] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:22:52,621]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:22:52,622]  Header receptor trimis: [ack_nr: 277589] , [check:  932] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:22:52,622]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:22:52,622]  
[LINE:83]# INFO     [2020-05-05 10:22:52,623]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:23:03,672]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:23:03,672]  Header emitator primit: [seq_nr: 273386] , [check:  599] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:23:03,673]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:23:03,673]  Header receptor trimis: [ack_nr: 274786] , [check:  3736] , [window: 1]
[LINE:45]# INFO     [2020-05-05 10:23:03,673]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:23:03,674]  
[LINE:83]# INFO     [2020-05-05 10:23:03,674]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:23:39,888]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:23:39,888]  Header emitator primit: [seq_nr: 274786] , [check:  25266] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:23:39,889]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:23:39,889]  Header receptor trimis: [ack_nr: 276186] , [check:  2332] , [window: 5]
[LINE:45]# INFO     [2020-05-05 10:23:39,889]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:23:39,890]  
[LINE:83]# INFO     [2020-05-05 10:23:39,890]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:23:41,882]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:23:41,883]  Header emitator primit: [seq_nr: 283190] , [check:  4445] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:23:41,883]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:23:41,884]  Header receptor trimis: [ack_nr: 284590] , [check:  10313] , [window: 4]
[LINE:45]# INFO     [2020-05-05 10:23:41,884]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:23:41,885]  
[LINE:83]# INFO     [2020-05-05 10:23:41,885]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:23:42,889]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:23:42,890]  Header emitator primit: [seq_nr: 277586] , [check:  9919] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:23:42,891]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:23:42,892]  Header receptor trimis: [ack_nr: 278986] , [check:  15920] , [window: 1]
[LINE:45]# INFO     [2020-05-05 10:23:42,893]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:23:42,893]  
[LINE:83]# INFO     [2020-05-05 10:23:42,893]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:23:58,975]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:23:58,975]  Header emitator primit: [seq_nr: 278986] , [check:  480] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:23:58,976]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:23:58,977]  Header receptor trimis: [ack_nr: 280386] , [check:  14519] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:23:58,977]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:23:58,978]  
[LINE:83]# INFO     [2020-05-05 10:23:58,978]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:00,985]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:00,985]  Header emitator primit: [seq_nr: 281787] , [check:  2901] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:00,985]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:00,986]  Header receptor trimis: [ack_nr: 283187] , [check:  11718] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:24:00,986]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:00,986]  
[LINE:83]# INFO     [2020-05-05 10:24:00,986]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:01,988]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:01,988]  Header emitator primit: [seq_nr: 280386] , [check:  7212] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:01,989]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:01,989]  Header receptor trimis: [ack_nr: 281786] , [check:  13118] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:24:01,989]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:01,990]  
[LINE:83]# INFO     [2020-05-05 10:24:01,990]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:07,017]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:07,017]  Header emitator primit: [seq_nr: 285987] , [check:  1440] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:07,018]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:07,019]  Header receptor trimis: [ack_nr: 287387] , [check:  7518] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:24:07,020]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:07,020]  
[LINE:83]# INFO     [2020-05-05 10:24:07,020]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:11,040]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:11,040]  Header emitator primit: [seq_nr: 284586] , [check:  9936] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:11,041]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:11,041]  Header receptor trimis: [ack_nr: 285986] , [check:  8920] , [window: 1]
[LINE:45]# INFO     [2020-05-05 10:24:11,041]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:11,042]  
[LINE:83]# INFO     [2020-05-05 10:24:11,042]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:13,052]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:13,052]  Header emitator primit: [seq_nr: 287386] , [check:  4964] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:13,053]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:13,053]  Header receptor trimis: [ack_nr: 288786] , [check:  6117] , [window: 4]
[LINE:45]# INFO     [2020-05-05 10:24:13,054]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:13,054]  
[LINE:83]# INFO     [2020-05-05 10:24:13,054]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:14,058]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:14,058]  Header emitator primit: [seq_nr: 290187] , [check:  4204] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:14,058]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:14,059]  Header receptor trimis: [ack_nr: 291587] , [check:  3317] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:24:14,059]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:14,059]  
[LINE:83]# INFO     [2020-05-05 10:24:14,059]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:15,063]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:15,064]  Header emitator primit: [seq_nr: 291587] , [check:  14490] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:15,064]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:15,065]  Header receptor trimis: [ack_nr: 292987] , [check:  1915] , [window: 5]
[LINE:45]# INFO     [2020-05-05 10:24:15,065]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:15,065]  
[LINE:83]# INFO     [2020-05-05 10:24:15,065]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:16,068]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:16,068]  Header emitator primit: [seq_nr: 288786] , [check:  5884] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:16,069]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:16,070]  Header receptor trimis: [ack_nr: 290186] , [check:  4718] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:24:16,070]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:16,070]  
[LINE:83]# INFO     [2020-05-05 10:24:16,070]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:18,083]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:18,084]  Header emitator primit: [seq_nr: 294387] , [check:  19002] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:18,084]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:18,085]  Header receptor trimis: [ack_nr: 295787] , [check:  31883] , [window: 5]
[LINE:45]# INFO     [2020-05-05 10:24:18,086]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:18,086]  
[LINE:83]# INFO     [2020-05-05 10:24:18,086]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:20,095]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:20,095]  Header emitator primit: [seq_nr: 292986] , [check:  13740] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:20,096]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:20,097]  Header receptor trimis: [ack_nr: 294386] , [check:  517] , [window: 4]
[LINE:45]# INFO     [2020-05-05 10:24:20,097]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:20,097]  
[LINE:83]# INFO     [2020-05-05 10:24:20,097]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:21,103]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:21,103]  Header emitator primit: [seq_nr: 299989] , [check:  31322] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:21,103]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:21,104]  Header receptor trimis: [ack_nr: 301389] , [check:  26282] , [window: 4]
[LINE:45]# INFO     [2020-05-05 10:24:21,104]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:21,104]  
[LINE:83]# INFO     [2020-05-05 10:24:21,104]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:25,126]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:25,127]  Header emitator primit: [seq_nr: 295786] , [check:  2918] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:25,127]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:25,128]  Header receptor trimis: [ack_nr: 297186] , [check:  30484] , [window: 5]
[LINE:45]# INFO     [2020-05-05 10:24:25,128]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:25,128]  
[LINE:83]# INFO     [2020-05-05 10:24:25,128]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:31,168]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:31,168]  Header emitator primit: [seq_nr: 297186] , [check:  1484] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:31,169]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:31,169]  Header receptor trimis: [ack_nr: 298586] , [check:  29087] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:24:31,170]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:31,170]  
[LINE:83]# INFO     [2020-05-05 10:24:31,170]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:33,180]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:33,180]  Header emitator primit: [seq_nr: 298586] , [check:  11178] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:33,181]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:33,182]  Header receptor trimis: [ack_nr: 299986] , [check:  27687] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:24:33,182]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:33,182]  
[LINE:83]# INFO     [2020-05-05 10:24:33,182]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:37,206]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:37,206]  Header emitator primit: [seq_nr: 302787] , [check:  11019] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:37,207]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:37,207]  Header receptor trimis: [ack_nr: 304187] , [check:  23484] , [window: 4]
[LINE:45]# INFO     [2020-05-05 10:24:37,207]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:37,207]  
[LINE:83]# INFO     [2020-05-05 10:24:37,208]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:38,212]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:38,213]  Header emitator primit: [seq_nr: 305588] , [check:  11321] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:38,213]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:38,214]  Header receptor trimis: [ack_nr: 306988] , [check:  20686] , [window: 1]
[LINE:45]# INFO     [2020-05-05 10:24:38,214]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:38,214]  
[LINE:83]# INFO     [2020-05-05 10:24:38,215]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:40,226]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:40,226]  Header emitator primit: [seq_nr: 301386] , [check:  2152] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:40,226]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:40,227]  Header receptor trimis: [ack_nr: 302786] , [check:  24885] , [window: 4]
[LINE:45]# INFO     [2020-05-05 10:24:40,228]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:40,228]  
[LINE:83]# INFO     [2020-05-05 10:24:40,228]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:41,235]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:41,235]  Header emitator primit: [seq_nr: 304186] , [check:  5984] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:41,236]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:41,237]  Header receptor trimis: [ack_nr: 305586] , [check:  22086] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:24:41,238]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:41,238]  
[LINE:83]# INFO     [2020-05-05 10:24:41,238]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:41,238]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:41,238]  Header emitator primit: [seq_nr: 306987] , [check:  36] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:41,239]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:41,240]  Header receptor trimis: [ack_nr: 308387] , [check:  19285] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:24:41,240]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:41,240]  
[LINE:83]# INFO     [2020-05-05 10:24:41,241]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:41,241]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:41,241]  Header emitator primit: [seq_nr: 308388] , [check:  23109] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:41,241]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:41,243]  Header receptor trimis: [ack_nr: 309788] , [check:  17884] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:24:41,243]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:41,243]  
[LINE:83]# INFO     [2020-05-05 10:24:41,243]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:43,250]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:43,251]  Header emitator primit: [seq_nr: 312588] , [check:  6121] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:43,251]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:43,252]  Header receptor trimis: [ack_nr: 313988] , [check:  13686] , [window: 1]
[LINE:45]# INFO     [2020-05-05 10:24:43,252]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:43,252]  
[LINE:83]# INFO     [2020-05-05 10:24:43,252]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:44,255]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:44,256]  Header emitator primit: [seq_nr: 309786] , [check:  11435] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:44,256]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:44,256]  Header receptor trimis: [ack_nr: 311186] , [check:  16488] , [window: 1]
[LINE:45]# INFO     [2020-05-05 10:24:44,256]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:44,256]  
[LINE:83]# INFO     [2020-05-05 10:24:44,256]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:50,289]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:50,289]  Header emitator primit: [seq_nr: 311186] , [check:  1110] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:50,290]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:50,290]  Header receptor trimis: [ack_nr: 312586] , [check:  15086] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:24:50,291]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:50,291]  
[LINE:83]# INFO     [2020-05-05 10:24:50,291]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:51,294]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:51,295]  Header emitator primit: [seq_nr: 315387] , [check:  17824] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:51,295]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:51,296]  Header receptor trimis: [ack_nr: 316787] , [check:  10884] , [window: 4]
[LINE:45]# INFO     [2020-05-05 10:24:51,296]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:51,296]  
[LINE:83]# INFO     [2020-05-05 10:24:51,296]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:24:51,296]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:24:51,296]  Header emitator primit: [seq_nr: 316788] , [check:  932] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:24:51,296]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:24:51,297]  Header receptor trimis: [ack_nr: 318188] , [check:  9483] , [window: 4]
[LINE:45]# INFO     [2020-05-05 10:24:51,297]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:24:51,297]  
[LINE:83]# INFO     [2020-05-05 10:24:51,297]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:25:00,350]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:25:00,351]  Header emitator primit: [seq_nr: 318187] , [check:  26517] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:25:00,351]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:25:00,352]  Header receptor trimis: [ack_nr: 319587] , [check:  8086] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:25:00,352]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:25:00,352]  
[LINE:83]# INFO     [2020-05-05 10:25:00,352]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:25:07,389]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:25:07,390]  Header emitator primit: [seq_nr: 313986] , [check:  9377] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:25:07,390]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:25:07,391]  Header receptor trimis: [ack_nr: 315386] , [check:  12285] , [window: 4]
[LINE:45]# INFO     [2020-05-05 10:25:07,391]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:25:07,391]  
[LINE:83]# INFO     [2020-05-05 10:25:07,391]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:25:08,395]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:25:08,395]  Header emitator primit: [seq_nr: 319586] , [check:  6033] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:25:08,395]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:25:08,396]  Header receptor trimis: [ack_nr: 320986] , [check:  6686] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:25:08,396]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:25:08,396]  
[LINE:83]# INFO     [2020-05-05 10:25:08,396]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:25:08,396]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:25:08,396]  Header emitator primit: [seq_nr: 320987] , [check:  1422] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:25:08,397]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:25:08,397]  Header receptor trimis: [ack_nr: 322387] , [check:  5287] , [window: 1]
[LINE:45]# INFO     [2020-05-05 10:25:08,397]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:25:08,397]  
[LINE:83]# INFO     [2020-05-05 10:25:08,398]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:25:18,449]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:25:18,449]  Header emitator primit: [seq_nr: 322386] , [check:  2082] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:25:18,450]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:25:18,451]  Header receptor trimis: [ack_nr: 323786] , [check:  3886] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:25:18,451]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:25:18,451]  
[LINE:83]# INFO     [2020-05-05 10:25:18,451]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:25:19,457]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:25:19,458]  Header emitator primit: [seq_nr: 326588] , [check:  8915] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:25:19,458]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:25:19,459]  Header receptor trimis: [ack_nr: 327988] , [check:  194] , [window: 4]
[LINE:45]# INFO     [2020-05-05 10:25:19,460]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:25:19,460]  
[LINE:83]# INFO     [2020-05-05 10:25:19,460]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:25:21,468]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:25:21,468]  Header emitator primit: [seq_nr: 327988] , [check:  23529] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:25:21,468]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:25:21,469]  Header receptor trimis: [ack_nr: 329388] , [check:  330] , [window: 4]
[LINE:45]# INFO     [2020-05-05 10:25:21,469]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:25:21,469]  
[LINE:83]# INFO     [2020-05-05 10:25:21,470]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:25:24,484]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:25:24,484]  Header emitator primit: [seq_nr: 323786] , [check:  8178] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:25:24,485]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:25:24,486]  Header receptor trimis: [ack_nr: 325186] , [check:  2486] , [window: 3]
[LINE:45]# INFO     [2020-05-05 10:25:24,486]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:25:24,486]  
[LINE:83]# INFO     [2020-05-05 10:25:24,486]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:25:27,500]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:25:27,500]  Header emitator primit: [seq_nr: 325186] , [check:  24132] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:25:27,501]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:25:27,502]  Header receptor trimis: [ack_nr: 326586] , [check:  1087] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:25:27,502]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:25:27,502]  
[LINE:83]# INFO     [2020-05-05 10:25:27,502]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:25:28,506]  Am primit 1231 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:25:28,506]  Header emitator primit: [seq_nr: 330787] , [check:  11082] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:25:28,506]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:25:28,507]  Header receptor trimis: [ack_nr: 332010] , [check:  3854] , [window: 2]
[LINE:45]# INFO     [2020-05-05 10:25:28,507]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:25:28,507]  
[LINE:83]# INFO     [2020-05-05 10:25:28,507]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:25:45,606]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:25:45,607]  Header emitator primit: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:25:45,607]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:25:45,608]  Header receptor trimis: [ack_nr: 330786] , [check:  979] , [window: 5]
[LINE:45]# INFO     [2020-05-05 10:25:45,608]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:25:45,608]  
[LINE:83]# INFO     [2020-05-05 10:25:45,608]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:25:47,619]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:25:47,620]  Header emitator primit: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:25:47,620]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:25:47,620]  Header receptor trimis: [ack_nr: 330786] , [check:  979] , [window: 5]
[LINE:45]# INFO     [2020-05-05 10:25:47,620]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:25:47,620]  
[LINE:83]# INFO     [2020-05-05 10:25:47,621]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:25:52,647]  Am primit 1408 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:25:52,647]  Header emitator primit: [seq_nr: 329386] , [check:  12143] , [flag: P]
[LINE:35]# INFO     [2020-05-05 10:25:52,647]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:25:52,648]  Header receptor trimis: [ack_nr: 330786] , [check:  979] , [window: 5]
[LINE:45]# INFO     [2020-05-05 10:25:52,648]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:25:52,648]  
[LINE:83]# INFO     [2020-05-05 10:25:52,648]  Asteptam mesaje...
[LINE:85]# INFO     [2020-05-05 10:25:53,655]  Am primit 31 octeti de la ('172.8.0.2', 60924)
[LINE:91]# INFO     [2020-05-05 10:25:53,656]  Header emitator primit: [seq_nr: 1458] , [check:  2124] , [flag: F]
[LINE:35]# INFO     [2020-05-05 10:25:53,656]  Se trimit 20 confirmari
[LINE:44]# INFO     [2020-05-05 10:25:53,657]  Header receptor trimis: [ack_nr: 1459] , [check:  583] , [window: 5]
[LINE:45]# INFO     [2020-05-05 10:25:53,657]  S-au trimis 20 confirmari
[LINE:46]# INFO     [2020-05-05 10:25:53,657]  
[LINE:135]# INFO     [2020-05-05 10:25:53,661]  Transferul a fost incheiat cu succes! :)
[LINE:141]# INFO     [2020-05-05 10:25:53,665]  Fisierul este integru. :)
root@c15c0fd3b3c5:/elocal/tema-3-mc-network/src# 

```
