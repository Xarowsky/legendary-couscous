#! /usr/bin/env python
# -*- coding: utf-8 -*-


def euklides(a, b):

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def main(args):
    num1 = int(input("liczba a = "))
    num2 = int(input("liczba b = "))
    print(euklides(num1, num2))
    assert euklides(1989, 867) == 51
    assert euklides(10, 5) == 5
    print("Nwd({:d}, {:d}) = {:d}".format(num1, num2, euklides(num1, num2)))


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
