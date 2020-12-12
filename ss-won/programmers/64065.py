def getTuples(s):
    tuples, s, i = [], s[1:len(s)-1], 0
    while i < len(s):
        if s[i] == '{':
            tp, i, j = [], i+1, i+1
            while (1):
                if s[i] == ',' or s[i] == '}':
                    tp.append(int(s[j:i]))
                    if s[i] == '}':
                        break
                    j = i+1
                i += 1
            tuples.append(tp)
        i += 1
    return tuples


def solution(s):
    answer = []
    tuples = sorted(getTuples(s), key=lambda x: len(x))
    for tp in tuples:
        for i in range(len(tp)):
            if not tp[i] in answer:
                answer.append(tp[i])
    return answer
