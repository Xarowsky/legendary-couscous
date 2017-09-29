#include <iostream>

using namespace std;

int main(int argc, char **argv) {
	
    int a=0;
    int b=0;
    char znak;
    cout << "podaj znak dzialania";
    cin >> znak;
    cout << "podaj dwie liczby" << endl;
    cin >> a >> b;
    if (znak == '+')
    {
    cout << a+b;
    }
    else if (znak == '-')
    {
    cout << a-b;
    }
    else if (znak == '*')
    {
    cout << a*b;
    }
    else if (znak == '/')
    {
    cout << a/b;
    }
	return 0;
}

