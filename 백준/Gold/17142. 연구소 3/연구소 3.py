import sys
import itertools
from collections import deque

input = sys.stdin.readline

def bfs(virus):
    global N
    global lab
    global minn
    global total
    q = deque([])
    visited = [[False for _ in range(N)] for _ in range(N)]
    for y, x in virus:
        visited[y][x] = True
        q.append([y,x])

    spread = 0
    cnt = -1
    nextt = set()
    while q:
        cnt += 1
        if cnt >= minn:
            break
        if spread == total:
            return cnt, spread
        while q:
            y, x = q.popleft()
            for dy, dx in [[1,0],[-1,0],[0,1],[0,-1]]:
                ny, nx = y+dy, x + dx
                if 0<= ny < N and 0<= nx <N:
                    if not visited[ny][nx] and lab[ny][nx] == 0:
                        spread += 1
                        visited[ny][nx] = True
                        nextt.add((ny, nx))
                    elif not visited[ny][nx] and lab[ny][nx] == 2:
                        visited[ny][nx] = True
                        nextt.add((ny, nx))

        q.extend(nextt)
        nextt = set()

    return cnt, spread


N, M = map(int, input().split())
lab = [[0 for _ in range(N)] for _ in range(N)]
virus = set()
walls = 0
for i in range(N):
    row = list(map(int, input().split()))
    for j,r in enumerate(row):
        lab[i][j] = r
        if r == 2:
            virus.add((i,j))
        if r == 1:
            walls += 1

minn = float('inf')
checks = [[] for _ in range(len(virus))]
total = N * N - len(virus) - walls
for place in set(itertools.combinations(virus, M)):
    cnt, spread = bfs(place)
    if spread == total:
        minn = min(minn, cnt)

print(minn) if minn != float('inf') else print(-1)

