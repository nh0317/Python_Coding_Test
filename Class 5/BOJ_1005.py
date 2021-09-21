import sys
from collections import deque
import copy

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    V,E=map(int,input().split())
    graph = [[] for _ in range(V+1)]
    times = [-1]+list(map(int,input().split()))
    indegree=[0 for _ in range(V+1)]
    for i in range(E):
        v,u = map(int,input().split())
        graph[v].append(u)
        indegree[u]+=1
    W=int(input())

    dp = copy.deepcopy(times)
    que = deque([])
    for i in range(1,V+1):
        if indegree[i]==0:
            que.append(i)
    while que:
        v = que.popleft()
        if v==W:
            break
        maxTime=-1
        for next in graph[v]:
            indegree[next]-=1
            dp[next]=max(dp[next], dp[v]+times[next])
            if indegree[next]==0:
                que.append(next)
    print(dp[W])

# 위상정렬 공부하기
# 참고: https://chocochip101.tistory.com/entry/XFile