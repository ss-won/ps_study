#include <string>
#include <vector>
#include <queue>
#include <functional>
using namespace std;
const int MAX = 20001;
vector<int> adj[MAX];
bool visited[MAX];

int bfs(int s)
{
    int count = 0, mx = 0, v, h;
    visited[s] = true;
    queue<pair<int, int>> q;
    q.push({s, 0});
    while (!q.empty())
    {
        tie(v, h) = q.front();
        q.pop();
        if (h > mx)
        {
            mx = h;
            count = 1;
        }
        else if (h == mx)
        {
            count += 1;
        }
        for (auto next : adj[v])
        {
            if (!visited[next])
            {
                visited[next] = true;
                q.push({next, h + 1});
            }
        }
    }
    return count;
}

int solution(int n, vector<vector<int>> edge)
{
    int answer = 0, u, v;

    // 인접행렬 adj
    for (auto e : edge)
    {
        u = e[0];
        v = e[1];
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    fill(&visited[0], &visited[n] + 1, false);
    visited[1] = true;
    return answer = bfs(1);
}
