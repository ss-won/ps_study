def solution(m, n, puddles):
    answer = 0
    cache = [[-1 for _ in range(n+1)] for _ in range(m+1)]
    matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for puddle in puddles:
        x, y = puddle[0], puddle[1]
        matrix[x][y] = 1

    def getPath(x, y):
        if x > m or y > n or matrix[x][y] == 1:
            return 0
        if cache[x][y] != -1:
            return cache[x][y]
        if x == m and y == n:
            return 1
        cache[x][y] = (getPath(x+1, y) + getPath(x, y+1)) % 1000000007
        return cache[x][y]
    answer = getPath(1, 1)
    return answer
