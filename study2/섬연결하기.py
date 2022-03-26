import heapq


def heapsort(cost):
    q = []
    for c in cost:
        heapq.heappush(q, [c[2], c[0], c[1]])
    return q


def find_parent(parent, v):
    while parent[v] != v:
        v = parent[v]
    return parent[v]


def merge(parent, u, v):
    if (u < v):
        parent[u] = v
    else:
        parent[v] = u


def MST(q, V):
    parents = [i for i in range(V)]
    minn = 0
    F = []
    while len(F) < V - 1:
        w, u, v = heapq.heappop(q)
        p1 = find_parent(parents, u)
        p2 = find_parent(parents, v)
        if (p1 != p2):
            merge(parents, p1, p2)
            minn += w
            F.append([u, v])
    return minn


def solution(n, costs):
    answer = 0
    q = heapsort(costs)
    answer = MST(q, n)

    return answer