#!/usr/bin/env python
# -*- coding: utf-8 -*-


def pot(num1, potega):
    result = num1
    if potega == 0:
        result = 1
    else:
        for i in range(potega - 1):
            result = result * num1
    return result


def main():
    num1 = int(input("podaj liczbe ktora chcesz podniesc do potegi = "))
    potega = int(input("podaj potege = "))
    print(pot(num1, potega))

main()
