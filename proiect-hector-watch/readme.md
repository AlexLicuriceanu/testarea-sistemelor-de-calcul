# Proiect TSC - Hector Watch 

## Nume: Alexandru LICURICEANU
## Grupa: 332CD


## Implementarea schemei
Am plecat de la schema data in enuntul proiectului, pe care am
creat-o in Fusion folosind componentele din biblioteca Hector-Watch.

Pentru componentele care nu erau potrivite pentru proiect, cum
ar fi butoanele si conectorul LCD, m-am uitat in datasheet-urile
lor si am realizat simbolul si footprintul corect al acestora.

Am respectat urmatoarele constrangeri: Toate rezistentele si condensatoarele
sunt SMD in capsula 0402, cu exceptie unde se mentioneaza ca sunt in capsula
0603 sau tantal case C.

Verificarea ERC a intors 0 errori si 0 warning-uri.

## Implementare board-ului
(partea distractiva..)

In primul rand, am redimensionat board-ul sa fie in forma de cerc
cu raza de 18 centimetri.

Apoi am separat componentele care stau pe top de cele de pe bottom si am inceput
sa le plasez pe board: Mai intai am pozitionat butoanele si modulul cu conectorul
USB conform specificatiilor date in enunt, iar apoi am plasat microcontroller-ul,
cu partea cu antena orientata in exteriorul PCB-ului.

De aici doar am pus restul componentelor in pozitii favorabile (sa abia trasee
cat mai scurte pentru cand voi face rutarea). Am incercat sa tin cont si de
condensatoarele de decuplare, sa le pun cat mai aproape de pinii de alimentare ai
modulelor din care fac parte, iar apoi am facut planul de masa.

In momentul acesta, doar componentele de pe top sunt puse pe board, asa ca am
inceput rutarea manuala, iar dupa mult trial and error am reusit sa conectez
toate componentele de pe top.

Am facut acelasi proces si pe bottom: mai intai am pus componentele care trebuie
sa stea intr-o anumita locatie, apoi restul si am facut planul de masa si rutarea.

Pentru traseele de putere (VBAT, VBUS, 3V3, GND) am folosit grosime de 0.3mm,
iar pentru restul 0.127mm si am evitat sa fac unghiuri drepte la rutare.

La final, am decupat PCB-ul si planurile de masa in locul unde
se afla modulul de antena al microcontroller-ului si am aranjat
silkboard-ul.

Verificarea DRC a intors 3 erori de overlap/clearance, dar le-am
acceptat deoarece erau overlap-uri destul de mici.
