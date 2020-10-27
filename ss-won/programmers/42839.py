import math


def solution(numbers):
    answer = 0
    arr, checked, size = list(numbers), [], len(numbers)

    def ckDecimal(num):
        if num == 1 or num == 0:
            return False
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True

    def mkNum(l, cur, arr, res):
        if l == len(cur):
            if not(int(cur) in checked):
                if ckDecimal(int(cur)):
                    res += 1
                checked.append(int(cur))
            return res
        for i in range(len(arr)):
            res = mkNum(l, cur+arr[i], arr[:i]+arr[i+1:], res)
        return res
    for i in range(1, size+1):
        answer += mkNum(i, "", arr, 0)
    return answer
