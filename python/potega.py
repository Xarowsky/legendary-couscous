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
    num1 = int(input("podaj podstawe potegi = "))
    potega = int(input("podaj wykladnik potegi = "))
    assert type(num1) == int
    assert type(potega) == int
    assert pot(100, 0) == 1
    assert pot(100, 1) == 100
    assert pot(2, 3) == 8
    print(pot(num1, potega))

main()
