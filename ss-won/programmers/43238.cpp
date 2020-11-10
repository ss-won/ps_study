#include <string>
#include <vector>
#include <algorithm>
using namespace std;

unsigned long long solution(int n, vector<int> times)
{
    unsigned long long answer, p, cur, high, low;
    sort(times.begin(), times.end());
    high = times[times.size() - 1] * n;
    low = 1;
    answer = high;
    while (high >= low)
    {
        cur = (high + low) / 2;
        p = 0;
        for (auto time : times)
        {
            p += cur / time;
        }
        if (p < n)
        {
            low = cur + 1;
        }
        else
        {
            answer = min(answer, cur);
            high = cur - 1;
        }
    }
    return answer;
}
