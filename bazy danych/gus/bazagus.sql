-- bazagus.sql
DROP TABLE IF EXISTS miasta;
DROP TABLE IF EXISTS dane_demograficzne;
DROP TABLE IF EXISTS powierzchnia_miasta;

CREATE TABLE miasta (
    id_miasta INTEGER PRIMARY KEY , 
    nazwa_miasta TEXT(30),
    wojewodztwo TEXT(30)
);

CREATE TABLE dane_demograficzne (
    id INTEGER,
    id_miasta INTEGER,
    liczba_mieszkancow INTEGER,
    liczba_kobiet INTEGER,
    grupa_wiekowa TEXT(15),
    data_aktualizacji DATE,
    FOREIGN KEY (id_miasta) REFERENCES miasta(id_miasta)
);
CREATE TABLE powierzchnia_miasta (
    id INTEGER,
    pow_miasta INTEGER,
    pow_t_z INTEGER,
    dat_akt DATE,
    id_miasta INTEGER,
    FOREIGN KEY (id_miasta) REFERENCES miasta(id_miasta)
);
-- sqlite3 baza.db < bazagus.sql
-- sqlite3 baza.db
-- sqlite> .table
-- sqlite> .schema
-- sqlite> .quit
