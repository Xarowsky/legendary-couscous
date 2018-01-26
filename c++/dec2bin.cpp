#include <iostream>

using namespace std;

int main(int argc, char **argv) {
	int liczba = 120;
    int podstawa = 2;
    int tab[16];
    int i = 0;
    char znaka = 'A';
    char znakb = 'B';
    cout<<"podaj liczbe"<<endl;
    cin>>liczba;
    cout<<"podaj podstawe (1-9)"<<endl;
    cin>>podstawa;
    cout<<(int)znaka<<" "<<(int)znakb<<endl;
    do {
        tab[i] = liczba % podstawa; 
        liczba = liczba / podstawa;
        i++;
    } while(liczba > 0);
    
    i--;
    
    while(i >= 0) {
        cout<<tab[i]<<" ";
        i--;
    }
	return 0;
}
