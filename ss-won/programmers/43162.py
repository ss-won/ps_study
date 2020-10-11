# 코딩테스트 고득점 Kit(DFS/BFS) - 네트워크(43162)
def solution(n, computers):
    answer = 0
    visited = []
    def dfs(s):
        visited.append(s)
        for i in range(len(computers[s])):
            if i != s and computers[s][i] == 1 and not(i in visited):
                dfs(i)
    for i in range(n):
        if not(i in visited):
            dfs(i)
            answer += 1
    return answer
