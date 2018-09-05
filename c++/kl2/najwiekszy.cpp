/*
 * największa.cpp
 * pobierz dwie liczby całkowite i wybierz wieksza
 */
#include <iostream>

using namespace std;

int main(int argc, char **argv) {
	int a, b;
    a = 0;
    b = 0;
    cout << "podaj liczbę A: ";
    cin >> a;
    cout << "podaj liczbę B: ";
    cin >> b;
    
    if (a>b)
    {
    cout << "większe A = ";
    cout << a;
    }
    else if (a<b)
    {
    cout << "większe B = ";
    cout << b;
    }
    else //if (a==b)
    {
    cout << "A = B" << endl;
    cout << a << "=" << b << endl;
    }
	return 0;
}

