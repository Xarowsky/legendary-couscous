#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  klasa_uczen.py
import os
from peewee import *
from uczniowie_model import *
from baza import czy_jest
from baza import czytaj_dane

def dodaj_dane(dane):
    for model, plik in dane.items():
        pola = [pole for pole in model._meta.fields]
        pola.pop(0)
        print(pola)
        
        wpisy = czytaj_dane(plik + '.csv')
        model.insert_many(wpisy, fields=pola).execute()
        

def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()  # połączenie z baza
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
