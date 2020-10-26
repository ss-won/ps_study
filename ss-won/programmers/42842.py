def solution(brown, yellow):
    answer = []
    sum = int((brown+4)/2)
    mul = brown+yellow
    w, h = sum-1, 1
    while w >= h:
        if w*h == mul:
            break
        h += 1
        w = sum-h
    answer = [w, h]
    return answer
