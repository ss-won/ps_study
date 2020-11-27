def solution(files):
    answer = []
    num = [chr(ord('0')+i) for i in range(10)]
    fileArr = []
    for idx in range(len(files)):
        file, s, e = files[idx], -1, -1
        for i in range(len(file)):
            if s == -1 and file[i] in num:
                s = i
            if s != -1 and e == -1 and not file[i] in num:
                e = i
                break
        if e == -1:
            head, number, tail = file[0:s].lower(), int(file[s:]), ''
        else:
            head, number, tail = file[0:s].lower(), int(file[s:e]), file[e:]
        fileArr.append((head, number, tail, idx))
    res = sorted(fileArr, key=lambda x: (x[0], x[1], x[3]))
    answer = [files[idx] for h, n, t, idx in res]
    return answer
