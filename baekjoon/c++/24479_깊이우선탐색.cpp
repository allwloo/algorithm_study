#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>

using namespace std;

int cnt = 1;
vector<int> graph[100001];
int visited[100001];
int graph_count[100001];

void dfs(int R)
{
    if(visited[R]==1)
        return;
    visited[R]=1;
    graph_count[R] = cnt;
    cnt++;
    for(int i = 0; i<graph[R].size(); i++)
        dfs(graph[R][i]);

}


int main(void)
{

    int N = 0; int M = 0; int R = 0;
    int row = 0; int col = 0; // За, ї­

    cin >> N >> M >> R;

    for(int i=1; i<=M; i++)
    {
        scanf("%d %d", &col, &row );
        graph[row].push_back(col);
        graph[col].push_back(row);
    }
    
    for(int i=1; i<=N; i++)
    {
        sort(graph[i].begin(), graph[i].end());
    }
    

    dfs(R);

    for(int i=1; i<=N; i++)
        printf("%d\n",graph_count[i] );



    return 0;
}