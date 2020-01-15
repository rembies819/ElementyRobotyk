import numpy as np
import math

#Adam Rembiewski


ruch = [(-1, 0),  # gora
        (0, -1),  # lewo
        (1, 0),  # dol
        (0, 1)]  # prawo


# manhatan - dojscie do celu 2 prostymi liniami
# euklidesowa - jedna prosta linia
def heurystyka(start, cel):
    x = (start[0] - cel[0]) ** 2
    y = (start[1] - cel[1]) ** 2
    return math.sqrt(x + y)


def children(pozycja, mapa):
    tab = []
    for x,y in ruch:
        x2 = pozycja[0] + x
        y2 = pozycja[1] + y
        if (x2 < 0
                or x2 > mapa.shape[0] - 1
                or y2 < 0
                or y2 > mapa.shape[1] - 1):  # sprawdzenie czy jest w granicy mapy
            continue
        if mapa[x2][y2] != 0:
            continue
        tab.append((x2, y2))
    return tab
def koszt_ruchu(pozycja):
    return 1

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
        # sprawdzanie dzieci dla biezacego punktu
        for child in children(biezacy, mapa):
            if child in zamkniete:
                continue #juz sprawdzone
            if child not in otwarte:
                otwarte.add(child) #nowe dziecko
            elif g[child] <= g[biezacy] + koszt_ruchu(biezacy):
                continue #gorszy wynik
            g[child] = g[biezacy] + 1
            rodzic[child] = biezacy
            #szacowanie kosztu do konca od obecnego punktu
            szacowane = heurystyka(child, koniec)
            f[child] = g[child] + szacowane
        # budowanie drogi po tablicy rodziców
        if biezacy == koniec:
            path = [biezacy]
            while biezacy in rodzic:
                biezacy = rodzic[biezacy]
                path.append(biezacy)
            print(g[koniec]) #wyswietlanie koncowego kosztu calktowitego
            return path


start = (19, 0)
koniec = (0, 19)
mapa = np.loadtxt("grid.txt")
droga = szukaj(start, koniec, mapa)
for x in droga:
    mapa[x[0]][x[1]] = 3
print(mapa)
