import sys
from collections import deque

input = sys.stdin.readline

def bfs(y,x,visited):
    di=[[1,0],[0,1],[-1,0],[0,-1]]
    que = deque([[y,x]])
    co=[[y,x]]
    sumi=cities[y][x]
    visited[y][x]=True
    while que:
        # print(que, visited)
        cy, cx = que.popleft()
        for dy, dx in di:
            ny = cy+dy
            nx = cx +dx
            if 0<=ny<N and 0<= nx <N:
                # print(visited[ny][nx], ny, nx, cy, cx, abs(cities[ny][nx] - cities[cy][cx]))
                if not visited[ny][nx] and L<=abs(cities[ny][nx]-cities[cy][cx])<=R:
                    co.append([ny,nx])
                    que.append([ny,nx])
                    visited[ny][nx]=True
                    sumi+=cities[ny][nx]
    return co,sumi;

N, L, R = map(int, input().split())

cities = [list(map(int, input().split())) for _ in range(N)]

moved = float('inf')
day=-1
while True:
    visited = [[False for _ in range(N)]for _ in range(N)]
    moved=False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                co,total = bfs(i,j,visited)
                # print(co, total)
                if len(co) > 1:
                    moved=True
                for y,x in co:
                    cities[y][x] = total//len(co)
    day+=1
    if not moved:
        break
print(day)