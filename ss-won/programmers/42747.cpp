#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool compare(int a, int b)
{
    return a > b;
}
// 논문의 수 1<= citations.size() <= 1000
// 논문별 인용 횟수 0 <= citations의 value <= 10000
int solution(vector<int> citations)
{
    int answer = 0;
    int n = (int)citations.size();
    int h = 0, upper = 0, remain = 0;

    if (n == 1)
        return answer = citations[0];

    sort(citations.begin(), citations.end(), compare);
    h = citations[0];
    int i = 1, j = 0;
    while (h >= 0)
    {
        while (j < n)
        {
            if (citations[j] < h)
                break;
            j++;
        }
        upper = j;
        remain = n - j;
        if (upper >= h && remain <= h)
        {
            break;
        }
        else
        {
            h--;
            i = (i + 1) % n;
            j = 0;
        }
    }
    return answer = h;
}
