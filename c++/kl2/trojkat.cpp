/*program pobiera trzy boki trójkat spradza czy da się z nich zbudować trojkat
 * oblicza obwod i pole (wzor herona)
 * 
*/
#include <iostream>
#include <cmath>
using namespace std;

int main(int argc, char **argv) {
    float a, b, c;
    
    a=0;
    b=0;
    c=0;
    cout << "podaj dlugosc boku a= ";
    cin >> a;
    cout << "podaj dlugosc boku b= ";
    cin >> b;
    cout << "podaj dlugosc boku c= ";
    cin >> c;
    float obwod = a + b + c;
    if (a+b>c && c+b>a && a+c>b)
    {
    cout << "obwod= " << a + b + c << endl;
    float p = obwod / 2;
    cout << "p= " << p;
    
    }
	return 0;
}

