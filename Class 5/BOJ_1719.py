import sys
import copy

input = sys.stdin.readline

V, E = map(int,input().split())

D = [[float('inf') for _ in range(V+1)] for _ in range(V+1)]
P = [[float('inf') for _ in range(V+1)] for _ in range(V+1)]


for _ in range(E):
    u,v,w=map(int, input().split())
    D[u][v]=w
    D[v][u]=w
    P[u][v]=v
    P[v][u]=u

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            if D[i][j] > D[i][k]+D[k][j] and i != j:
                D[i][j]=D[i][k]+D[k][j]
                P[i][j]=P[i][k]

for i in range(1,V+1):
    for j in range(1,V+1):
        if P[i][j] == float('inf'):
            print("-",end=" ")
        else:
            print(P[i][j],end=" ")
    print()

