import sys

def floyd(D,V):
    for k in range(1, V):
        for i in range(1, V):
            for j in range(1, V):
                if (i == j):
                    D[i][j] = 0
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])

input = sys.stdin.readline
V=int(input())+1
bus=int(input())

D = [[float('inf') for _ in range(V)]for _ in range(V)]
for _ in range(bus):
    u,v,w=map(int,input().split())
    D[u][v]=min(D[u][v],w)

floyd(D,V)

for i in range(1,V):
    for j in range(1,V):
        if(D[i][j]==float('inf')): print(0, end=" ")
        else: print(D[i][j],end=" ")
    print()