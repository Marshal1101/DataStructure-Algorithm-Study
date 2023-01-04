#include <iostream>
#include <vector>
using namespace std;

int num1[10001] = {0,}, num2[10001] = {0,};
vector<int> v;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    string a="", b="", temp = "";
    int c = 0;
    cin >> a >> b;
    if(a.size()<b.size()){ // 긴 문자열을 a에 저장
        temp = a;
        a = b;
        b = temp;
    }
    for(int i=0; i<a.size(); i++) num1[i+1] = a[i]-'0';
    for(int i=0; i<b.size(); i++) num2[i+1+a.size()-b.size()] = b[i]-'0';
    for(int i=a.size(); i>0; i--){
        c = num1[i]+num2[i];
        if(c>=10){
            num1[i-1]++;
            c-=10;
        }
        v.push_back(c);
    }
    if(num1[0]!=0) v.push_back(1);
    for(int i=v.size()-1; i>=0; i--) cout << v[i];
    return 0;
}