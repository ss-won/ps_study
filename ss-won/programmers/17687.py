def solution(n, t, m, p):
    answer = ''
    num = ['0', '1', '2', '3', '4', '5', '6', '7',
           '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    narr, size, cur, ck = [], p+m*(t-1), [0], False
    while len(narr) < size:
        if cur[-1] >= n:
            for i in range(1, len(cur)+1):
                cur[-i] += 1
                if cur[-i] < n:
                    ck = True
                    break
                cur[-i] = 0
            if ck == False:
                cur = [1] + cur
        for v in cur:
            narr.append(num[v])
        cur[-1] += 1
        ck = False
    for i in range(t):
        answer += narr[p+m*i-1]
    return answer
