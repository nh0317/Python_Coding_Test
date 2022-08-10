import sys

input = sys.stdin.readline

N = int(input())

tree = [[] for _ in range(N+1)]

def find_longest(u, tree):
    visited = [False for _ in range(len(tree))]
    visited[u] = True
    stack = [[u, 0]]
    maxx = -1
    node = u
    while stack:
        u, w = stack.pop()
        if maxx < w:
            maxx = w
            node = u

        for v,weight in tree[u]:
            if not visited[v]:
                stack.append([v, w+weight])
                visited[v] = True
    return node, maxx


for _ in range(N-1):
    u, v, w = map(int, input().split())
    tree[u].append([v,w])
    tree[v].append([u,w])

node, maxx = find_longest(1, tree)
node, maxx = find_longest(node, tree)

print(maxx)

