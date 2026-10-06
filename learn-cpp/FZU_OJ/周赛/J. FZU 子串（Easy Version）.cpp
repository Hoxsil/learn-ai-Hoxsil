#include <iostream>
using namespace std;
typedef long long ll;

int main()
{
    ll n;
    cin >> n;
    ll ans = 0;
    ll power = 3; //3^1
    ll L = 1;
    while(power < n - L + 1)
    {
        ans += power;
        L++;
        power *=3;
    }
    ll len = n - L + 1;
    ans += len * (len + 1)/2;
    cout << ans << endl;
    return 0;
}