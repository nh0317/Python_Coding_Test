import sys
import heapq

input = sys.stdin.readline

V,E=map(int,input().split())
graph=[[]for _ in range(V+1)]
for _ in range(E):
    u,v,w=map(int,input().split())
    graph[u].append([v,w])
    graph[v].append([u,w])
sum_w=0
heap=[[0,1]]
visited=[False for _ in range(V+1)]
while heap:
    for _ in range(V):
        if heap:
            w,u = heapq.heappop(heap)
            if not visited[u]:
                visited[u]=True
                sum_w+=w
                for i in graph[u]:
                    heapq.heappush(heap,[i[1],i[0]])
print(sum_w)
