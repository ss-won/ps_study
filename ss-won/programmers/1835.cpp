#include <string>
#include <vector>
#include <cmath>
using namespace std;
vector<string> lines;
string kf = "ACFJMNRT";

void setLines(string cur)
{
    if (cur.length() == 8)
    {
        lines.push_back(cur);
        return;
    }
    for (int i = 0; i < 8; i++)
    {
        if (cur.find(kf[i]) == -1)
        {
            setLines(cur + kf[i]);
        }
    }
}

bool ckValid(string str, vector<string> data)
{
    for (auto d : data)
    {
        int f1 = str.find(d[0]), f2 = str.find(d[2]);
        int num = (int)(d[4] - '0') + 1;
        if (d[3] == '=')
        {
            if (abs(f1 - f2) != num)
                return false;
        }
        else if (d[3] == '<')
        {
            if (abs(f1 - f2) >= num)
                return false;
        }
        else if (d[3] == '>')
        {
            if (abs(f1 - f2) <= num)
                return false;
        }
    }
    return true;
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int n, vector<string> data)
{
    lines.clear();
    string kf = "ACFJMNRT";

    int answer = 0;
    setLines("");

    for (auto line : lines)
    {
        if (ckValid(line, data))
            answer += 1;
    }
    return answer;
}
