/*
 * sumuj.cpp
 */


#include <iostream>

using namespace std;
//iteracja powtarzanie czegoś.
int main(int argc, char **argv) {
    int suma=0;
    int liczba=0;
    // i-= dekrementacja zmniejszenie
    while(suma<=100) //pętla nieskończona
    {
    cout << "Podaj liczbe." << endl;
    cin >> liczba;
    //suma=suma+liczba;
    suma+=liczba;
}
cout << suma <<endl;
	return 0;
}
