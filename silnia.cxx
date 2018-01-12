/*
 * silnia.cxx
*/


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int i, n, silnia;
    
    cout<<"podaj argument "/*n*/;
    cin >> n;
    n= n + 1;
    silnia = 1;
    i = 1;
    do {
        silnia *= i;
        i++;
     } while (i < n);
     
     cout<<endl<<n - 1<<"! ="<< silnia << endl;
     
	return 0;
}

