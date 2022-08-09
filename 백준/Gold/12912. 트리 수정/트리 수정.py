import sys

input = sys.stdin.readline

def dfs(start, tree):
    visited = [False for _ in range(len(tree))]
    maxx = 0
    q = [[start,0]]
    visited[start] = True
    while q :
        u, weight = q.pop()
        maxx = max(maxx, weight)
        for v, w in tree[u]:
            if not visited[v]:
                q.append([v, weight+w])
                visited[v] = True
    return maxx

def find_start_node(start, tree):
    visited = [False for _ in range(len(tree))]
    maxx = 0
    node = start
    q = [[start,0]]
    visited[start] = True
    while q :
        u, weight = q.pop()
        if maxx < weight:
            maxx = weight
            node = u

        for v, w in tree[u]:
            if not visited[v]:
                q.append([v, weight+w])
                visited[v] = True
    return node

N = int(input())

tree = [[] for _ in range(N)]
edges = []


for _ in range(N-1):
    u, v, w = map(int, input().split())
    tree[u].append([v, w])
    tree[v].append([u,w])
    edges.append([u,v,w])

maxx = -1
while edges:
    u, v, w = edges.pop()
    tree[u].remove([v,w])
    tree[v].remove([u,w])

    n1 = find_start_node(u, tree)
    n2 = find_start_node(v, tree)

    maxx = max(dfs(n1, tree) + dfs(n2, tree) + w, maxx)

    tree[u].append([v, w])
    tree[v].append([u,w])

print(maxx)