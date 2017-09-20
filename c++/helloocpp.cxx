/*
 * hellocpp.cxx
 */


#include <iostream>
//biblioteki
using namespace std;
//koniec bibliotek
int main(int argc, char **argv)
{
    char imie[10]; //deklaracja zmiennej znakowej //[] deklaracja tablicy znaków
    
	cout << "hello c++" << endl; //cout print onscreen
    cout << "Podaj imię:";
    //cin >> imie;
    cin.getline(imie, 10) >> imie; //funkcje po .
    cout << "Cześć " << imie << endl;
	return 0;
}
//zmiennna to nazwa której można przypisać dane lub je odczytać
