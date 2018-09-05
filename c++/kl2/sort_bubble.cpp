#include <iostream>
#include <cstdlib> // zawiera srand i rand
#include <ctime> // zawiera time
#include <cstddef> // zawiera NULL


using namespace std;


void zamien(int &a, int &b) {
    int tmp = a;
    a = b;
    b = tmp;
    }


void wypelnij(int t[], int n) {
    srand(time(NULL));
    for(int i = 0; i < n; i++) {
         t[i] = 1 + rand() % 10; //losowanie liczb całkowitych z zakresu <0;10>
         }
    }


void sort_bubble(int t[], int n) {
    for (int i = 0;i < n;i++ ) {
        for(int j = i;j < n - i - 1; j++) {
            if (t[j] > t[j+1])
                zamien(t[j], t[j+1])
        }
    }
}


int main(int argc, char **argv) {
 const int ile = 10;
    int tab[ile];
    wypelnij(tab, ile);
	return 0;
}

