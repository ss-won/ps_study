#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <functional>
using namespace std;
struct compare
{
    bool operator()(pair<int, int> a, pair<int, int> b)
    {
        if (a.second == b.second)
            return a.first > b.first;
        return a.second > b.second;
    }
};

// Shortest Job First 방식이 평균 대기시간을 줄여주는 방식이므로 평균 CPU burst time을 줄일 수 있다.
// 본 문제에서는 비선점형 SJF 구현에 대한 문제이다.
int solution(vector<vector<int>> jobs)
{
    int answer = 0;
    int at, bt, top = 0;
    int cur = 0, size = (int)jobs.size();
    priority_queue<pair<int, int>, vector<pair<int, int>>, compare> pq;
    sort(jobs.begin(), jobs.end());

    for (int i = size; i > 0; i--)
    {
        if (pq.empty() && jobs[top][0] > cur)
            cur = jobs[top][0];
        for (int j = top; i > pq.size() && j < size; j++)
        {
            if (jobs[j][0] <= cur)
            {
                pq.push({jobs[j][0], jobs[j][1]});
            }
            else
            {
                top = j;
                break;
            }
        }
        tie(at, bt) = pq.top();
        pq.pop();
        cur += bt;
        answer += cur - at;
    }

    return answer / size;
}
