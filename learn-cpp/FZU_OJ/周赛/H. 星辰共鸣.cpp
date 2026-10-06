#include <iostream>
using namespace std;


int n;
long long num[1005];
long long last_num;
const int MOD = 1000000007;

void init(){
    cin >> n;
    for (int i=1;i <= n;i++)
        cin >> num[i];
    return;
}

long long gcd(long long a,long long b){
    while (b){
        long long t = a % b;
        a = b;
        b = t;
    }
    return a;
}

long long lcm(long long x,long long y){
    return x / gcd(x,y) * y;
}

long long star_num(long long a, long long b, long long c){
    return lcm(lcm(a,b),c) / gcd(gcd(a,b),c) % MOD;
}

int main(){
    init();
    for (int i=1;i <= n-2;i++)
        for (int j=i+1;j <= n-1;j++)
            for (int k=j+1;k <= n;k++){
                if (last_num == 0)
                    last_num = star_num(num[i], num[j], num[k]);
                else
                    last_num = last_num * star_num(num[i], num[j], num[k]) % MOD;
            }
    cout << last_num;
    cin >> n;
    return 0;
}