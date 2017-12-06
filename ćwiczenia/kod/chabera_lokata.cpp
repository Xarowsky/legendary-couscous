#include <iostream>

using namespace std;

void bank(int t){
    int i = 0;
    int bnk = 100;
    int wpl = 110;
     while(i!=t){
        bnk = bnk + wpl;
        wpl = wpl + 10;
        i++;
    }
    cout<<"stan konta wynosi "<<bnk<<endl;
    cout<<"ostatnia wplata wynosi "<<wpl<<endl;
    
    
    
    
}

int main(int argc, char **argv) {
	int t = 0;
    cout<<"ile miesięcy"<<endl;
    cin>>t;
    bank(t);
	return 0;
}

