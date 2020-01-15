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
    g = {}
    f = {}
    pass
    g[start] = 0
    f[start] = heurystyka(start, koniec)
    if mapa[koniec[0]][koniec[1]] == 5:
        print("Punkt końcowy jest przeszkodą")
        return None
    if mapa[start[0]][start[1]] == 5:
        print("Punkt startowy jest przeszkodą")
        return None
    if start == koniec:
        print("Punkt początkowy jest też punktem końcowym")
        return {start}
    zamkniete = []
    otwarte = {start}
    rodzic = {}
    while otwarte:
        aktualny = None
        aktualnyf = None
        for p in otwarte:
            if aktualny is None or f[p] < aktualnyf:
                aktualny = p
                aktualnyf = f[p]
        # odtwarzanie drogi po tablicy(słowniku)rodziców
        if aktualny == koniec:
            droga = set()
            droga.add(aktualny)
            while aktualny in rodzic:
                aktualny = rodzic[aktualny]
                droga.add(aktualny)
            return droga
        # przerobiony punkt trafia do listy zamknietej
        otwarte.remove(aktualny)
        zamkniete.append(aktualny)
        # sprawdzanie sąsiadów dla punktu aktualny
        for sasiad in child(aktualny, mapa):
            if sasiad in zamkniete:
                continue
            if sasiad not in otwarte:
                otwarte.add(sasiad)
            elif g[aktualny] + 1 >= g[sasiad]:
                continue
            rodzic[sasiad] = aktualny
            g[sasiad] = g[aktualny] + 1
            h = heurystyka(sasiad, koniec)
            f[sasiad] = g[sasiad] + h

start = (19, 0)
koniec = (0, 19)
koszt = 1
mapa = np.loadtxt("grid.txt")
trasa = szukaj(start, koniec, mapa)
if trasa.__len__() == 0:
    print("Nie znaleziono drogi")
else:
    for x in trasa:
        mapa[x[0]][x[1]] = 3
    mapa[start[0]][start[1]] = 1
    mapa[koniec[0]][koniec[1]] = 2
    print(mapa)
