def solution(numbers, hand):
    answer, left, right = '', (3, 0), (3, 2)
    phone = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
    h = {'L': [1, 4, 7], 'R': [3, 6, 9]}

    for num in numbers:
        find = False
        for i in range(len(phone)):
            for j in range(len(phone[i])):
                if phone[i][j] == num:
                    find = True
                    break
            if find == True:
                break
        if num in h['L']:
            left = (i, j)
            answer += 'L'
        elif num in h['R']:
            right = (i, j)
            answer += 'R'
        else:
            gabLeft = abs(left[0]-i) + abs(left[1]-j)
            gabRight = abs(right[0]-i) + abs(right[1]-j)
            if gabLeft > gabRight:
                right = (i, j)
                answer += 'R'
            elif gabLeft < gabRight:
                left = (i, j)
                answer += 'L'
            else:
                if hand == "left":
                    left = (i, j)
                    answer += 'L'
                else:
                    right = (i, j)
                    answer += 'R'
    return answer
