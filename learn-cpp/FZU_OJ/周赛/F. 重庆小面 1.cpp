#include <iostream>
using namespace std;


int a, b, c, d, e;

void init(){
    cin >> a >> b >> c >> d >> e;
    return;
}

int main(){
    init();
    cout << min(min(a+d, b+c), e);
    return 0;
}