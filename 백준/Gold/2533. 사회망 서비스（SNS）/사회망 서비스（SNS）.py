import sys

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

def dfs(u):
    global early
    global visited
    visited[u] = True

    early[u][0] = 1

    for v in graph[u]:
        if not visited[v]:
            dfs(v)
            early[u][1] += early[v][0]
            early[u][0] += min(early[v][0], early[v][1])


N = int(input())

graph = [[] for _ in range(N+1)]

early = [[0 for _ in range(2)] for _ in range(N + 1)]
visited = [False for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(1)

print(min(early[1][0], early[1][1]))

# https://hqjang.tistory.com/104