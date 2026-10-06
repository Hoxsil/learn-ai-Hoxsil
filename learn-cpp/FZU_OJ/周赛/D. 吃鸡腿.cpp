#include <iostream>
using namespace std;

int main(){
    int n, num = 1;
    cin >> n;
    while (true) {
        if (num % 2 == 1)
            n -= 6;
        else
            n -= 4;
        if (n < 0){
            cout << num-1;
            break;
        }
        num++;
    }
    cin >> n;
    return 0;
}