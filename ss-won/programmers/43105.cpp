#include <string>
#include <vector>
#include <algorithm>
using namespace std;
const int MAX = 500;
int cache[MAX][MAX];

int getMax(int x, int y, int h, vector<vector<int>> &triangle)
{
    if (x < 0 || x >= h || y < 0 || y >= h)
        return 0;
    if (cache[x][y] != -1)
        return cache[x][y];
    if (x == h - 1)
        return triangle[x][y];
    return cache[x][y] = max(getMax(x + 1, y, h, triangle), getMax(x + 1, y + 1, h, triangle)) + triangle[x][y];
}

int solution(vector<vector<int>> triangle)
{
    int answer = 0;
    int h = (int)triangle.size();

    // cache 초기화
    for (int i = 0; i < h; i++)
    {
        fill(&cache[i][0], &cache[i][h - 1] + 1, -1);
    }

    answer = getMax(0, 0, h, triangle);
    return answer;
}
