import random
import pickle
kroki = 0
ciag = []
ramki = []
print("1. Dzialaj na zapisanym ciagu \n2. Stworz nowy ciag odniesienia")
decyzja = int(input("Wybierz dzialanie: "))
if decyzja == 1:
    plik = open("ciag.txt", 'rb')
    ciag = pickle.load(plik)
elif decyzja == 2:
    n = int(input("Podaj dlugosc ciagu odniesienia: "))
    s = int(input("Podaj ilosc stron: "))
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
            del ramki[0]
            ramki.append(ciag[0])
            del ciag[0]
        else:       # lub zostawiamy bez zmian
            del ciag[0]
            kroki += 1
            continue
    kroki += 1
print(kroki, "\t\t|\t", ramki, "\t\t|\t")