def solution(name):
    answer, cur = 0, 0
    ck = [False for _ in range(len(name))]
    for i in range(len(name)):
        if name[i] == 'A':
            ck[i] = True

    while False in ck:
        if ck[cur] == False:
            if ord(name[cur]) - ord('A') <= 13:
                answer += ord(name[cur]) - ord('A')
            else:
                answer += 26 - ord(name[cur]) + ord('A')
            ck[cur] = True
        # 다음 문자 탐색
        i, j = cur-1, cur
        if cur < len(name)-1:
            j += 1
        while ck[i] == True:
            if abs(cur-i) == len(name):
                i = 0
                break
            i -= 1
        while j < len(name) and ck[j] == True:
            if j == len(name)-1:
                break
            j += 1
        # 다음 위치 선택 및 answer 업데이트
        if ck[i] == True and ck[j] == True:
            break
        elif ck[i] == True:
            answer += abs(j-cur)
            cur = j
        elif ck[j] == True:
            answer += abs(i-cur)
            if i < 0:
                cur = len(name)+i
            else:
                cur = i
        else:
            if abs(i-cur) >= abs(j-cur):
                answer += abs(j-cur)
                cur = j
            else:
                answer += abs(i-cur)
                if i < 0:
                    cur = len(name)+i
                else:
                    cur = i
    return answer
