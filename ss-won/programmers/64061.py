def solution(board, moves):
    answer = 0
    boardq = [[] for _ in range(len(board))]
    bucket = []
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] != 0:
                boardq[x].append(board[y][x])

    for mv in moves:
        if len(boardq[mv-1]) > 0:
            doll = boardq[mv-1].pop(0)
            if len(bucket) > 0 and bucket[-1] == doll:
                bucket.pop()
                answer += 2
            else:
                bucket.append(doll)
    return answer
