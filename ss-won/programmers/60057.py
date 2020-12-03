def Compression(size, s):
    cur, rep, res = s[0:size], 1, ""
    i = size
    while i < len(s):
        if s[i:i+size] != cur:
            if rep > 1:
                res += str(rep)+cur
            else:
                res += cur
            cur, rep = s[i:i+size], 1
        else:
            rep += 1
        i += size
    if rep != 1:
        res += str(rep) + cur
    else:
        res += cur
    res += s[i:]
    return res


def solution(s):
    answer = len(s)
    for size in range(1, len(s)//2+1):
        answer = min(answer, len(Compression(size, s)))
    return answer
