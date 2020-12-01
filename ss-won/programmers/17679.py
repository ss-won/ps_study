import re


def solution(m, n, board):
    answer = 0
    ck = [[False for _ in range(m)] for _ in range(n)]
    boardq = [[board[j][i] for j in range(m)] for i in range(n)]
    for i in range(n-1):
        for j in range(m-1):
            cur = boardq[i][j]
            if re.match('[A-Z]', cur) != None and cur == boardq[i][j+1]:
                if cur == boardq[i+1][j] and cur == boardq[i+1][j+1]:
                    ck[i][j], ck[i][j+1] = True, True
                    ck[i+1][j], ck[i+1][j+1] = True, True

    for i in range(n):
        for j in range(m):
            if ck[i][j] == True:
                answer += 1
                boardq[i].pop(j)
                boardq[i] = ['0'] + boardq[i]
    board = [[boardq[j][i] for j in range(n)] for i in range(m)]
    board = ["".join(board[i]) for i in range(m)]
    if answer == 0:
        return answer
    return solution(m, n, board) + answer
