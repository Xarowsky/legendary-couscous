#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint


def losuj(ileliczb, maksliczb):
    liczby = []
    ile = 0  # ilość wylosowanych liczb
    while ile < ileliczb:
    #for i in range(ileliczb):
        liczba = randint(0, maksliczb)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            ile += 1
    return liczby


def pobierz_typy(ileliczb):
    typy = set()  # pusty zbiór
    ile = 0
    while ile < ileliczb:

        typ = input("Podaj typ: ")
        if typ not in typy:
            typy.add(typ)
            ile += 1
    return typy


def main(args):
    maksliczb = int(input("Podaj górny zakres: "))
    ileliczb = int(input("Ile liczb chcesz zgadnąć?"))

    while ileliczb > maksliczb:
        ileliczb = int(input("Ile liczb chcesz zgadnąć z %s ?" % maksliczb))

    liczby = losuj(ileliczb, maksliczb)
    typy = pobierz_typy(ileliczb)
    trafione = set(liczby) & set(typy)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
