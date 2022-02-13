import sys
from collections import deque

def dfs(y,x):
    next = [[1,0],[-1,0],[0,1],[0,-1]]
    if dp[y][x]: return dp[y][x]
    dp[y][x]=1
    for dy, dx in next:
        ny,nx=y+dy, x+dx
        if 0<=ny <N and 0<=nx< N:
            if bamboos[y][x]<bamboos[ny][nx]:
                dp[y][x]=max(dp[y][x],dfs(ny,nx)+1)
    return dp[y][x]

input = sys.stdin.readline

N = int(input())

bamboos = [list(map(int,input().split())) for _ in range(N)]

# dp[i][j] : 현재 위치에서 출발하여 가장 많이 움직일 수 있는 거리
dp=[[0 for _ in range(N)] for _ in range(N)]

answer=0
for i in range(N):
    for j in range(N):
        answer=max(answer,dfs(i,j))

print(answer)

