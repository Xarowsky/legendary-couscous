/*
 * zlozonosc1.cpp
 * 
*/


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int n = 0;
    cout<<"podaj liczbe"<<endl;
    cin>>n;
    if (n == 1 )
        {   cout<<"1";
            return 0; }
    if ((n & 2) != 0) {
        while (n > 0) {
            cout<<n<<" ";
            n = n - 2;
        }
    }
    if ((n & 2) == 0) {
    n = n - 1;
    while (n > 0) {
            cout<<n<<" ";
            n = n - 2;
        }
    }
	return 0;
}

