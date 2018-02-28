#! /usr/bin/env python
# -*- coding: utf-8 -*-

# ascii 32 - 126


def szyfruj(tekst, klucz):
    klucz = klucz % 126
    szyfrogram = ""
    for znak in tekst:
        ascii = ord(znak) + klucz
        if ascii > 126:
            ascii = 31 + (ascii - 126)
        szyfrogram = szyfrogram + chr(ascii)
    return szyfrogram


def deszyfruj(tekst, klucz):
    klucz = klucz % 126
    szyfrogram = ""
    for znak in tekst:
        ascii = ord(znak) - klucz
        if ascii < 32:
            ascii = 125 - abs(ascii - 32)
        szyfrogram = szyfrogram + chr(ascii)
    return szyfrogram


def main(args):
    tekst = input("podaj tekst: ")
    ragnarok = int(input("poddaj klucz: "))
    szyfrogram = szyfruj(tekst, ragnarok)
    print(szyfrogram)
    tekst = deszyfruj(szyfrogram, ragnarok)
    print(tekst)
    return 0


#        ascii = ord(znak) + klucz
#        if ascii > 126:
#            ascii -= 26
#            szyfrogram += chr(ascii)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
