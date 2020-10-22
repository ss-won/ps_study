#include <string>
#include <vector>
#include <queue>
using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0, first, second;
    priority_queue<int, vector<int>, greater<int>> pq;
    
    for(auto food : scoville){
        pq.push(food);
    }
    
    while((int)pq.size() > 1) {
        if(pq.top() >= K)
            break;
        first = pq.top(); pq.pop();
        second = pq.top(); pq.pop();
        pq.push(first+second*2);
        answer++;
    }
    
    if(pq.top() < K) answer = -1;
    return answer;
}
