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


def wysz_bin(lista, el):
    lewy, prawy = 0, len(lista) - 1
    while lewy < prawy:
        sr = floor(lewy + prawy / 2
        if el < l[sr]:
    return -1


def main(args):
    lista = [4, 1, 2, 7, 8, 9, 5, 8, 3, 7]
    el = 3
    lista.sort()
    print(wysz_lin(lista, el))
    wysz_bin(lista, el)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
