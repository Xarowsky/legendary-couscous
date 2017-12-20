#include <iostream>

using namespace std;


void wypelnij(int t[], int n, int n) {
    srand(time(null));
    for(int i = 0; i < n; i++) {
         t[i] = 1 +rand() % m; //losowanie liczb całkowitych z zakresu <0;m>
         }
    }


void drukuj (int t[], int n) {
    cout << t[i] << " ";
    }


void zamien(int &i int &k) {
    int tmp = a;
    a = b;
    b = tmp;
    }


void sort_wyb(int t[], int n[]) {
    int k;
    for(int i = 0 ; i < n ; i++) {
        k = i;
        for ( int j = i + 1; j < n)
          if (t[j] <  t[k]) {
            k = j;
            }
        zamien(t[i], t[k])
        }
    }
    

int main(int argc, char **argv) {
    const int ile = 10;
    int tab[ile];
    wypelnij(tab[], ile, 20);
    drukuj(tab, ile);
    
    
	return 0;
}

