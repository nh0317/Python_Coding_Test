import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    que = deque([[0, 0, 1, False]])
    visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(2)]
    visited[0][0][0]=True
    while que:
        # print(que)
        y, x, cnt, if_break = que.popleft()

        if y == N-1 and x == M-1:
            global min_distance
            min_distance = min(min_distance, cnt)

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0<= ny <N and 0<= nx<M:
                if if_break and not visited[1][ny][nx]:
                    if maps[ny][nx] == 0:
                        que.append([ny, nx, cnt+1, if_break])
                        visited[1][ny][nx] = True
                elif not if_break and not visited[0][ny][nx]:
                    if maps[ny][nx] == 1:
                        que.append([ny, nx, cnt+1, True])
                        visited[1][ny][nx] = True
                    if maps[ny][nx] == 0:
                        que.append([ny, nx, cnt+1, if_break])
                        visited[0][ny][nx] = True



N, M = map(int, input().split())
maps = [[int(x) for x in input().rstrip()] for _ in range(N)]
# print(maps)
min_distance=float('inf')
bfs()
print(min_distance if min_distance!= float('inf') else -1)
