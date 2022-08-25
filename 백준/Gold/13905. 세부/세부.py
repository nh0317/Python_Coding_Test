import sys
import heapq

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline

def find(u, parent):
    if u != parent[u]: 
        parent[u] = find(parent[u],parent)
    return parent[u]

def union(u,v,parent):
    p1 = find(u,parent)
    p2 = find(v,parent)
    parent[min(p1,p2)] = max(p1,p2)

def mst(start, end):
    global edges
    parent = [i for i in range(N+1)]
    minn = float('inf')
    s,e = start, end
    while edges:
        w, u, v = heapq.heappop(edges)
        p1 = find(u,parent)
        p2 =find(v,parent)
        if p1 != p2:
            union(u, v, parent)
            minn = min(minn, -w)
        if find(e,parent) == find(s,parent):
            return minn
    return 0

N, M = map(int, input().split())
start, end = map(int, input().split())
edges = []

for _ in range(M):
    u,v,w = map(int, input().split())
    heapq.heappush(edges,[-w, u,v])

res = mst(start, end)
print(res)