import sys
input = sys.stdin.readline

N, W = map(int, input().split())

nodes = [0 for _ in range(N+1)]
nodes[1] = 1
for _ in range(N-1):
    u, v = map(int, input().split())
    nodes[u] += 1
    nodes[v] += 1

print(W/nodes.count(1))