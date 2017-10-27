/*
 * teksty.cpp
*/

#include <iostream>

using namespace std;

int main(int argc, char **argv) {
    char osoba[25];
    int i=0;
    
    cout<<"jak ssię nazywasz?"<<endl;
    //cin>>osoba;
    cin.getline(osoba, 25);
    cout<<"hej,"<<osoba<<"!"<<endl;
    //~for(i=65;i<91;i++){cout<<i<<" "<<char(i)<<endl;}
    //~cout<<endl;
    //~for(i=97;i<122;i++){cout<<i<<" "<<char(i)<<endl;}

    	return 0;\
    /*00001010-ASCII "10" Line Feed koniec wiersza linux
     * 00001101- ASCII "13" Carriage return koniec lini windows
     * 00100000- ASlCII 
     */
}
