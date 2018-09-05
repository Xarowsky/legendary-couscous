#include <iostream>

using namespace std;

int main(int argc, char **argv)
{

char zn='t';


while(true)
{
cout<<"podaj znak =";
cin>>zn;
    //if (zn=='n'||zn=='N'||zn=='t'||zn=='T'){cout<<zn<<endl;}
    //else break;
switch(zn){
    case 'n':
    case 'N':
    case 't':
    case 'T':
    goto koniec;
    }
}
	koniec:return 0;
}

