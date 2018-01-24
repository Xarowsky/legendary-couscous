#! /usr/bin/env python
# -*- coding: utf-8 -*-
from math import floor


def sort_wstaw(lista):
    """wersja liniowa"""
    for i in range(1, len(lista)):
        el = lista[i]
        k = i - 1
        while k >= 0 and lista[k] < el:
            lista[k + 1] = lista[k]
            k -= 1
        lista[k + 1] = el
    return lista


def wysz_bin_it(lewy, prawy, lista, el):
    while lewy < prawy:
        srodek = floor((lewy + prawy) / 2)
                if el <= prawy:



def sort_wst_bin(lista):
    for i in range(1, len(lista)):
        el = lista[i]
        k = wysz_bin(0, i, lista, el)
        lista = lista[:k] + [el] + lista[k:i] + lista[i:] + lista[i + 1:]
        print(lista)
    return lista


def main(args):
    lista = [9, 6, 8, 4, 7, 5, 2, 3, 1]
    print(lista)
#   print(sort_wstaw(lista))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
