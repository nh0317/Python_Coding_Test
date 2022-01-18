import sys
from collections import deque

def day_of_ripe(ripes):
    que=deque(ripes)
    day=-1
    visited=[[[False for _ in range(M)]for _ in range(N)]for _ in range(H)]
    dz=[1,-1,0,0,0,0]
    dy=[0,0,1,-1,0,0]
    dx=[0,0,0,0,1,-1]
    while que:
        day+=1
        for _ in range(len(que)):
            z,y,x=que.popleft()
            if not visited[z][y][x]:
                visited[z][y][x]=True
                for j in range(6):
                    nz,ny,nx=z+dz[j],y+dy[j],x+dx[j]
                    if 0<=nz<H and 0<=ny<N and 0<=nx<M:
                            if tomatoes[nz][ny][nx]==0:
                                tomatoes[nz][ny][nx]=1
                                que.append([nz,ny,nx])
    for a in tomatoes:
        for b in a:
            if 0 in b:
                day=-1
    return day

input = sys.stdin.readline

M,N,H=map(int, input().split())
#1 : 익은 토마토 0: 익지 않은 토마토 -1: 토마토X
tomatoes = [ [] for _ in range(H)]
ripes=set()
for i in range(H):
    for j in range(N):
        row = list(map(int,input().split()))
        tomatoes[i].append(row)
        for k in range(M):
            if tomatoes[i][j][k]==1:
                ripes.add((i,j,k))

print(day_of_ripe(ripes))






