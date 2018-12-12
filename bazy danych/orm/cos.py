#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  
import os
from peewee import *

baza_plik = 'test_orm.db'
baza = SqliteDatabase(baza_plik)

###############MODELE###############

class BazaModel(Model):
    class Meta:
        database = baza
        
class Klasa(BazaModel):
    nazwa = CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)
    
class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    
    
class Wynik(BazaModel):
    egzhum = FloatField(default=0)
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)
    uczen = ForeignKeyField(Uczen, related_name='wyniki')
    
###############MODELE###############

def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()
    baza.create_tables([Klasa, Uczen, Wynik])
    klasa2A.nazwa = '2A'
    klasa2A.roknaboru = 2011
    klasa2A.rokmatury = 2014
    klasa2A.save()
    klasa3A=Klasa((klasa='3A',roknaboru=2010,rokmatury=2013))
    klasa3A.save()
    ucz1 = Uczen(imie='adam',
                 nazwisko='słodowy',
                 plec=False
                 klasa=kl3A)
    ucz.save()
    ucz2 = Uczen(imie='ewa',
                 nazwisko='kolorowa',
                 plec=False
                 klasa=kl2A)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
