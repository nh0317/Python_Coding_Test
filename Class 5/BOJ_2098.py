import sys
def travel():
    for i in range(N):
        for j in range(N):
            if W[i][j]==0:
                W[i][j]=float('inf')
    for i in range(1,N):
        D[i][0]=W[i][0]

    for k in range(1,N-1):
        for route in range(1,size):
            if count(route,N)==k:
                for i in range(1,N):
                    if not isIn(i,route):
                        D[i][route]=getMinWeight(i,route)
    D[0][size-1]=getMinWeight(0,size-1)
    return D[0][size-1]

def getMinWeight(i, route):
    minWeight = float('inf')
    for j in range (1,N):
        if isIn(j,route):
            pre_route = route&~(1<<j-1)
            weight = W[i][j]+D[j][pre_route]
            if minWeight > weight:
                minWeight = weight
    return minWeight

def count(route,N):
    cnt=0
    for n in range(1,N):
        if route & (1<<n-1) !=0:
            cnt+=1
    return cnt

def isIn(i, route):
    if route &(1<<i-1)!=0:
        return True
    else: return False

input = sys.stdin.readline
N=int(input())
W=[[int(x) for x in input().split()]for _ in range(N)]
size = 2 ** (N-1)
D=[[float('inf') for _ in range(size)]for _ in range(N)]
print(travel())
