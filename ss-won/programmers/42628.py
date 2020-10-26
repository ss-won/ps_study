def solution(operations):
    answer = [0, 0]
    q = []
    for operation in operations:
        op, num = operation.split()
        if op == 'I':
            q.append(int(num))
            q.sort()
        else:
            if len(q) == 0:
                continue
            q.sort()
            if int(num) > 0:
                q.pop(-1)
            else:
                q.pop(0)

    if len(q) == 0:
        return answer
    answer[0], answer[1] = q[-1], q[0]
    return answer
