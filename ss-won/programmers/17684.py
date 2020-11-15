def solution(msg):
    answer = []
    dict = {}
    for i in range(26):
        dict[chr(ord('A')+i)] = i+1
    cur, s = 0, len(dict)
    while cur < len(msg):
        i = len(msg)
        while i > cur:
            if msg[cur:i] in dict:
                w = msg[cur:i]
                answer.append(dict[w])
                cur = i
                if cur < len(msg):
                    c = msg[cur]
                    if not w+c in dict:
                        s += 1
                        dict[w+c] = s
                break
            i -= 1
    return answer
