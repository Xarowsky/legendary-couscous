/*
 * silnia.cpp
 */


#include <iostream>
#include <math.h>
using namespace std;

int silnia(int num1)
{
    int i;
    int wynik = 1;
    for (i = 2;i<=num1;i++) {wynik = wynik * i;}
    return wynik;
}


int main(int argc, char **argv)
{
    int a, b;
    a=b=0;
    cout<<"podaj 1 liczbe: ";
    cin>>a;
    cout<<"silnia wynosi: "<<silnia(a)<<endl;
    return 0;
}
