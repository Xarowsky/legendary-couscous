/*
zadanie2.cpp
*/

#include <iostream>
#include <math.h>

using namespace std;

main(int argc, char**argv)
{
int a=1;
int b=0;
int c=0;
int p=0;
int pa=0;
int pb=0;
int pc=0;


int pole=0;

while (a+b<c||a+c<b||b+c<a)
{
    cout << "podaj pierwszy bok trojkata= ";
    cin >> a;
    cout << "podaj drogi krotszy bok trojkata= ";
    cin >> b;
    cout << "podaj trzeci bok trojkata= ";
    cin >> c;
}

p=a+b+c/2;
pa=p-a;
pb=p-b;
pc=p-c;
pole=p*pa*pb*pc;
pole=sqrt(pole);

cout << "pole trojkata= " << pole;


return 0;
}
