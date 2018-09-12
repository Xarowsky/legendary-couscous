#include <iostream>

using namespace std;

int main(int argc, char **argv) {
    char n = 't';
    float m = 0;
    float height = 0;
    //if (n = 't') {
	cout << "podaj swoja mase (kg): ";
    cin >> m;
	cout << "podaj swoj wzrost (m): ";
    cin >> height;
    height = height * height;
	float bmi= m/height;
    if (bmi > 25) {
    cout << "overweight ";
    cout << bmi ;
    }
    else if (bmi < 18.5) {
        cout << "underweight ";
        cout << bmi;
    }
    else {
        cout << "ok ";
        cout << bmi;
    }
    cout << "przeprowdzic test jeszcze raz? (t/n)";
    if (n =! 'n' && n=! 't') {
    cout << "blad (prawidlowe wartosci t/n) ";
    cin >> n ;
    }
    //}
	return 0;
}

