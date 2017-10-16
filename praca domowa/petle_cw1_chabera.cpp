/*
zadanie1.cpp
*/

#include <iostream>
#include <math.h>

using namespace std;

main(int argc, char**argv)
{
int a= -1;

while (a<0){
    cout << "podaj liczbe dodatnia liczbe A: ";
    cin >> a;

}

cout << "Pierwiastek liczby A =" <<sqrt(a)<<endl;
cout << "kwadrat liczby A =" << a*a;



return 0;
}
