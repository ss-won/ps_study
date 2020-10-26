#include <string>
#include <vector>
#include <deque>
#include <algorithm>
using namespace std;

vector<int> solution(vector<string> operations)
{
    vector<int> answer(2, 0);
    deque<int> dq;

    for (auto operation : operations)
    {
        char op = operation[0];
        int num = stoi(operation.substr(2));
        if (op == 'I')
        {
            dq.push_back(num);
            sort(dq.begin(), dq.end());
        }
        else
        {
            if (!dq.empty())
            {
                if (num > 0)
                    dq.pop_back();
                else
                    dq.pop_front();
                sort(dq.begin(), dq.end());
            }
        }
    }
    if (dq.empty())
        return answer;
    answer[0] = dq.back();
    answer[1] = dq.front();

    return answer;
}
