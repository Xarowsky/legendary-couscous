#include <iostream>

using namespace std;

int main(int argc, char **argv)
{

int m=0;


while(m<1||m>12)
{
cout<<"podaj miesiac (1-12) ="<<endl;
cin>>m;
}
cout<<"Miesiac: "<<m<<endl;

switch(m)
{
    case 1;
        cout<<"styczen";
    break;}

switch(m)
{
    case 2;
        cout<<"luty";
    break;
}

switch(m){
    case 3;
        cout<<"marzec";
    break;
}

switch(m)
{
    case 4;
        cout<<"kwiecien";
    break;
}

switch(m)
{
case 5;
    cout<<"lipiec";
break;
}

switch(m)
{
    case 6;
        cout<<"czerwiec";
    break;
}

	return 0;
}

