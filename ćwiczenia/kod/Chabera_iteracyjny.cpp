#include <iostream>

using namespace std;

void iloczyn(int n) {
    int a = 0;
    int i = 0;
    int wynik = 1;
    int p = 0;
    while (i != n) {
    cout<<"podaj liczbe a"<<endl;
    cin>>a;
    wynik = wynik * a;
    cout<<wynik<<endl;
        if (p % 2 == 0)
        {p++;}
    i++;}
    cout<<"parzyste "<<p;
}




int main(int argc, char **argv) {
	int n = 0;
    cout<<"podaj liczbe n"<<endl;
    cin>>n;
    iloczyn(n);
	return 0;
}

