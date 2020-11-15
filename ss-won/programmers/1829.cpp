#include <vector>
#include <queue>
#include <functional>
using namespace std;
const int MAX = 101;
bool visited[MAX][MAX];
pair<int, int> mv[4] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

int bfs(int x, int y, int m, int n, vector<vector<int>> map)
{
    int cx, cy, w = 1;
    queue<pair<int, int>> q;
    visited[x][y] = true;
    q.push({x, y});
    while (!q.empty())
    {
        tie(cx, cy) = q.front();
        q.pop();
        for (int i = 0; i < 4; i++)
        {
            int nx = cx + mv[i].first, ny = cy + mv[i].second;
            if (nx >= 0 && nx < m && ny >= 0 && ny < n)
            {
                if (!visited[nx][ny] && map[nx][ny] == map[cx][cy])
                {
                    visited[nx][ny] = true;
                    q.push({nx, ny});
                    w++;
                }
            }
        }
    }
    return w;
}
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture)
{
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    for (int i = 0; i < m; i++)
    {
        fill(&visited[i][0], &visited[i][n - 1] + 1, false);
    }
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (picture[i][j] != 0 && !visited[i][j])
            {
                max_size_of_one_area = max(bfs(i, j, m, n, picture), max_size_of_one_area);
                number_of_area++;
            }
        }
    }

    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}
