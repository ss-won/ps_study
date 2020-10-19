def solution(triangle):
    answer = 0
    h = len(triangle)
    cache = [[-1 for _ in range(h)] for _ in range(h)]

    def getMax(x, y):
        if x < 0 or x >= h or y < 0 or y >= h:
            return 0
        if cache[x][y] != -1:
            return cache[x][y]
        if x == h:
            return triangle[x][y]
        cache[x][y] = max(getMax(x+1, y), getMax(x+1, y+1)) + triangle[x][y]
        return cache[x][y]
    answer = getMax(0, 0)
    return answer
