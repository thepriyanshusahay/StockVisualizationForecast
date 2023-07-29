#include<bits/stdc++.h>
#include<map>
using namespace std;

string read(int n, vector<int> book, int target)
{
    int val = 0;
    map<int, int> p;
    for(int i:book){
        if(target >= i){
            p[i] = target-i;
        }
        else{
            p[i] = i-target;
        }
    }
    for(auto i:p){
        // int a = i.second;
        // if(p.find(a) != p.end()){
        //     return "YES";
        // }
        cout << i.first << " " << i.second << endl;
    }
    return "NO";
}

int main(){

    vector<int> a = {1,2};
    cout << read(2,a,1) << endl;
    return 0;
}