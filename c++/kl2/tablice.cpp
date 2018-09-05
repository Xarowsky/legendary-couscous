#include <iostream>

using namespace std;

int sumuj(int tab[])
{
    int suma=0;
    int i=0
    for(i=0;i<5;i++)
    {
        cout<<"podana liczba nr."<<i<<"="<<tab[i]<<endl;
        suma=suma+tabela[i];
        }
    return suma;
    }

void pobierzdane(int tab[],int ile)
{
    int i;
    cout <<"podaj " <<ile<<" liczb:"<<endl;
    for(i=0;i<ile;i++) {cin>>tab[i];}
    }
int main(int argc, char **argv)
{
const int rozmiar=5;
float srednia=0;
int suma = 0;
int tabela[5];

pobierzdane(tabela,rozmiar);
    
sumuj(tabela);

    srednia=float(suma)/float(5);
    cout<<"suma "<<suma<<endl;
    cout<<"srednia  "<<srednia;
	return 0;
    }
