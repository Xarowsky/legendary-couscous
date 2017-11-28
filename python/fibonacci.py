#! /usr/bin/env python
# -*- coding: utf-8 -*-


def fib_it(n):
    a, b = (0, 1)
    if n == 0:
        print a
        return a
    elif n == 1:
        print b
        return b
    for i in range(0, n):
        a = b
        a = b + a
    print b
    return b


def main(args):
    n = int(input("który wyraz"))
    fib_it(n)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
