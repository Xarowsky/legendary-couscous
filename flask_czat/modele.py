#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  modele.py

from peewee import *

baza = SqliteDatabase('quiz.db')


class BaseModel(Model):
    class Meta:
        database = baza


class Kategorie(BaseModel):
    kategoria = CharField()
    

class Pytania(BaseModel):
    pytanie = CharField()
    id_kat = ForeignKeyField(Kategorie, related_name='id')
    

class Odpowiedzi(BaseModel):
    id_p = ForeignKeyField(Pytania, related_name='id')
    odpowiedz = CharField()
    odpok = BooleanField()



if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
