/*
zadanie5.cpp
*/

#include <iostream>
#include <math.h>

using namespace std;

main(int argc, char**argv)
{
int x=0;
int suma=0;
cout<<"podaj liczbe ";
cin>>x;
petla:while (x!=0)
{
    suma=x%10+suma;
    x=x/10;
}
cout <<"suma cyfr liczby wynosi "<<suma<<endl;
if(suma>=10)
{
x=suma;
suma=0;
goto petla;
}
else
{
return 0;
}
}
