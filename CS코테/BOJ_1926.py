import sys
from collections import deque

input = sys.stdin.readline

def bfs(y, x, visited, board):
    dydx = [[1,0],[-1,0],[0,1],[0,-1]]
    q = deque([])
    q.append([y,x])
    visited[y][x] = True
    area = 0
    while q:
        area += 1
        cy, cx = q.popleft()
        for dy, dx in dydx:
            ny, nx = cy+dy, cx+dx
            if 0<= ny < N and 0<= nx < M:
                if not visited[ny][nx] and board[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append([ny, nx])
    return area

N, M = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

maxx = 0
cnt = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j] and board[i][j] == 1:
            cnt+=1
            area=bfs(i,j,visited, board)
            maxx = max(maxx, area)

print(cnt)
print(maxx)
