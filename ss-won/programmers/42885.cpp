#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <functional>
using namespace std;

bool desc(int a, int b)
{
    return a > b;
}

int solution(vector<int> people, int limit)
{
    int answer = 0, w;
    priority_queue<int, vector<int>, greater<int>> pq;
    sort(people.begin(), people.end(), desc);
    for (auto p : people)
    {
        if (pq.empty())
        {
            pq.push(p);
        }
        else
        {
            w = pq.top();
            if (w + p > limit)
            {
                pq.push(p);
            }
            else
            {
                pq.pop();
                answer++;
            }
        }
    }
    answer += (int)pq.size();
    return answer;
}
