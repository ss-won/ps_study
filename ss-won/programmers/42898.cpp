#include <string>
#include <vector>
using namespace std;
const int MAX = 501;
const int dv = 1000000007;
int cache[MAX][MAX];
char map[MAX][MAX];

int getPath(int x, int y, int m, int n)
{
    if (x > m || y > n || map[x][y] == '1')
        return 0;
    if (cache[x][y] != -1)
        return cache[x][y];
    if (x == m && y == n)
        return cache[x][y] = 1;
    return cache[x][y] = (getPath(x + 1, y, m, n) + getPath(x, y + 1, m, n)) % dv;
}

int solution(int m, int n, vector<vector<int>> puddles)
{
    int answer = 0;
    // cache 초기화
    for (int i = 0; i <= m; i++)
    {
        fill(&cache[i][0], &cache[i][n] + 1, -1);
    }

    // puddles 표시
    for (auto puddle : puddles)
    {
        int x = puddle[0], y = puddle[1];
        map[x][y] = '1';
    }

    answer = getPath(1, 1, m, n);
    return answer;
}
