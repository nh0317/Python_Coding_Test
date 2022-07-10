from collections import deque


def make_zero(degrees, graph, a):
    result = []
    q = deque()
    cnt = 0

    for i in range(len(graph)):
        if degrees[i] == 1:
            q.append(i)

    while q:
        u = q.popleft()

        for v in graph[u]:
            if len(graph[u]) == 1 or (a[u] != 0 and a[v] != 0):
                cnt += abs(a[u])
                a[v] += a[u]
                a[u] = 0

            degrees[v] -= 1
            if degrees[v] == 1:
                q.append(v)

    for w in a:
        if w != 0: cnt = -1

    return cnt


def solution(a, edges):
    degrees = [0 for _ in range(len(a))]
    graph = [[] for _ in range(len(a))]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        degrees[v] += 1
        degrees[u] += 1

    answer = make_zero(degrees, graph, a)
    return answer