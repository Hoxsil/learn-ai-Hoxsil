#include <iostream>
using namespace std;


const int MOD = 998244353;
int n;
string s;
long long dp[6];
char c[6]={'E', 'l', 'y', 's', 'i', 'a'};


void init(){
    cin >> n >> s;
    return;
}

int main(){
    init();
    for (char a:s){
        if (a == 'E') dp[0]++;
        for (int i=1;i < 6;i++)
            if (a == c[i]) dp[i] = (dp[i] + dp[i-1]) % MOD;
    }
    cout << dp[5] << endl;
    cin >> n;
    return 0;
}