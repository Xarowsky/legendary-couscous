/*
 * hellocpp.cxx
 */

#include <iostream> //biblioteki
#include <math.h>

using namespace std;

int main(int argc, char **argv)
{
    int bok = 0;
    cout << "Podaj długość boku kwadratu: ";
    cin >> bok;
    cout << "obwód: " << 4*bok << endl << "pole: " << bok * bok;
	return 0;
}
//zmiennna to nazwa której można przypisać dane lub je odczytać
