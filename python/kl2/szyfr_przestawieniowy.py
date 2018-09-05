#! /usr/bin/env python
# -*- coding: utf-8 -*-


def szyfruj(tekst, klucz):

    reszta = len(tekst) % klucz
    if reszta > 0:
        tekst += (klucz - reszta) * "."
    print(tekst)

    for i in range(klucz):
        for j in range(int(len(tekst) / klucz)):
            print(i + j * klucz, )
    return ""


def main(args):
    tekst = input('podaj tekst ')
    klucz = int(input('podaj ilosc znakow w wierszu '))
    while (2 * klucz > len(tekst)):
        klucz = input('podaj ilosc znakow w wierszu ')
    print(szyfruj(tekst, klucz))


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
