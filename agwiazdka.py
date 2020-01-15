import numpy as np
import math

#Adam Rembiewski


ruch = [(-1, 0),  # gora
        (0, -1),  # lewo
        (1, 0),  # dol
        (0, 1)]  # prawo


# manhatan - dojscie do celu 2 prostymi liniami
# euklidesowa - jedna prosta linia
def heurystyka(pozycja1, pozycja2):
    x = (pozycja1[0] - pozycja2[0]) ** 2
    y = (pozycja1[1] - pozycja2[1]) ** 2
    return math.sqrt(x + y)


def child(pozycja, mapa):
    tab = []
    for nowa_pozycja in ruch:
        nowax = pozycja[0] + nowa_pozycja[0]
        noway = pozycja[1] + nowa_pozycja[1]
        if (nowax < 0
                or nowax > mapa.shape[0] - 1
                or noway < 0
                or noway > mapa.shape[1] - 1):  # sprawdzenie czy jest w granicy mapy
            continue
        if mapa[nowax][noway] != 0:
            continue
        tab.append((nowax, noway))
    return tab


def szukaj(start, koniec, mapa):
    g = {} # koszt dojścia od pozycji startowej do poz
    f = {}  #koszt
    g[start] = 0
    f[start] = heurystyka(start, koniec)
    zamkniete = [start]
    otwarte = {start}
    rodzic = {}
    while len(otwarte) > 0:
        biezacy = None
        biezacyf = None
        for pozycja in otwarte:
            #okreslanie najtanszego punktu
            if biezacy is None or f[pozycja] < biezacyf:
                biezacyf = f[pozycja]
                biezacy = pozycja
        # przerobiony punkt trafia do listy zamknietej
        otwarte.remove(biezacy)
        zamkniete.append(biezacy)
        # sprawdzanie sąsiadów dla biezacego punktu
        for sasiad in child(biezacy, mapa):
            if sasiad in zamkniete:
                continue
            if sasiad not in otwarte:
                otwarte.add(sasiad)
            elif g[biezacy] + 1 >= g[sasiad]:
                continue
            g[sasiad] = g[biezacy] + 1
            rodzic[sasiad] = biezacy
            #szacowanie kosztu do konca od obecnego punktu
            szacowane = heurystyka(sasiad, koniec)
            f[sasiad] = g[sasiad] + szacowane
        # budowanie drogi po tablicy rodziców
        if biezacy == koniec:
            path = []
            path.append(biezacy)
            while biezacy in rodzic:
                biezacy = rodzic[biezacy]
                path.append(biezacy)
            print(g[koniec]) #wyswietlanie koncowego kosztu calktowitego
            return path


start = (19, 0)
koniec = (0, 19)
koszt = 1
mapa = np.loadtxt("grid.txt")
droga = szukaj(start, koniec, mapa)
for x in droga:
    mapa[x[0]][x[1]] = 3
mapa[start[0]][start[1]] = 1
mapa[koniec[0]][koniec[1]] = 2
print(mapa)
