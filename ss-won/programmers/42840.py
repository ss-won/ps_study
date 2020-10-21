def solution(answers):
    answer = []
    c1, c2, c3 = 0, 0, 0
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if one[i % len(one)] == answers[i]:
            c1 += 1
        if two[i % len(two)] == answers[i]:
            c2 += 1
        if three[i % len(three)] == answers[i]:
            c3 += 1
    if c1 > c2:
        if c1 > c3:
            answer.append(1)
        elif c1 < c3:
            answer.append(3)
        else:
            answer = [1, 3]
    elif c1 < c2:
        if c2 > c3:
            answer.append(2)
        elif c2 < c3:
            answer.append(3)
        else:
            answer = [2, 3]
    elif c1 == c2:
        if c1 > c3:
            answer = [1, 2]
        elif c1 < c3:
            answer.append(3)
        else:
            answer = [1, 2, 3]
    return answer
