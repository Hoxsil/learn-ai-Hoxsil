#include <iostream>
using namespace std;
int main(){
    int n, x, min_num=10005, a;
    long long sum;
    cin >> n >> x;
    sum = x;
    for (int i=1;i <= n;i++){
        cin >> a;
        sum += a;
        if (a < min_num) min_num = a;
    }
    cout << (sum-min_num) % 998244353 * min_num << endl;
    return 0;
}