import sys
from collections import deque , defaultdict
input = sys.stdin.readline

min_step=float('inf')

def climbing(graph, x,y):
    visited=[[]for _ in range(T+1)]
    visited[y].append(x)
    que = deque([[y,x,0]])
    while que:
        by,bx,step = que.popleft()
        global min_step
        if step > min_step:
            continue
        if T==by:
            min_step=min(min_step,step)
            visited[by].remove(bx)
            continue
        for ny in range(by-2,by+3,1):
            if 0<=ny<=T:
                for nx in graph[ny]:
                    if(abs(nx-bx)<=2):
                        if nx not in visited[ny]:
                            visited[ny].append(nx)
                            que.append([ny,nx,step+1])

n,T=map(int, input().split())
hole=[[]for _ in range(T+1)]

visited = [[] for _ in range(T + 1)]
for _ in range(n):
    x,y=map(int, input().split())
    hole[y].append(x)

climbing(hole, 0,0)
if min_step == float('inf'):
    print(-1)
else:
    print(min_step)

# dfs로 푼다면?
# backtracking 할 때마다 노드를 미방문처리를 해야함
# 즉 bfs보다 방문횟수가 많아져 메모리 초과 또는 재귀 횟수 초과 발생
