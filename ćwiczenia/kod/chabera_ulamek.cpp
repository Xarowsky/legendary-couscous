#include <iostream>

using namespace std;

int euklides(int a,int b){
    int tmp = 0;
    while (b!=0){
    tmp = a % b;
    a = b;
    b =tmp;
    }
    return a;
}


int main(int argc, char **argv) {
	int a = 0;
    int b = 0;
    int nwd = 0;
    cout<<"licznik"<<endl;
    cin>>a;
    cout<<"mianownik"<<endl;
    cin>>b;
    nwd = euklides(a,b);
    cout<<a/nwd<<"/"<<b/nwd<<endl;
	return 0;
}

