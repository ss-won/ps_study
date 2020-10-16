#include <string>
#include <vector>
#include <functional>
using namespace std;
const int MAX = 10001;
bool visited[MAX];
bool finished = false;
int use = 0;

void visit(string cur, vector<vector<string>> tickets, vector<string> &answer)
{
    if (use == tickets.size())
    {
        finished = true;
        return;
    }
    for (int i = 0; i < tickets.size(); i++)
    {
        if (tickets[i][0] == cur && !visited[i])
        {
            visited[i] = true;
            answer.push_back(tickets[i][1]);
            use++;
            visit(tickets[i][1], tickets, answer);
            if (!finished)
            {
                visited[i] = false;
                use--;
                answer.pop_back();
            }
        }
    }
}

// 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return
vector<string> solution(vector<vector<string>> tickets)
{
    vector<string> answer;

    // 정렬
    sort(tickets.begin(), tickets.end());

    // 방문
    answer.push_back("ICN");
    visit("ICN", tickets, answer);

    return answer;
}
