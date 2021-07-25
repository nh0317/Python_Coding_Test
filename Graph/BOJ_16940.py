import sys
import heapq

def bfs():
    start = 1
    visited = [False for _ in range(V + 1)]
    check=[]

    PQ=[]
    heapq.heappush(PQ,(path.index(start),start))
    visited[start]=True
    root=0
    if path[0]!=1:
        return False
    while PQ:
        w, x=heapq.heappop(PQ)
        check.append(x)
        for y in graph[x]:
            if not visited[y]:
                heapq.heappush(PQ,(rank[y]+root,y))
                visited[y]=True
        root+=100000
    return check==path

input = sys.stdin.readline
V=int(input())

graph=[[]for _ in range(V+1)]
for _ in range(V-1):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

path=list(map(int,input().split()))
rank=[0 for _ in range(max(path)+1)]
for  i in range(len(path)):
    rank[path[i]]=i

if(bfs()): print(1)
else : print(0)


