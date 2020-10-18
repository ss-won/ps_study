def solution(priorities, location):
    answer = 0
    ckprint = True
    q = []
    printed = []

    for i in range(len(priorities)):
        q.append([priorities[i], i])

    while(len(q) > 0):
        cur, idx = q[0][0], q[0][1]
        q.pop(0)
        for doc in q:
            if doc[0] > cur:
                ckprint = False
                break
        if ckprint == True:
            printed.append(idx)
        else:
            q.append([cur, idx])
            ckprint = True

    for i in range(len(printed)):
        if location == printed[i]:
            answer = i+1
            break

    return answer
