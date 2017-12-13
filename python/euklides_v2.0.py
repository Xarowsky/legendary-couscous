#! /usr/bin/env python
# -*- coding: utf-8 -*-


def euklides(a, b):
    while a > b:
        a = a % b
        b = b - a
    return b


def euklides_re(a, b):
    if b == 0:
        return a
    return euklides_re(b, a % b)


def main(args):
    num1 = int(input("liczba a = "))
    num2 = int(input("liczba b = "))
    print(euklides_re(num1, num2))
    assert euklides_re(1989, 867) == 51
    assert euklides_re(10, 5) == 5
    print("Nwd({:d}, {:d}) = {:d}".format(num1, num2, euklides(num1, num2)))


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
