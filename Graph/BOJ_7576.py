import sys
from collections import deque

def bfs(ripe):
    dy=[1,-1,0,0]
    dx=[0,0,1,-1]
    visited=[[False for _ in range(M)]for _ in range(N)]
    day=-1
    while ripe:
        for _ in range(len(ripe)):
            y,x=ripe.popleft()
            if not visited[y][x]:
                visited[y][x]=True
                for i in range(4):
                    ny=dy[i]+y
                    nx=dx[i]+x
                    if 0<=ny<N and 0<=nx<M and box[ny][nx]!=-1:
                        if box[y][x]==1 and box[ny][nx]==0:
                            box[ny][nx]=1
                            ripe.append([ny,nx])
        day+=1
    for b in box:
        if 0 in b:
            day=-1
    return day


input=sys.stdin.readline
M,N=map(int,input().split())
box=[]
ripe=deque()
for i in range(N):
    row=list(map(int,input().split()))
    for j in range(M):
        if row[j]==1:
            ripe.append([i,j])
    box.append(row)

print(bfs(ripe))


