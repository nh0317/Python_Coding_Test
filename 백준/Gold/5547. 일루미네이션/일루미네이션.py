import sys
from collections import deque

input = sys.stdin.readline

even_dydx = [[0, 1], [0, -1], [-1, -1], [1, 0], [-1, 0], [1, -1]]
odd_dydx = [[0, 1], [0, -1], [-1, 0], [1, 1], [-1, 1], [1, 0]]

def outside():
    global buildings
    global even_dydx
    global odd_dydx

    q = deque()
    q.append([0,0])
    visited = [[False for _ in range(len(buildings[0]))] for _ in range(len(buildings))]
    visited[0][0] = True
    buildings[0][0] = 2

    while q:
        y, x = q.popleft()
        if y % 2 == 0:
            move(even_dydx, q, visited, x, y)
        else:
            move(odd_dydx, q, visited, x, y)

def decorate(y,x, visited):
    q = deque()
    q.append([y,x])
    visited[y][x] = True
    cnt = 0

    while q:
        y, x = q.popleft()
        if y % 2 == 0:
            cnt += count(even_dydx, q, visited,x,y)
        else:
            cnt += count(odd_dydx, q, visited, x, y)
    return cnt

def count(dydx, q, visited, x, y):
    global buildings
    global even_dydx
    global odd_dydx

    cnt = 0
    for dy, dx in dydx:
        ny, nx = y + dy, x + dx
        if 0 <= ny < len(buildings) and 0 <= nx < len(buildings[0]):
            if not visited[ny][nx] and buildings[ny][nx] == 1:
                visited[ny][nx] = True
                q.append([ny, nx])
            elif buildings[ny][nx] == 2:
                cnt += 1
    return cnt


def move(dydx, q, visited, x, y):
    global buildings
    for dy, dx in dydx:
        ny, nx = y + dy, x + dx
        if 0 <= ny < len(buildings) and 0 <= nx < len(buildings[0]):
            if not visited[ny][nx] and buildings[ny][nx] == 0:
                buildings[ny][nx] = 2
                visited[ny][nx] = True
                q.append([ny, nx])
    return q

W, H = map(int, input().split())
buildings = [[0 for _ in range(W+2)]]
for _ in range(H):
    buildings.append([0]+list(map(int, input().split()))+[0])
buildings.append([0 for _ in range(W+2)])

outside()
visited = [[False for _ in range(len(buildings[0]))] for _ in range(len(buildings))]
cnt = 0

for i in range(len(buildings)):
    for j in range(len(buildings[0])):
        if not visited[i][j] and buildings[i][j] == 1:
            cnt += decorate(i,j,visited)

print(cnt)