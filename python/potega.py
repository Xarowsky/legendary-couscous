#!/usr/bin/env python
# -*- coding: utf-8 -*-
# a^n = (a^n-1)*a


def pot(num1, potega):
    result = num1
    if potega == 0:
        result = 1
    else:
        for i in range(potega - 1):
            result = result * num1
    return result


def pot_re(a, n):
    if a == 1:
        return 1
    return pot_re(n, a - 1) * a


def main(args):
    num1 = int(input("podaj podstawe potegi = "))
    potega = int(input("podaj wykladnik potegi = "))
    assert type(num1) == int
    assert type(potega) == int
    assert pot_re(100, 0) == 1
    assert pot_re(100, 1) == 100
    assert pot_re(2, 3) == 8
    print(pot_re(num1, potega))


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
