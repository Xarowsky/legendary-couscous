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
    start:cout << "podaj liczbe A: ";
    cin >> a;
    cout << "podaj liczbe B: ";
    cin >> b;
    cout << "podaj liczbe C: ";
    cin >> c;

     if (a>b && a>c)
    {
            cout << "najwieksze A = " << a;
            goto start;
    }
    if (b>a && b>c)
    {
        cout << "najwieksze B = " << b;
        return 0;
    }
    if (c>a && c>b)
    {
        cout << "najwieksze C = " << c;
        return 0;
    }
    if (b==a && c>a)
    {
    cout << "najwieksze C = " << c;
    return 0;
        }
    if (b==c && a>b)
    {
    cout << "najwieksze A = " << a;
    return 0;
    }
    if (c==a && b>a)
    {
    cout << "najwieksze B = " << b;
    return 0;
    }
    else //if (a==b)
    {
    cout << "A = B = C" << endl;
    cout << a << " = " << b << " = " << c << endl;
    }
	return 0;
}

