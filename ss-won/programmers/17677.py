import re


def mkMultiSet(s):
    i = 0
    multiSet = {}
    while i < len(s)-1:
        if re.match('[A-Z]', s[i]) != None and re.match('[A-Z]', s[i+1]) != None:
            if not s[i:i+2] in multiSet:
                multiSet[s[i:i+2]] = 1
            else:
                multiSet[s[i:i+2]] += 1
        i += 1
    return multiSet


def solution(str1, str2):
    answer = 0
    set1, set2 = mkMultiSet(str1.upper()), mkMultiSet(str2.upper())
    if len(set1) == 0 and len(set2) == 0:
        answer = 65536
    else:
        total, n = 0, 0
        for key in set1:
            if key in set2:
                if set1[key] <= set2[key]:
                    n += set1[key]
                else:
                    n += set2[key]
        for k, v in set1.items():
            total += v
        for k, v in set2.items():
            total += v
        answer = int(n / (total - n) * 65536)
    return answer
