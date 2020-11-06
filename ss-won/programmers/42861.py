import heapq


def solution(n, costs):
    answer = 0
    root = [i for i in range(n)]
    rank = [1 for _ in range(n)]
    pq = []
    for cost in costs:
        u, v, w = cost
        heapq.heappush(pq, (w, u, v))

    def find(v):
        if root[v] != v:
            root[v] = find(root[v])
        return root[v]

    def union(u, v):
        ru, rv = find(u), find(v)
        if rank[u] > rank[v]:
            root[rv] = ru
        else:
            if rank[ru] == rank[rv]:
                rank[v] += 1
            root[ru] = rv

    while len(pq) > 0:
        w, u, v = heapq.heappop(pq)
        if find(u) != find(v):
            union(u, v)
            answer += w
    return answer
