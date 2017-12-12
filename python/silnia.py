#! /usr/bin/env python
# -*- coding: utf-8 -*-
# N! = 1 dla {0, 1}
# n! = 1*2*...*n dla N+ -{0, 1}
# n! = (n - 1)! * n


def silnia_it(num1):
    """silnia"""
    wynik = 1
    for i in range(2, num1 + 1):
        wynik = wynik * i
    return wynik


def silnia_re(n):
    if n < 2:
        return 1
    return silnia_re(n - 1) * n


def main(args):
    num1 = int(input("podaj liczbę ="))
    print(silnia_re(num1))
    assert type(num1) == int
    assert silnia_re(1) == 1
    assert silnia_re(0) == 1
    assert silnia_re(7) == 5040
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
