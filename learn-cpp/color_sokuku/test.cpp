#include <iostream>
#include <iomanip>
#include <windows.h>
#include <algorithm>
using namespace std;

int n;
int map[30][30];

int tmp_map[30][30], last_map[30][30], flag[30][30][30], color_num[30], finded_color[30];
// 行为 1 ，列为 2
int row_and_col_flag[30][2][30], row_and_col_num[30][2];
int count_num = 1;

void cout_map() {
    for (int i=1;i <= n;i++){
        for (int j=1;j <= n;j++)
            cout << setw(3) << map[i][j];
        cout << endl;
    }
    return;
}

void count_color() {
    // 清空所有颜色的计数
    for (int i=1;i <= n;i++)
        color_num[i] = 0;
    // 遍历计数
    for (int i=1;i <= n;i++) {
        for (int j=1;j <= n;j++)
            if (map[i][j] != 0)
                color_num[map[i][j]]++;
    }
    return;
}

void init() {
    cin >> n;
    for (int i=1;i <= n;i++)
        for (int j=1;j <= n;j++)
            cin >> map[i][j];
    count_color();
    int order_num[30];
    for (int i=1;i <= n;i++)
        order_num[i] = color_num[i];
    sort(order_num, order_num + n);
    for (int i=1;i <= n;i++)
        for (int j=1;j <= n;j++)
            if(color_num[i] == order_num[j])
                color_num[i] = j;
    for (int i=1;i <= n;i++)
        cout << i << "->" << color_num[i] << endl;
    for (int i=1;i <= n;i++)
        for (int j=1;j <= n;j++)
            map[i][j] = color_num[map[i][j]];
    return;
}

void draw_row_and_col() {
    for (int i=1;i <= n;i++)
        for (int j=1;j <= n;j++) {
            row_and_col_flag[map[i][j]][0][j] = 1;
            row_and_col_flag[map[i][j]][1][i] = 1;
        }
    return;
}

void count_row_and_col() {
    for (int k=1;k <= n;k++){
        row_and_col_num[k][0] = 0;
        row_and_col_num[k][1] = 0;
    }
    for (int k=1;k <= n;k++){
        for (int i=1;i <= n;i++){
            if (row_and_col_flag[k][0][i] == 1)
                row_and_col_num[k][0]++;
            if (row_and_col_flag[k][1][i] == 1)
                row_and_col_num[k][1]++;
        }
    }
    return;
}

void draw_map(int x, int y) {
    int num = map[x][y];
    for (int i=1;i <= n;i++) {
        map[x][i] = 0;
        map[i][y] = 0;
    }
    map[x-1][y-1] = 0;
    map[x-1][y+1] = 0;
    map[x+1][y-1] = 0;
    map[x+1][y+1] = 0;
    map[x][y] = num;
    finded_color[map[x][y]] = 1;
    return;
}

bool catch_one_color_one() {
    count_color();
    for (int k=1;k <= n;k++)
        if (color_num[k] == 1 && finded_color[k] == 0) {
            for (int i=1;i <= n;i++)
                for (int j=1;j <= n;j++)
                    if (map[i][j] == k){
                        draw_map(i, j);
                        return true;
                    }
        }
    
    return false;
}

bool catch_just_one_in_line() {
    bool find_flag = false;
    for (int k=1;k <= n;k++) {
        int row_num=0, col_num=0;
        // 检验第 k 行中是否有单独的块
        for (int j=1;j <= n;j++){
            if (map[k][j] != 0){
                if (col_num != 0){
                    col_num = 0;
                    break;
                }
                else {
                    col_num = j;
                }
            }
        }
        if (col_num != 0 && finded_color[map[k][col_num]] == 0) {
            draw_map(k, col_num);
            find_flag = true;
        }
        // 检验第 k 列中是否有单独的块
        for (int i=1;i <= n;i++){
            if (map[i][k] != 0){
                if (row_num != 0){
                    row_num = 0;
                    break;
                }
                else {
                    row_num = i;
                }
            }
        }
        if (row_num != 0 && finded_color[map[row_num][k]] == 0) {
            draw_map(row_num, k);
            find_flag = true;
        }
    }
    return find_flag;
}

bool exclude_one_line_color() {
    bool exclude_flag=false;
    for (int k=1;k <= n;k++){
        if (finded_color[k] == 1)
            break;
        if (row_and_col_num[k][0] == 1){
            cout << "行开始清除" << k <<endl;
            for (int i=1;i <= n;i++)
                if (row_and_col_flag[k][0][i] == 1){
                    for (int j=1;j <= n;j++)
                        if (map[i][j] != k && map[i][j] != 0){
                            cout << "清除坐标为" << i << " " << j << "的块" << endl;
                            map[i][j] == 0;
                            exclude_flag = true;
                        }
                    break;
                }
        }
        if (row_and_col_num[k][1] == 1){
            cout << "列开始清除" << k << endl;
            for (int i=1;i <= n;i++)
                if (row_and_col_flag[k][1][i] == 1){
                    for (int j=1;j <= n;j++)
                        if (map[i][j] != k && map[i][j] != 0){
                            cout << "清除坐标为" << i << " " << j << "的块" << endl;
                            map[i][j] = 0;
                            exclude_flag = true;
                        }
                }
        }
    }
    return exclude_flag;
}

void exclude() {
    int num=1;
    while (num <= 100) {
        num++;
        if (catch_one_color_one()) {
            cout << 1 << endl;
            continue;
        }
        if (catch_just_one_in_line()){
            cout << 2 << endl;
            continue;
        }
        draw_row_and_col();
        count_row_and_col();

        if (exclude_one_line_color()){
            cout << 3 << endl;
            continue;
        }
        return;
    }
}

int main() {
    init();
    SetConsoleOutputCP(CP_UTF8);
    
    cout_map();
    cout << "请输入回车以退出";
    cin >> n;
    return 0;
}