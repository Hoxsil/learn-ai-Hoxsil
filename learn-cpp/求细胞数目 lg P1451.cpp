#include <iostream>
using namespace std;

int n, m, sum, flag[105][105];
char Map[105][105];
int X[5] = {0, 1, 0, -1, 0};
int Y[5] = {0, 0, 1, 0, -1};

void init() {
	cin >> n >> m;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
			cin >> Map[i][j];
	return;
}

void dfs(int x, int y){
    flag[x][y] = 1;
    for(int i=1;i <= 4;i++) {
        int x_next = x + X[i];
        int y_next = y + Y[i];
        if (Map[x_next][y_next] != '0' && flag[x_next][y_next] != 1 && x_next >= 1 && x_next <= n && y_next >= 1 && y_next <= m) {
            dfs(x_next, y_next);
        }
    }
    return;
}

int main() {
    init();
    for (int i=1;i <= n; i++) {
        for (int j=1;j <= m;j++){
            if(Map[i][j] != '0' && flag[i][j] == 0) {
                dfs(i, j);
                sum++;
            }
        }
    }
    cout << sum;
    return 0;
}