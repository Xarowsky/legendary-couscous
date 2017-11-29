#! /usr/bin/env python
# -*- coding: utf-8 -*-


def fib_it(n):
    a, b = (0, 1)
    if n == 0:
        print(a)
        return a
    elif n == 1:
        print(b)
        return b
    for i in range(1, n):
        # tmp = b
        # b = a + b
        # a = tmp
        a, b = b, a + b
        print(a, " wyraz ", i, ": ", b)
    return b


def fib_it2(n):
    a, b = (0, 1)
    if n == 0:
        print(a)
        return a
    elif n == 1:
        print(b)
        return b
    while n - 1 > 0:
        a, b = b, a + b
        print(a, " ", b)
        n = n - 1
    return b


def main(args):
    n = int(input("który wyraz "))
    fib_it2(n)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
