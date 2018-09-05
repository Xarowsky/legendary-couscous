#! /usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
    a = 0
    while a < 1 or a > 99:
        a = int(input("podaj liczbe od 1 do 99"))

    for i in range(2, 101, 2):
        if a == i:
            print("parzysta")
            return 0
    print("nieparzysta")


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
