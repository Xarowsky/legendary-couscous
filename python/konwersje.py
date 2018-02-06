#! /usr/bin/env python
# -*- coding: utf-8 -*-


def dec2other(liczba10, podstawa):
    """konwersja liczby dziesietnej na system o podanej podstawie"""
    liczba = []
    while liczba10 != 0:
        reszta = liczba10 % podstawa
        if reszta > 9:
            reszta = chr(reszta + 55)
        liczba.append(str(reszta))
        liczba10 = int(liczba10 / podstawa)
    liczba.reverse()
    return liczba


def zamiana1():
    liczba = int(input("podaj liczbe: "))
    podstawa = 0
    while podstawa < 2 or podstawa > 16:
        podstawa = int(input("podaj podstawe: "))
    print("wynik konwersji: {}(10) = {}({})".format(
        liczba, dec2other(liczba, podstawa), podstawa))


def zamiana2():
    liczba = input("podaj liczbe: ")
    podstawa = 0
    while podstawa < 2 or podstawa > 16:
        podstawa = int(input("podaj podstawe: "))
    # pass
    print("wynik konwersji: {}({}) = {}".format(
        liczba, podstawa, other2dec(liczba, podstawa)))


def other2dec(liczba, podstawa):
    liczba10 = 0
    potega = len(liczba) - 1
    for cyfra in liczba:
        if not cyfra.isdigit():
            liczba10 += (ord(cyfra.upper) - 55) * (podstawa ** potega)
        else:
            liczba += int(cyfra) * (podstawa ** potega)
    potega -= 1
    return liczba10


def main(args):
    zamiana1()
    zamiana2()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
