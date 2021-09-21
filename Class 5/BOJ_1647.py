import sys
import heapq
input = sys.stdin.readline

def find_parent(parent,v):
    while parent[v] != v:
        v= parent[v]
    return parent[v]

def merge(parent,u,v):
    if u<v:
        parent[u]=v
    else : parent[v]=u

V,E=map(int,input().split())

graph=[]
nearest=[0 for _ in range(V+1)]
minn=0
vnear=0
distance=[float('inf') for _ in range(V+1)]

for _ in range(E):
    u,v,w=map(int, input().split())
    heapq.heappush(graph,(w,u,v))

parent=[ i for i in range(V+1) ]

F=[]
minn=0
while len(F)<V-2:
    w,u,v=heapq.heappop(graph)
    p=find_parent(parent,u)
    q=find_parent(parent,v)
    if p!=q:
        merge(parent,p,q)
        F.append((u,v))
        minn+=w
print(minn)

#출처:https://woongsin94.tistory.com/405