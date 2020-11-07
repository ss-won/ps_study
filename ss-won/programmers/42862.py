def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    ck = []
    for r in reserve:
        for i in range(len(lost)):
            if lost[i] == r:
                lost.pop(i)
                ck.append(r)
                break

    for r in reserve:
        if not r in ck:
            for i in range(len(lost)):
                if lost[i] == r-1:
                    lost.pop(i)
                    break
                elif lost[i] == r+1:
                    lost.pop(i)
                    break

    answer = n - len(lost)
    return answer
