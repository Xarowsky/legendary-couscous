#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy_orm.py
import os
from uczniowie_model import *

def kw08():
    """ lista nazwisk uczniĂłw i nazw klas """
    query = (Uczen
        .select(Uczen.nazwisko, Uczen.klasa.klasa)
        .join(Klasa)
    )

    for obj in query:
        print(obj.nazwisko, obj.klasa.klasa)

def kw09():
    """ lista klas i iloĹÄ uczniĂłw """
    query = (Uczen
        .select(fn.Count(Uczen.id).alias('ilu'), Uczen.klasa.klasa)
        .join(Klasa)
        .group_by(Klasa)
        .order_by(SQL('ilu').asc())
    )

    for obj in query:
        print(obj.klasa.klasa, obj.ilu)

def kw10():
    """ lista przedmiotĂłw i iloĹÄ ocen """
    query = (Ocena
        .select(fn.Count(Ocena.id).alias('ile'), Ocena.przedmiot.przedmiot)
        .join(Przedmiot)
        .group_by(Przedmiot)
        .order_by(SQL('ile').asc())
    )

    for obj in query:
        print(obj.przedmiot.przedmiot, obj.ile)

def kw11():
    """ Po ile ocen majÄ uczniowie """
    query = (Ocena
        .select(Ocena.uczen.nazwisko, fn.COUNT(Ocena.id).alias('ile'))
        .join(Uczen)
        .group_by(Ocena.uczen.nazwisko)
        .order_by(SQL('ile').asc())
    )
    for obj in query:
        print(obj.uczen.nazwisko, obj.ile)


def kw12():
    """ Ĺrednie ocen poszczegĂłlnych uczniĂłw """
    query = (Ocena
        .select(Ocena.uczen.nazwisko, fn.AVG(Ocena.ocena).alias('srednia'))
        .join(Uczen)
        .group_by(Ocena.uczen.nazwisko)
        .order_by(SQL('srednia').asc())
    )
    for obj in query:
        print(obj.uczen.nazwisko, round(obj.srednia, 2))

def kw13():
    """ Ĺrednie ocen ucznia Szymczak z poszczegĂłlnych przedmiotĂłw """
    
    query = (Ocena
        .select(Ocena.uczen.nazwisko, Ocena.przedmiot.przedmiot, fn.AVG(Ocena.ocena).alias('srednia'))
        .join(Uczen)
        .join_from(Ocena, Przedmiot)
        .where(Ocena.uczen.nazwisko == 'Szymczak')
        .group_by(Ocena.przedmiot.przedmiot)
        .order_by(SQL('srednia').asc())
    )
    for obj in query:
        print(obj.uczen.nazwisko, obj.przedmiot.przedmiot, round(obj.srednia, 2))

def kw14():
    """ilu uczniĂłw ma ĹredniÄ powyĹźej 3.5 z WF?"""
    query = (Ocena
        .select(Ocena.uczen.nazwisko, fn.AVG(Ocena.ocena).alias('srednia'))
        .join(Uczen)
        .join_from(Ocena, Przedmiot)
        .where(Ocena.przedmiot.przedmiot == WF)
        .group_by(Ocena.uczen.nazwisko)
    )
    for obj in query:
        print(obj.uczen.nazwisko, round(obj.srednia, 2))


def main(args):
    baza.connect()  # poĹÄczenie z bazÄ

    kw14()

    kwerendy = [
        "Uczen.select()",
        "Uczen.select().where(Uczen.imie=='RafaĹ')",
        "Uczen.select().where(Uczen.imie.startswith('G'))",
        "Uczen.select().where(Uczen.egz_mat.between(20, 40))",
        "Uczen.select().where((Uczen.nazwisko=='Piasecki') & (Uczen.imie=='RafaĹ'))",
        "Uczen.select().order_by(Uczen.egz_mat.asc())",
        "Uczen.select().where(Uczen.plec==1).order_by(Uczen.egz_mat.asc())",
    ]
    
    #for obj in eval(kwerendy[6]):
    #    print(obj.nazwisko, obj.imie, obj.egz_mat)
    
    baza.commit()
    baza.close()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
