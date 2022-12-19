import random
import copy
import pickle
procesy = []         # staly slownik przechowujacy wszystkie procesy
aktualne = []        # lista z procesami 'ruchomymi'
zakonczone = []      # lista z procesami zakonczonymi
n= len(procesy)
print("1. Dzialaj na zapisanych procesach \n2.Stworz nowe procesy")
decyzja = int(input("Wybierz dzialanie (1 lub 2): "))
if decyzja == 1:
    plik = open("procesy.txt", 'rb')
    procesy = pickle.load(plik)
    n = len(procesy)
elif decyzja == 2:
    n = int(input("Podaj liczbe procesow: "))
    srednia = int(input("Podaj srednia czasow wykonywania procesow: "))
    odchylenie = int(input("Podaj odchylenie standardowe dla czasow wykonywania procesow: "))
    a = int(input("Podaj poczatek zakresu czasu przyjscia: "))
    b = int(input("Podaj koniec zakresu czasu przyjscia:"))
    while b < a:
        print("Wprowadzono nieprawidlowe dane. Sprobuj ponownie.")
        b = int(input("Podaj koniec zakresu czasu przyjscia:"))
    for i in range(n):  # generowanie procesow
        czas_przyjscia = random.randrange(a, b + 1)  # generowanie czasu przyjscia procesu
        if srednia - odchylenie < 0:
            pocz = 0
        else:
            pocz = srednia - odchylenie
        czas_trwania = random.randrange(pocz, srednia + odchylenie + 1)  # generowanie czasu trwania procesu
        lista = []
        lista.append(czas_przyjscia)  # przyporzadkowanie procesowi jego czasów przyjscia i trawania
        lista.append(czas_trwania)
        lista.append(0)  # dodanie procesorowi dwoch zmiennych (czasy zakonczenia i czekania)
        lista.append(0)
        procesy.append(lista)  # tworzenie listy procesow
        file = open("procesy.txt",'wb')
        pickle.dump(procesy,file)

# Algorytm SJF (niewywłaszczeniowy)
lista = []
czas_w_petli=0
while True:     # petla ktora wykonuje sie az do zakonczenia wszystkich procesow
    for i in range(len(procesy)):
        if procesy[i][0] == czas_w_petli:
            x = [procesy[i][0], procesy[i][1], procesy[i][2], procesy[i][3]]  # tworzymy liste procesow, ktore przyszly
            lista.append(x)
    lista.sort(key=lambda pair: pair[1])  # sortujemy procesy ktore wlasnie przyszly po dlugosci ich czasu wykonywania
    if len(lista) > 0:
        for i in range(len(lista)):
            x = copy.deepcopy(lista[i])  # kazdy proces, ktory przyszedl
            aktualne.append(x)     # dodajemy do listy procesow ktore juz się rozpoczely tworzac kolejke
    lista = []
    czas_w_petli += 1
    if len(aktualne) >= 1:          # dzialania podejmujemy gdy kolejeka nie jest pusta
        aktualne[0][1] -= 1         # zmniejszamy pozostaly czas wykonania procesu pierwszego w kolejce o 1 j. czasu
        if aktualne[0][1] == 0:                      # gdy program pierwszy w kolejce sie zakonczy
            aktualne[0][2] = czas_w_petli            # przypisujemy mu jego czas zakonczenia
            if len(zakonczone) > 0:                                   # jeśli lista procesow zakonczonych nie jest pusta
                czas_oczekiwania = zakonczone[-1][2] - aktualne[0][0]           # obliczamy czas oczekiwania procesu
                if czas_oczekiwania < 0:
                    czas_oczekiwania = 0
            else:                                      # jesli lista zakonczona jest pusta to proces aktualny jest
                czas_oczekiwania = 0                   # pierwszym procesem, nie czeka
            aktualne[0][3] = czas_oczekiwania
            zakonczone.append(aktualne[0])
            del aktualne[0]
            aktualne.sort(key=lambda pair: pair[1])  # po zakonczeniu procesu sortujemy liste spowrotem
    if len(aktualne) == 0 and len(zakonczone) == n:
        break
print("procesy", procesy)
print("aktualne", aktualne)
print("zakonczone", zakonczone)
suma = 0
for i in range(n):
    suma += zakonczone[i][3]
print("Czasy kolejno wykonywanych procesow:")
print("Zakoncznia\t|\tOczekiwania")
for element in zakonczone:
    print("\t", element[2],"\t\t|\t\t", element[3], sep="")
print("Dla algorytmu SJF, sredni czas oczekiwania wynosi:", suma/n)
