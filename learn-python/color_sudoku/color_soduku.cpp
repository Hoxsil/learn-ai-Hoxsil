#include <iostream>
#include <iomanip>
using namespace std;

int n;
int Map[30][30];

int tmp_map[30][30], last_map[30][30], flag[30][30][30];


void add_flag(int x, int y, int num) {
    for (int i=1;i <= n;i++) {
        flag[i][y][num] = 99;
        flag[x][i][num] = 99;
    }
    flag[x-1][y-1][num] = 99;
    flag[x-1][y+1][num] = 99;
    flag[x+1][y-1][num] = 99;
    flag[x+1][y+1][num] = 99;
    flag[x][y][num] = -num;
    return;
}

void clear_flag(int x, int y, int num) {
    for (int i=1;i <= n;i++) {
        flag[i][y][num] = 0;
        flag[x][i][num] = 0;
    }
    flag[x-1][y-1][num] = 0;
    flag[x-1][y+1][num] = 0;
    flag[x+1][y-1][num] = 0;
    flag[x+1][y+1][num] = 0;
    return;
}

void draw_tmp_map() {
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            tmp_map[i][j] = Map[i][j];
    
    for (int i=1;i <= n;i++)
        for (int j=1;j <= n;j++)
            for (int k=1;k <= n;k++) {
                if (flag[i][j][k] != 0) {
                    tmp_map[i][j] = -1;
                    break;
                }
            }
    return;
}

void draw_last_map() {
    for (int i=1;i <= n;i++)
        for (int j=1;j <= n;j++) {
            for (int k=1;k <= n;k++)
                if (flag[i][j][k] < 0)
                    last_map[i][j] = 1;
            if (tmp_map[i][j] == n) {
                last_map[i][j] = 1;
            }

        }
    return;
}

void init() {
    cin >> n;
    for (int i=1;i <= n;i++)
        for (int j=1;j <= n;j++)
            cin >> Map[i][j];
    return;
}

int dfs(int x, int y, int num) {
    if (num == n)
        return n;

    add_flag(x, y, num);
    draw_tmp_map();

    int goal = num + 1;
    bool find_goal = false;

    for (int i=1;i <= n;i++)
        for (int j=1;j <= n;j++) {
            draw_tmp_map();
            if (tmp_map[i][j] == goal)
                if (dfs (i, j, goal) == n)
                    return n;
        }

    clear_flag(x, y, num);

    return num;
}

int main() {
    init();

    bool exit_flag = false;
    for (int i=1;i <= n;i++){
        for (int j=1;j <=n;j++)
            if(Map[i][j] == 1){
                // 初始状态允许一只 初始 num=1
                if (dfs(i, j, 1) == n){
                    draw_last_map();
                    exit_flag = true;
                    break;
                }
            }
        if(exit_flag) break;
    }

    for (int i=1;i <=n ;i++) {
        for (int j=1;j <= n;j++)
            cout << last_map[i][j] << ' ';
        cout << endl;
    }
    // cout << "请输入任意键以退出";
    // cin >> n;
    return 0;
}