import sys
from collections import deque

input = sys.stdin.readline

N, W = map(int, input().split())

def bfs():
    global graph
    q = deque([1])
    visited = [False for _ in range(len(graph))]
    visited[1] = True
    leaves = 0

    while q:
        u = q.popleft()

        is_leaf = True
        for v in graph[u]:
            if not visited[v]:
                q.append(v)
                visited[v] = True
                is_leaf = False
        if is_leaf:
            leaves+=1
    return leaves



graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

leaves = bfs()
print(W/leaves)