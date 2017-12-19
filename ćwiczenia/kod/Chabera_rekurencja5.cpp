#include <iostream>


using namespace std;


int ciag(int a)
{
        if(a==0)
            return 0;
            
        return ciag(a-1)+1+(a-1)*2;
}
int main(int argc, char **argv)
{
        int a;
        cout << "ktory wyraz ciagu : ";
        cin >> a;
        cout << ciag(a);
        return 0;
}

