#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  klasa_uczen.py
import os
from uczniowie_model import *
from baza import czy_jest, czytaj_dane

def dodaj_dane(dane):
    
    for model, plik in dane.items():
        print(plik)
    

def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()
    baza.create_tables([Klasa, Uczen, Przedmiot, Ocena])  # tworzymy tabele

    dane = {
        Klasa: 'klasy',
        Uczen: 'uczniowie',
        Przedmiot: 'przedmioty',
        Ocena: 'oceny'
    }

    dodaj_dane(dane)
    
    baza.commit()
    baza.close()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
