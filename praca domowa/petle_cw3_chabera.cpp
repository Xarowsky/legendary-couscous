/*
zadanie3.cpp
*/

#include <iostream>
#include <math.h>

using namespace std;

main(int argc, char**argv)
{
int i=0;
cout<<"podaj liczbe ";
cin >> i;
if (i<0)
{
for(i=i;i<=0;i++)
return 0;
}
else if(i>15)
{
for (i=i;i>15;i--)
return 1;
}
else return 2;
}
