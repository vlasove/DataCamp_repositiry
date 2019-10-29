#include <iostream>

using namespace std;

int main(){

    int a1,b1,a2,b2;

    cin>>a1>>b1>>a2>>b2;

    if(((a1 -a2 ==1 || a1 - a2 == -1 )&& (b1 - b2 == 2 || b1 - b2 == -2)) || ((a1 -a2 ==2 || a1 - a2 == -2 )&& (b1 - b2 == 1 || b1 - b2 == -1)) ){
        cout<<"YES"<<endl;
    }else{
        cout<<"NO"<<endl;
    }


    return 0;
}