/*
 * funkcje.cpp
 */


#include <iostream>

using namespace std;

void iloczyn(int a, int b)
{
    cout<<"iloczyn= "<<a*b;
}

int iloraz(int a,int b)
{
    if(b!=0)
    {return a/b;}
    else
    cout<<"dzielnik= 0";
    return 0;
}

void dodaj(int a, int b)
{
    cout<<"suma= "<<a+b<<endl;
}
int odejmij(int l1,int l2)
{
    return l1-l2;
}

int main(int argc, char **argv)
{
    int a, b;
    a=b=0;
    cout<<"podaj 2 liczby: ";
    cin>>a>>b;
    
    dodaj(a, b);
    cout<<"Różnica= "<<odejmij(a,b)<<endl;
    cout<<"iloraz= "<<iloraz(a,b)<<endl;
    iloczyn(a,b);
    cout<<endl;
    return 0;
}
