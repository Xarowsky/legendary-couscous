#include <iostream>

using namespace std;
//iteracja powtarzanie czegoś.
int main(int argc, char **argv) {
    int i;
    // i-= dekrementacja zmniejszenie
    for (i = 0; i <101; i++) // inkrementacja zwiększenie
    {
    if (i % 10 == 0 )
        cout << i << endl;
    // cout << '*' <<endl;
    }
	return 0;
}

