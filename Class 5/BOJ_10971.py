import sys

def TSP():
    for i in range(N):
        for j in range(N):
            if W[i][j]==0:
                W[i][j]=float('inf')
    for i in range(1,N):
        D[i][0]=W[i][0]

    for k in range(1,N-1):
        for route in range(1,elements):
            if count(route)==k:
                for i in range(1,N):
                    if not isIn(i,route):
                        D[i][route] = minWeight(i,route)
    D[0][elements-1]= minWeight(0,elements-1)
    return D[0][elements-1]

def minWeight(i,route):
    min_dis=float('inf')
    for j in range(1,N):
        if isIn(j,route):
            m=W[i][j]+D[j][diff(route,j)]
            if(min_dis>m):
                min_dis=m
    return min_dis

def count(route):
    cnt=0
    for i in range(1,N):
        if route & (1<<i-1) != 0:
            cnt+=1
    return cnt

def isIn(i,route):
    if route & (1<<i-1)!=0:
        return True
    else: return False

def diff(route,i):
    return route & ~(1<<i-1)



input=sys.stdin.readline
N=int(input())

W =[list(map(int,input().split())) for _ in range(N)]
elements=1<<(N-1) # 1~N-1 원소 방문 처리
D =[[float('inf') for _ in range(elements)]for _ in range(N)]

print(TSP())
