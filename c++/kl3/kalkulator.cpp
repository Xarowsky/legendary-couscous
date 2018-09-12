#include <iostream>

using namespace std;

float dodawanie (float a ,float b) {
    return a + b;
}

float odejmowanie (float a ,float b) {
    return a - b;
}

float dzielenie (float a ,float b) {
    return a / b;
}

float mnozenie (float a , float b) {
    return a * b;
}

int main(int argc, char **argv) {
	int a = 0;
    int b = 0;
    int c = 0;
    cout << "lista dzialan "<< endl;
    cout << "1. dodawanie (a+b)"<< endl;
	cout << "2. odejmowanie (a-b)"<< endl;
	cout << "3. mnozenie (a*b)"<< endl;
	cout << "4. dzielenie (a/b)"<< endl;
    cout << "podaj liczbe a "<< endl;
    cin >> a;
    cout << "podaj liczbe b "<< endl;
    cin >> b;
    cout << "wybierz dzialanie (1-4) "<< endl;
    cin >> c;
    if (c == 1) cout << dodawanie(a,b);
    else if (c == 2) cout << odejmowanie(a,b);
    else if (c == 3) cout << mnozenie(a,b);
    else if (c == 4) cout << dzielenie(a,b);
    else cout << "blad 404 dzialanie nie znalezione";
	return 0;
}

