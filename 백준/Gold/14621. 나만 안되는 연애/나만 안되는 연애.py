import sys
import heapq

input = sys.stdin.readline

def find(u):
    global parent
    if parent[u] == u:
        return u
    parent[u] = find(parent[u])
    return parent[u]

def union(u,v):
    global parent
    parent[max(u,v)] = min(u,v)

def mst():
    global parent
    global edges
    global univ

    summ = 0
    n = 0
    while edges and n < len(univ) - 2:
        w, u, v = heapq.heappop(edges)
        if univ[u][0] != univ[v][0]:
            p1 = find(u)
            p2 = find(v)
            if p1 != p2:
                union(p1, p2)
                n += 1
                summ += w
                # print(u, v, w)
    if not edges and n < len(univ) - 2:
        return -1
    return summ



N, M = map(int, input().split())

univ = [[] for _ in range(N+1)]

wm = [''] +  input().split()
parent = [i for i in range(N+1)]
for i in range(1, N+1):
    univ[i].append(wm[i])

edges = []
for _ in range(M):
    u,v,w = map(int, input().split())
    univ[u].extend([v,w])
    univ[v].extend([u,w])
    heapq.heappush(edges, [w,u,v])

# print(univ)
print(mst())