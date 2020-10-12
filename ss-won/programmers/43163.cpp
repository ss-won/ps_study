#include <string>
#include <vector>
#include <queue>
#include <functional>
using namespace std;
bool visited[50];

bool change(string a, string b)
{
    int c = 0;
    for (int s = 0; s < a.length(); s++)
    {
        if (a[s] != b[s])
            c++;
        if (c > 1)
            return false;
    }
    return true;
}

int solution(string begin, string target, vector<string> words)
{
    int answer = 0;
    int count = 0, size = (int)words.size();
    string curr;

    queue<pair<string, int>> q;
    q.push({begin, 0});
    while (!q.empty())
    {
        tie(curr, count) = q.front();
        q.pop();
        if (curr == target)
        {
            answer = count;
            break;
        }
        for (int i = 0; i < size; i++)
        {
            string next = words[i];
            if (!visited[i] && change(curr, next))
            {
                q.push({next, count + 1});
                visited[i] = true;
            }
        }
    }
    return answer;
}
