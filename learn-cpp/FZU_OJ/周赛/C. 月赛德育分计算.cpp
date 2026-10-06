#include <iostream>
#include <algorithm>
using namespace std;

int score[5005], sorted_score[5005], assigned_score[5005], n;
int score_to_rank[1205];
string name[5005];

void init(){
    cin >> n;
    for (int i=1;i <= n;i++){
        cin >> name[i] >> score[i];
        sorted_score[i] = score[i];
    }
    sort(sorted_score+1, sorted_score+n+1, greater<int>());
}

void get_assigned_score(){
    for (int i=n;i >= 1;i--)
        score_to_rank[sorted_score[i]] = i;
    for (int i=1;i <= n;i++){
        if(score[i]==0){
            assigned_score[i]=0;
            continue;
        }
        int x = score_to_rank[score[i]];
        assigned_score[i] = 100 * (n - x) / n;
    }
}

int main(){
    init();
    get_assigned_score();
    for (int i=1;i <= n;i++){
        if (score[i] == 0){
            printf("0\n");
        }
        else{
            int s = assigned_score[i];
            if(s >= 90) printf("0.8\n");
            else if(s >= 75) printf("0.7\n");
            else if(s >= 60) printf("0.6\n");
            else if(s >= 40) printf("0.5\n");
            else if(s >= 25) printf("0.4\n");
            else if(s >= 10) printf("0.3\n");
            else printf("0.2\n");
        }
    }
    return 0;
}