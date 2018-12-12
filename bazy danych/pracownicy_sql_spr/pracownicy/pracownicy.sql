DROP TABLE IF EXISTS kontakty;
--id_pracownika, typ_k, kontakt, uwagi
CREATE TABLE kontakty (
id_pracownika INTEGER PRIMARY KEY,
typ_k TEXT(11),
kontakt TEXT(20),
uwagi TEXT(100)
);

DROP TABLE IF EXISTS place;
--id_p, id_s, placa, data_z
CREATE TABLE place (
id_p INTEGER,
id_s INTEGER,
placa INTEGER,
data_z DATE,
FOREIGN KEY (id_p) REFERENCES kontakty(id_pracownika),
FOREIGN KEY (id_s) REFERENCES stanowiska(id_s)
);

DROP TABLE IF EXISTS pracownicy;
--imie, nazwisko, kod, miasto_z, ulica, data_u, miasto_u
CREATE TABLE pracownicy (
imie TEXT(20),
nazwisko TEXT(20),
kod INTEGER,
miasto_z TEXT(20),
ulica TEXT(20),
data_u DATE,
misto_u TEXT(20),
id_p INTEGER,
FOREIGN KEY (id_p) REFERENCES kontakty(id_pracownika)
);

DROP TABLE IF EXISTS stanowiska;
--stanowisko, id_s
CREATE TABLE stanowiska (
stanowiska TEXT(20),
id_s INTEGER
);

--INSERT INTO kontakty(nr_ucznia, nazwisko, imie1, imie2)
--VALUES (9201, "Adamczuk", "Agata", "");
--INSERT INTO kontakty
--VALUES (9802, "Adamiuk", "Marta", "");

--    nr_ucznia INTEGER,
--    dzien INTEGER,
--    miesiac INTEGER,
--    rok INTEGER,
--    miejsce_urodz TEXT(20) DEFAULT "Gdańsku",
--    wojewodztwo TEXT(25) DEFAULT "pomorskie",
--    FOREIGN KEY (nr_ucznia) REFERENCES kontakty(nr_ucznia)

--  nr_ucznia INTEGER PRIMARY KEY NOT NULL,
--    nazwisko TEXT(20) NOT NULL,
--    imie1 TEXT(20),
--    imie2 TEXT(20)

--      nr_ucznia INTEGER,
--    zach TEXT(10),
--    rel DECIMAL DEFAULT NULL,
--    pol DECIMAL,
--    ang DECIMAL,
--   niem DECIMAL,
--    mat DECIMAL,
--    his DECIMAL,
--    geo DECIMAL,
--    bio DECIMAL,
--    fiz DECIMAL,
--    che DECIMAL,
--    tech DECIMAL,
--   info DECIMAL DEFAULT NULL,
--    pla DECIMAL,
--    po DECIMAL,
--    wf DECIMAL DEFAULT NULL,
--    FOREIGN KEY (nr_ucznia) REFERENCES kontakty(nr_ucznia)

-- sqlite3 baza.db < szkola.sql
-- sqlite3 baza.db
-- .table
-- .schema
-- .quit
