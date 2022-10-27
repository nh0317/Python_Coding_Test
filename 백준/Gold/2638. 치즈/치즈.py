from collections import deque

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(N)]

def check_air(y,x):
    global visited
    global mapp
    q = deque()
    q.append([y,x])

    while q:
        y, x = q.popleft()

        for dy, dx in [[1,0],[0,1],[0,-1],[-1,0]]:
            ny, nx = y + dy, x + dx
            if 0<=ny<len(mapp) and 0<= nx<len(mapp[0]):
                if not visited[ny][nx] and mapp[ny][nx] != 1:
                    q.append([ny,nx])
                    mapp[ny][nx] = 2
                    visited[ny][nx] = True

def melt():
    global visited
    global mapp
    melted = []

    for i in range(len(mapp)):
        for j in range(len(mapp[0])):
            if mapp[i][j] == 1:
                cnt = 0
                for dy, dx in [[1,0],[0,1],[-1,0],[0,-1]]:
                    ny, nx = i+dy, j+dx
                    if mapp[ny][nx] == 2:
                        cnt += 1
                if cnt >= 2:
                    melted.append([i,j])

    for y, x in melted:
        mapp[y][x] = 0
    if melted: return True
    else: return False

cnt = -1
while True:
    cnt += 1
    visited = [[False for _ in range(M)] for _ in range(N)]
    check = False
    for i in range(len(mapp)):
        for j in range(len(mapp[0])):
            if mapp[i][j] != 1:
                check_air(i,j)
                check = True
                break
        if check: break

    if not melt():
        break
print(cnt)