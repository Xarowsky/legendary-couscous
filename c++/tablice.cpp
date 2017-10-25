#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
const int rozmiar=5;
int srednia=0;
int suma = 0;
int i = 0;
int tabela[5];
cout<<"podaj pięć liczb: ";

for(i=0;i<5;i++)
    {cin>>tabela[i];}
    
for(i=0;i<5;i++)
    {
        cout<<"podana liczba nr."<<i<<"="<<tabela[i]<<endl;
        suma=suma+tabela[i];
        }
    srednia=float(suma)/float(5);
    cout<<"suma "<<suma<<endl;
    cout<<"srednia  "<<srednia;
	return 0;
    }
