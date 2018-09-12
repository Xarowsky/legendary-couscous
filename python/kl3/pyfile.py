#! /usr/bin/env python
# -*- coding: utf-8 -*-

def dodawanie(a, b):
    return a + b


def odejmowanie(a, b):
    return a - b


def mnozenie(a, b):
    return a * b


def dzielenie(a, b):
    return a / b


def main(args):
    a = int(input("podaj liczbe a "))
    b = int(input("podaj liczbe b "))
    print(dodawanie(a, b))
    print(odejmowanie(a, b))
    print(mnozenie(a, b))
    print(dzielenie(a, b))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
