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
    cout << "podaj liczbe A: ";
    cin >> a;
    cout << "podaj liczbe B: ";
    cin >> b;
    cout << "podaj liczbe C: ";
    cin >> c;

    if (a>b)
    {
        if (a>c)
            cout << "najwieksze A = " << a;
                else
                cout << "njwieksze C =" << c;
    }
    else if (a<b)
    {
        if (b>c)
        cout << "najwieksze B = " << b;
            else
            cout << "najwieksze C = " << c;
    }
    else if (c>a)
    {
        if (c>b)
        cout << "najwieksze C = " << c;
            else
            cout << "najwieksze B = " << c;
    }
    else //if (a==b)
    {
    cout << "A = B = C" << endl;
    cout << a << " = " << b << " = " << c << endl;
    }
	return 0;
}

