def solution(n, results):
    answer = 0
    win = [[] for _ in range(n)]
    lost = [[] for _ in range(n)]
    for res in results:
        p, c = res[0]-1, res[1]-1
        win[p].append(c)
        lost[c].append(p)

    for i in range(n):
        for p in win[i]:
            for c in win[p]:
                if not c in win[i]:
                    win[i].append(c)
        for c in lost[i]:
            for p in lost[c]:
                if not p in lost[i]:
                    lost[i].append(p)

    for i in range(n):
        count = len(win[i]) + len(lost[i])
        if count == n-1:
            answer += 1
    return answer
