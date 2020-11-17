def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        li = arr1[i] | arr2[i]
        li = str(bin(li))[2:]
        res = ""
        if len(li) < n:
            li = "".join(['0' for _ in range(n-len(li))]) + li
        for idx in range(n):
            if li[idx] == '1':
                res += '#'
            else:
                res += ' '
        answer.append(res)
    return answer
