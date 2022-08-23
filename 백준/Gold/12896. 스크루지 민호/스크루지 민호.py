import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(u, cnt):
    global graph
    global visited
    global max_distance
    global node

    visited[u] = True
    flag = False
    for v in graph[u]:
        if not visited[v]:
            flag = True
            dfs(v, cnt+1)

    if not flag:
        if max_distance <= cnt:
            max_distance = cnt
            node = u


visited = [False for _ in range(N+1)]
max_distance = 0

node = 0
dfs(1,0)

visited = [False for _ in range(N+1)]
max_distance = 0
dfs(node,0)

if max_distance % 2 == 0:
    max_distance //= 2
else: max_distance=(max_distance + 1)// 2

print(max_distance)