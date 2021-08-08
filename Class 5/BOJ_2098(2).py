import sys
import heapq

class node :
    level=0
    path=[]
    subpath=[]
    bound=0
    weight=0

    def __init__(self,level):
        self.level=level
        self.path=[]
        self.bound=0
        self.weight=0

    def contains(self,x):
        for i in range(len(self.path)):
            if (self.path[i]==x):
                return True
        return False

    def calSubPath(self):
        self.subpath=self.path[1:0]

    def calW(self):
        self.weight=0
        for i in range(len(self.path)-1):
            if W[self.path[i]][self.path[i+1]]==0:
                return float('inf')
            else : self.weight+=W[self.path[i]][self.path[i+1]]
        return self.weight
    def __lt__(self, other):
        return self.bound<other.bound


def bound(u):
    summ=0
    if u.path[-1]==0:
        for i in range(N):
            summ+=min(W[i])
        return summ

    summ=u.calW()
    u.calSubPath()
    for i in range(u.path[-1],N):
        minn=float('inf')
        for j in range(N):
            if i==u.path[-1] and j!=0 and j not in u.subpath and i!=j:
                if W[i][j]==0:
                    return float('inf')
                elif minn>W[i][j]:
                    minn=W[i][j]
            elif j not in u.subpath and i!=j:
                if W[i][j]==0:
                    return float('inf')
                if minn>W[i][j]:
                    minn=W[i][j]
        summ+=minn
    return summ

def findNotIn(u):
    for i in range(N):
        if i not in u.path:
            return i

input = sys.stdin.readline
N=int(input())
W=[[int(x) for x in input().split()]for _ in range(N)]
PQ=[]
v=node(0)
global minLength
minLength=float('inf')
v.path.append(0)
v.bound=bound(v)
heapq.heappush(PQ,v)
while PQ:
    v=heapq.heappop(PQ)
    if (v.bound<minLength):
        for i in range(1,N):
            if v.contains(i):
                continue
            u=node(v.level+1)
            u.path=v.path[:]
            u.path.append(i)
            if(u.level == N-2):
                u.path.append(findNotIn(u))
                u.path.append(0)
                u.calW()
                if (u.weight<minLength):
                    minLength=u.weight
            else:
                u.bound = bound(u)
                if u.bound < minLength:
                    heapq.heappush(PQ,u)
print(minLength)

