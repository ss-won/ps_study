import re


def getAllCase(cur, op, fin):
    if len(cur) == 3:
        fin += [cur]
        return
    for i in range(len(op)):
        if not op[i] in cur:
            getAllCase(cur+[op[i]], op, fin)


def Operate(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    else:
        return a*b


def solution(expression):
    answer = 0
    op = ['+', '-', '*']
    cases = []
    getAllCase([], op, cases)
    for case in cases:
        num = list(map(lambda x: int(x), re.split('[-+*]', expression)))
        operators = re.findall('[-+*]', expression)
        for op in case:
            while op in operators and len(operators) > 0:
                idx = operators.index(op)
                nx = Operate(num[idx], num[idx+1], op)
                operators.pop(idx)
                num.pop(idx+1)
                num[idx] = nx
            if len(operators) == 0:
                answer = max(abs(num[0]), answer)
    return answer
