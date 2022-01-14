import sys
import heapq

input = sys.stdin.readline

N,M = map(int,input().split())

problems=[[] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    problems[a].append(b)
    degree[b]+=1

que = []

for i in range(1,N+1):
    if degree[i] == 0:
        heapq.heappush(que,i)

result=[]
while que:
    a=heapq.heappop(que)
    result.append(a)
    for u in problems[a]:
        degree[u]-=1
        if degree[u]==0:
            heapq.heappush(que,u)

for  r in result:
    print(r, end=" ")
