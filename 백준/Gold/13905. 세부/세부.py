import sys
import heapq

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline

def find(u, parent):
    if u == parent[u]:return u
    parent[u] = find(parent[u],parent)
    return parent[u]

def union(u,v,parent):
    parent[min(u, v)] = max(u,v)

def mst():
    global edges
    n = len(graph)
    parent = [i for i in range(N+1)]
    tree = []
    while edges:
        w, u, v = heapq.heappop(edges)
        p1 = find(u,parent)
        p2 =find(v,parent)
        if p1 != p2:
            union(p1, p2, parent)
            tree.append([-w,u,v])
    return tree


def dfs(start, end, mst):
    visited = [False for _ in range(N+1)]
    q = [[start, float('inf')]]
    minn = float('inf')
    visited[start] = True
    while q:
        child = False
        u, w = q.pop()
        if u == end:
            return w

        for v, weight in mst[u]:
            if not visited[v]:
                child = True
                q.append([v, min(weight, w)])
                visited[v] = True
    return 0

N, M = map(int, input().split())
start, end = map(int, input().split())
graph = [[] for _ in range(N+1)]
edges = []

for _ in range(M):
    u,v,w = map(int, input().split())
    heapq.heappush(edges,[-w, u,v])

tree=mst()

for w, u, v in tree:
    graph[u].append([v,w])
    graph[v].append([u,w])

res = dfs(start, end, graph)
print(res)