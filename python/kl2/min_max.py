#! /usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint


def maksimum(lista):
    max = lista[0]
    for i in lista:
        if i > max:
            max = i
    return max


def losuj(ile, zakres):
    lista = []
    for i in range(ile):
        lista.append(randint(0, zakres))
    return lista


def minimum(lista):
    min = lista[0]
    for i in lista:
        if i < min:
            min = i
    return min


def min_max(lista):
    lmin = [0]
    lmax = [0]
    for i, el in enumerate(lista):
        if i > lista[i + 1]:
            el = lmin
            lista[i + 1]
        else:
            el = lmax
            lista[i + 1] = lmin
    max = lmax[0]
    for i in lmax:
        if i > max:
            max = i
    min = lmin[0]
    for i in lmin:
        if i < min:
            min = i
    return min, max


def main(args):
    ile = 20
    zakres = 50
    lista = losuj(ile, zakres)
    print(lista)
    # print(minimum(lista))
    # print(maksimum(lista))
    print(min_max(lista))


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
