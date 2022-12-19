import random
import pickle

strony = []
ciag = []
ramki = []
x = 0
y = 0
kroki = 0
print("1. Dzialaj na zapisanym ciagu \n2. Stworz nowy ciag odniesienia")
decyzja = int(input("Wybierz dzialanie: "))
if decyzja == 1:
    plik = open("ciag.txt", 'rb')
    ciag = pickle.load(plik)
    m = max(ciag)
    for i in range(m):
        strony.append([i+1, 0])
elif decyzja == 2:
    n = int(input("Podaj dlugosc ciagu odniesienia: "))
    s = int(input("Podaj ilosc stron: "))
    for i in range(s):
        strony.append([i + 1, 0])  # [nr.strony, pozycja ostatniego uzywania]
    print(strony)
    for i in range(n):  # tworzymy losowy ciag odniesienia
        x = random.randrange(1, s + 1)
        ciag.append(x)
    plik = open("ciag.txt", 'wb')
    pickle.dump(ciag, plik)
r = int(input("Podaj liczbe ramek (rozmiar okna): "))

print("Ciag odniesienia:", ciag)
print("Krok\t|\tOkno\t\t|\tW kolejce")
while len(ciag) != 0:
    print(kroki, "\t\t|\t", ramki, "\t\t|\t", ciag[0])
    for i in range(len(strony)):
        if ciag[0] == strony[i][0]:
            x = i   # zapamietujemy pozycje liczby z ciagu w ciagu stron
            continue
    strony[x][1] = kroki
    if len(ramki) < r:          # dodajemy niepowtarzajace sie elementy do okna az do momentu gdy okno osiagnie
        if ciag[0] not in ramki:        # swoja makwymalna wielkosc
            ramki.append(ciag[0])
            del ciag[0]
        else:
            del ciag[0]
            kroki += 1
            continue
    else:       # gdy okno osiagnie swoja maksymalna wielkosc
        if ciag[0] not in ramki:    # usuwamy i odoajemy do niego odpowiednie pola
            lista = []       # tworzymy tymczasawa liste zawierajaca elementy ramki z czasem ich ostatniego uzycia
            for i in range(len(ramki)):
                for j in range(len(strony)):
                    if ramki[i] == strony[j][0]:
                        lista.append(strony[j])
            lista.sort(key=lambda pair: pair[1])  # sortujemy liste od najdawniej do najwczesniej uzywanych
            for i in range(len(ramki)):     # sprawdzamy na ktorej pozycji w ramce znajduje sie najdawniej uzyta strona
                if ramki[i] == lista[0][0]:
                    y = i
            del ramki[y]    # usuwamy ja
            ramki.append(ciag[0])
            del ciag[0]
        else:       # lub zostawiamy bez zmian
            del ciag[0]
            strony[x][1] = kroki
            kroki += 1
            continue
    kroki += 1
print(kroki, "\t\t|\t", ramki, "\t\t|\t")