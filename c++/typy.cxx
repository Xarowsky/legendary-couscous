/*
 * hellocpp.cxx
 */

#include <iostream> //biblioteki

using namespace std;

int main(int argc, char **argv)
{
    char imie[10]; //"char" deklaracja zmiennej znakowej //"[]" deklaracja tablicy znaków //
    //"char" typ znakowy
    int wiek = 0;//"int" typ całkowity integer
    //wiek = 0; inicjacja zmiennej
	cout << "hello c++" << endl; //cout print onscreen
    cout << "Podaj imię: ";
    //cin >> imie;
    cin.getline(imie, 10); //funkcje po .
    cout << "Cześć " << imie << endl;
    cout << "Ile masz lat?" << endl;
    cin >> wiek;
    cout << "rok urodzenia:" << 2017 - wiek << endl;
	return 0;
}
//zmiennna to nazwa której można przypisać dane lub je odczytać
