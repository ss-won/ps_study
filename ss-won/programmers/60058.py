def isValidBracket(s):
    op, cs = 0, 0
    for b in s:
        if cs > op:
            return False
        if b == '(':
            op += 1
        else:
            cs += 1
    if op == cs:
        return True
    return False


def isBalancedBracket(s):
    op, cs = 0, 0
    for b in s:
        if b == '(':
            op += 1
        else:
            cs += 1
    if op == cs:
        return True
    return False


def Reverse(s):
    res = ""
    for i in range(len(s)):
        if s[i] == '(':
            res += ')'
        else:
            res += '('
    return res


def solution(p):
    answer, u, v = '', '', ''
    if len(p) == 0:
        return answer

    i = 2
    while i <= len(p):
        if isBalancedBracket(p[0:i]):
            u, v = p[0:i], p[i:]
            break
        i += 2

    if isValidBracket(u) == True:
        answer = u + solution(v)
        return answer

    answer = "(" + solution(v) + ")" + Reverse(u[1:len(u)-1])
    return answer
