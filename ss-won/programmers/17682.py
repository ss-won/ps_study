def solution(dartResult):
    answer, cur = 0, 0
    bonus = {'S': 1, 'D': 2, 'T': 3}
    res = []
    while cur+1 < len(dartResult):
        for i in range(cur+1, len(dartResult)):
            if dartResult[i] in bonus:
                break
        n, b = int(dartResult[cur:i]), dartResult[i]
        res.append(n**bonus[b])
        cur = i+1
        if i+1 < len(dartResult):
            o = dartResult[i+1]
            if o == '*' or o == '#':
                if o == '*':
                    if len(res) >= 2:
                        res[-1] *= 2
                        res[-2] *= 2
                    else:
                        res[-1] *= 2
                elif o == '#':
                    res[-1] *= -1
                cur += 1
    for v in res:
        answer += v
    return answer
