#include <string>
#include <vector>
#include <queue>
using namespace std;
const int MAX = 200;
bool visited[MAX];

void bfs(int s, vector<vector<int>> computers)
{
    queue<int> q;
    q.push(s);
    visited[s] = true;
    int n = (int)computers.size();
    while (!q.empty())
    {
        int curr = q.front();
        q.pop();
        for (int i = 0; i < n; i++)
        {
            if (i == curr)
                continue;
            if (computers[curr][i] && !visited[i])
            {
                visited[i] = true;
                q.push(i);
            }
        }
    }
}
// 컴포넌트 개수 세기
int solution(int n, vector<vector<int>> computers)
{
    int answer = 0;
    for (int i = 0; i < n; i++)
    {
        if (!visited[i])
        {
            bfs(i, computers);
            answer++;
        }
    }
    return answer;
}
