#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  baza.py
import csv
import sqlite3
import os.path
from modele import *


def czy_jest(plik):
    """F. sprawdza, czy plik istnieje na dysku"""
    if not os.path.isfile(plik):
        print("Plik {} nie istnieje!".format(plik))
        return False
    return True


def czytaj_dane(plik, separator=";"):
    dane = []  # pusta lista na rekordy
    
    if not czy_jest(plik):
        return dane
    
    with open(plik, 'r', newline='', encoding='utf-8') as plikcsv:
        tresc = csv.reader(plikcsv, delimiter=separator)
        for rekord in tresc:
            dane.append(tuple(rekord))
    return dane
    
    
def dodaj_dane(dane):
    
    for model, plik in dane.items():
        pola = [pole for pole in model._meta.fields]
        pola.pop(0)  # usuwamy pola id
        print(pola)
        
        wpisy = czytaj_dane(plik + '.csv', ';')
        model.insert_many(wpisy, fields=pola).execute()
    

def main(args):
    baza_plik = 'quiz.db'
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()
    baza.create_tables([Kategorie, Pytania, Odpowiedzi])  # tworzymy tabele

    dane = {
        Pytania: 'pytania',
        Kategorie: 'kategorie',
        Odpowiedzi: 'odpowiedzi'
    }

    dodaj_dane(dane)
    
    baza.commit()
    baza.close()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
