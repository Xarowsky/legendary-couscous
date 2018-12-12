#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


import sqlite3


def kwerenda1(cur):
    
    cur.execute("""
    SELECT przedmiot, klasa, AVG(ocena) AS srednia FROM przedmioty
    INNER JOIN klasy ON klasy.id=uczniowie.id_klasa
    INNER JOIN uczniowie ON uczniowie.id=oceny.id_uczen
    INNER JOIN oceny ON przedmioty.id=oceny.id_przedmiot
    WHERE przedmiot='matematyka'
    GROUP BY id_klasa
    ORDER BY srednia DESC
    """)
    for row in cur.fetchall():
        print(tuple(row))

# SELECT przedmiot, AVG(ocena) AS srednia FROM przedmioty
#INNER JOIN oceny ON przedmioty.id=oceny.id_przedmiot
#GROUP BY id_przedmiot
#ORDER BY srednia DESC
#SELECT klasa, AVG(ocena) AS srednia FROM oceny
#INNER JOIN uczniowie ON uczniowie.id=oceny.id_uczen

def main(args):
    
    #######config#######    
    baza = 'uczniowie'
    roz = '.txt'
    naglowki = True
    #######config#######
       
    con = sqlite3.connect(baza + '.db')
    cur = con.cursor()
    
    kwerenda1(cur)
    
    con.commit()
    con.close()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
