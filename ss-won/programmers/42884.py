import heapq


def solution(routes):
    answer = 0
    pq, spot, ck = [], [], False
    for route in routes:
        s, e = route
        heapq.heappush(pq, (s, e))
    while len(pq) > 0:
        ck = False
        s, e = heapq.heappop(pq)
        if len(spot) == 0:
            spot.append([s, e])
        else:
            for sp in spot:
                if sp[0] <= s and sp[1] >= s and sp[0] <= e and sp[1] >= e:
                    sp[0], sp[1] = s, e
                    ck = True
                    break
                elif sp[0] <= s and sp[1] >= s:
                    sp[0] = s
                    ck = True
                    break
                elif sp[0] <= e and sp[1] >= e:
                    sp[1] = e
                    ck = True
                    break
            if ck == False:
                spot.append([s, e])
    answer = len(spot)
    return answer
