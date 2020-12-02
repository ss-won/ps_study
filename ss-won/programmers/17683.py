def solution(m, musicinfos):
    answer = "(None)"

    def Translate(s):
        music, i = "", 0
        while i < len(s):
            if i+1 < len(s) and s[i+1] == '#':
                music += s[i].lower()
                i += 2
            else:
                music += s[i]
                i += 1
        return music

    def getPlaytime(st, et):
        st, et = int(st[0:2])*60+int(st[-2:]), int(et[0:2])*60+int(et[-2:])
        if st <= et:
            playtime = et - st
        else:
            plattime = 25*60-st + et
        return playtime

    m = Translate(m)
    mdict = {}
    for music in musicinfos:
        st, et, title, s = music.split(",", 4)
        playtime = getPlaytime(st, et)
        s = Translate(s)
        s = s * (playtime//len(s)) + s[0:playtime % len(s)]
        mdict[s] = title
        i = 0
        while i+len(m) <= len(s):
            if m == s[i:i+len(m)]:
                if answer == "(None)" or len(s) > len(answer):
                    answer = s
                break
            i += 1
    if answer != "(None)":
        answer = mdict[answer]
    return answer
