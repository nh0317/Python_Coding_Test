import sys
from collections import deque, defaultdict

def bfs(y,x,iceberg, visited):
    que=deque([[y,x]])
    melted=defaultdict(int)
    while que:
        y,x=que.popleft()
        if not visited[y][x]:
            visited[y][x]=True
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if (0 <= nx < N and 0 <= ny < M and not visited[ny][nx]):
                    # 빙하 녹이기
                    if (iceberg[ny][nx] == 0):
                        melted[(y, x)] += 1

                    else:
                        que.append([ny,nx])
    return melted

input=sys.stdin.readline
M, N = map(int, input().split())
iceberg = [list(map(int, input().split()))for _ in range(M)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]

year=0
while True:
    visited=[[False for _ in range(N)]for _ in range(M)]
    cnt=0
    for i in range(M):
        for j in range(N):
            if iceberg[i][j]!=0 and not visited[i][j]:
                cnt+=1
                melted=bfs(i,j,iceberg,visited)

    if cnt==0 or cnt >=2:
        break

    for (y, x), melting in melted.items():
        if iceberg[y][x] < melting:
            iceberg[y][x] = 0
        else: iceberg[y][x] = iceberg[y][x]-melting
    year+=1

if cnt ==0:
    print(0)
else: print(year)