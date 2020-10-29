def solution(number, k):
    answer = ''
    narr, arr, count = list(number), [], 0
    for i in range(len(narr)):
        if count == k:
            break
        if len(arr) == 0:
            arr.append(narr[i])
        else:
            while len(arr) >= 0 and count <= k:
                if len(arr) == 0:
                    arr.append(narr[i])
                    break
                if arr[-1] >= narr[i]:
                    arr.append(narr[i])
                    break
                else:
                    arr.pop()
                    count += 1
                    if count == k:
                        arr += narr[i:]
                        break
    while len(arr) > len(narr)-k:
        arr.pop()
    answer = "".join(arr)
    return answer
