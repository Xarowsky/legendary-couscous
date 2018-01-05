#! /usr/bin/env python
# -*- coding: utf-8 -*-
from math import floor


def wysz_lin(l, el):
    for i in range(0, len(l)):
        if el == l[i]:
            return i
    return -1


# int wysz_lin(int l, int el, int n) {
#     for (int i; i < n; i++ ) {
#         if (l[i] == el)
#             return i
#    }
#   return -1
# }


def wysz_bin_it(lista, el):
    lewy, prawy = 0, len(lista) - 1
    while lewy < prawy:
        sr = floor((lewy + prawy) / 2)
        if el <= lista[sr]:
                prawy = sr
        else:
            lewy = sr
    if lista[lewy] == el:
        return lewy
    else:
        return -1


def wysz_bin_rek(lewy, prawy, lista, el):
    if lewy > prawy:
        return -1
    sr = floor((lewy + prawy) / 2)
    if el == lista[sr]:
        return sr + 1
    if el < lista[sr]:
        return wysz_bin_rek(lewy, sr - 1, lista, el)
    else:
        return wysz_bin_rek(sr + 1, prawy, lista, el)


def main(args):
    lista = [4, 1, 2, 7, 8, 9, 5, 8, 3, 7]
    el = 1
    lista.sort()
    print(lista)
#    print(wysz_lin(lista, el))
    print(wysz_bin_rek(0, len(lista) - 1, lista, el))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
