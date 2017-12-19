#include <iostream>

using namespace std;


int ciag(int n) {
    if(n < 1) {
        return 0;
        }
    return ciag(n-1) + 2 * n + ciag(n-2);
    }


int main(int argc, char **argv) {
    int n = 0; 
	cout <<" ktory wyraz ";
    cin >> n;
    cout << ciag(n);
	return 0;
}

