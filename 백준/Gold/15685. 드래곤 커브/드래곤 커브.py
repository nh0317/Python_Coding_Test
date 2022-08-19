import sys

input = sys.stdin.readline

N = int(input())
visited = [[False for _ in range(101)] for _ in range(101)]

def draw(y, x, n, d):
    global visited
    visited[y][x] = True

    curvs = []
    dydx = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    ny, nx = y + dydx[d][0], x + dydx[d][1]
    if 0 <= ny < 101 and 0 <= nx < 101:
        visited[ny][nx] = True
        curvs.append(d)

    nextt = []
    nextt.extend(curvs)
    for _ in range(n):
        while curvs:
            di = curvs.pop()
            nd = (di + 1) % 4
            ny, nx = ny + dydx[nd][0], nx + dydx[nd][1]
            if 0 <= ny < 101 and 0 <= nx < 101:
                visited[ny][nx] = True
                nextt.append(nd)
        curvs.extend(nextt)

for _ in range(N):
    x, y, d, g = map(int, input().split())
    draw(y,x,g,d)

cnt = 0
for i in range(100):
    for j in range(100):
        if visited[i][j] and visited[i][j+1] and \
                visited[i+1][j] and visited[i+1][j+1]:
            cnt += 1

print(cnt)



