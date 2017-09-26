/*
 * największa.cpp
 * pobierz trzy liczby całkowite i wybierz wieksza
 */
#include <iostream>

using namespace std;

int main(int argc, char **argv) {
	int a, b, c;
    a = 0;
    b = 0;
    c = 0;
    cout << "podaj liczbę A: ";
    cin >> a;
    cout << "podaj liczbę B: ";
    cin >> b;
    cout << "podaj liczbę C: ";
    cin >> c;
    
    if (a>b)
    {
        if (a>c)
            cout << "największe A = " << a;
    }
    else if (a<b)
    {
        if (b>c)
        cout << "największe B = " << b;
    }
    else if (c>a)
    {
        if (c>b)
        cout << "największe C = " << c;
    }
    else //if (a==b)
    {
    cout << "A = B = C" << endl;
    cout << a << " = " << b << " = " << c << endl;
    }
	return 0;
}

