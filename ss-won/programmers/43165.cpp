#include <string>
#include <vector>
using namespace std;

int search(vector<int> arr, int s, int curr, int target)
{
    int res = 0;
    if (s == arr.size())
    {
        if (curr == target)
            return 1;
        return 0;
    }
    res += search(arr, s + 1, curr + arr[s], target);
    res += search(arr, s + 1, curr - arr[s], target);
    return res;
}

int solution(vector<int> numbers, int target)
{
    int answer = 0;
    answer = search(numbers, 0, 0, target);
    return answer;
}
