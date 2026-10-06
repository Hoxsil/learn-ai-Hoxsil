#include <iostream>
using namespace std;


double a, b;

void init(){
    cin >> a >> b;
    return;
}

int main(){
    init();
    printf("%.2f\n", (a*b)/(a+b));
    cin >> a;
    return 0;
}