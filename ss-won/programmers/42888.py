def solution(record):
    answer = []
    msg = {}

    def Change(userId, name):
        msg[userId]['name'] = name
        for i in msg[userId]['e']:
            answer[i] = name+"님이 들어왔습니다."
        for i in msg[userId]['l']:
            answer[i] = name+"님이 나갔습니다."

    def Enter(userId, name):
        if not userId in msg:
            msg[userId] = {'e': [len(answer)], 'l': [], 'name': name}
        else:
            if msg[userId]['name'] != name:
                Change(userId, name)
            msg[userId]['e'].append(len(answer))
        answer.append(name+"님이 들어왔습니다.")

    def Leave(userId):
        msg[userId]['l'].append(len(answer))
        answer.append(msg[userId]['name']+"님이 나갔습니다.")

    for r in record:
        sr = r.split(" ", 3)
        if sr[0] == 'Enter':
            Enter(sr[1], sr[2])
        elif sr[0] == 'Leave':
            Leave(sr[1])
        else:
            Change(sr[1], sr[2])
    return answer
