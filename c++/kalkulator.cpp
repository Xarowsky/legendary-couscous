#include <iostream>

using namespace std;

int main(int argc, char **argv) {
	
    float a=0;
    float b=0;
    char znak;
    cout << "podaj znak dzialania ";
    cin >> znak;
    cout << "podaj dwie liczby " << endl;
    cin >> a >> b;
    
    if (znak == '+')
    {cout << "wynik= " << a+b;}
    
    else if (znak == '-')
    {cout << "wynik= " << a-b;}
    
    else if (znak == '*')
    {cout << "wynik= " << a*b;}
    
    else if (znak == '/')
    {cout << "wynik= " << a/b;}
    
    else
    {cout << endl << "Niepoprawny znak działania.";}
	return 0;
}

