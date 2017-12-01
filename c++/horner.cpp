/*
* horner.cpp
 */


#include <iostream>

// W(x)= 2x^3+3x^2+5x+4
// W(x) = x(2x^2 + 3x + 5)
// W(x) = x( x(2x + 3) + 5) + 4

using namespace std;


float horner_it(int stopien, float a[], float x)
    {
       float wynik = a[0];
        for(int i = 0;i<stopien+1 ; i++)
        {
            wynik = 2 * x +a[i];
            
        }
        return wynik;
    }
    
    
int main(int argc, char **argv)
{
    float x = 0;
	float a[4];
    int stopien = 3;
    cout << "podaj x" << endl;
    cin >> x;
    for (int i = 0; i < 4; i++)
    {
        cout<<"podaj wspolczynnik nr. "<< i+1 >>endl;
        cin >> a[i];
    }
    cout<<"wartosc wielomianu = "<<horner_it<<endl;
	return 0;
}
