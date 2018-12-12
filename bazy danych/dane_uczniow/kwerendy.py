#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


import sqlite3


def kwerenda1(cur):
    
    cur.execute("""SELECT * FROM nazwiska INNER JOIN dane_osobowe ON nazwiska.nr_ucznia
        WHERE miesiac>6 and miesiac<9''
    """)
    for row in cur.fetchall():
        print(tuple(row))

#"""SELECT * FROM nazwiska WHERE nazwisko LIKE 'G%'

def main(args):
    #config####################
    
    baza = 'uczniowie'
    tabele = ['nazwiska', 'dane_osobowe', 'oceny' ]
    roz = '.txt'
    naglowki = True
    
    
    #############################
    
    con = sqlite3.connect(baza + '.db')
    cur = con.cursor()
    
    kwerenda1(cur)
    
    con.commit()
    con.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
