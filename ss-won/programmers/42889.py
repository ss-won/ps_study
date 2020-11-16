def solution(N, stages):
    users, failRate = {}, [[0, i+1] for i in range(N)]
    for v in stages:
        if v in users:
            users[v] += 1
        else:
            users[v] = 1

    for i in range(1, N+1):
        stopped, arrived = 0, 0
        for key, val in users.items():
            if key >= i:
                if key == i:
                    stopped = val
                arrived += val
        if arrived != 0:
            failRate[i-1][0] = stopped / arrived

    failRate = sorted(failRate, key=lambda x: [-x[0], x[1]])
    answer = [n for r, n in failRate]
    return answer
