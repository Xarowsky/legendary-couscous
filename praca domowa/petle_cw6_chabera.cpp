/*
zadanie5.cpp
*/

#include <iostream>
#include <math.h>

using namespace std;

main(int argc, char**argv)
{
int a = 0;
int b =0;
int c=0;
int d=0;
int i;
cout<<"podaj dzielna= ";
cin>>a;
cout<<"podaj dzielnik= ";
cin>>b;

if (a%b==0)
{
    c=b;
    for (i=1;b<a;i++){b=b+c;}
}
if(a%b!=0)
{
d=a%b;
a=a-d;
c=b;
for(i=1;b<a;i++)
{b=b+c;}
}
cout<<"iloraz wynosi= "<<i<<endl;
cout<<"reszta wynosi= "<<d;
return 0;
}
/*
zadanie5.cpp
*/

#include <iostream>
#include <math.h>

using namespace std;

main(int argc, char**argv)
{
int a = 0;
int b =0;
int c=0;
int d=0;
int i;
cout<<"podaj dzielna= ";
cin>>a;
cout<<"podaj dzielnik= ";
cin>>b;

if (a%b==0)
{
    c=b;
    for (i=1;b<a;i++){b=b+c;}
}
if(a%b!=0)
{
d=a%b;
a=a-d;
c=b;
for(i=1;b<a;i++)
{b=b+c;}
}
cout<<"iloraz wynosi= "<<i<<endl;
cout<<"reszta wynosi= "<<d;
return 0;
}
