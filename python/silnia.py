#! /usr/bin/env python
# -*- coding: utf-8 -*-
# N! = 1 dla {0, 1}
# n! = 1*2*...*n dla N+ -{0, 1}


def silnia(num1):
    """silnia"""
    wynik = 1
    for i in range(2, num1 + 1):
        wynik = wynik * i
    return wynik


def main():
    num1 = int(input("podaj liczbę ="))
    print(silnia(num1))
    assert type(num1) == int
    assert silnia(1) == 1
    assert silnia(0) == 1
    assert silnia(7) == 5040
    return 0

main()
