import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
maze =[[0 for j in range(M)]for i in range(N) ]

print(maze)

check = [[-1] * M for _ in range(N)]
check[0][0] = 0
queue = deque()
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
queue.append([0, 0])

while queue:
    print(queue)
    print(check)
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if check[ny][nx] == -1:
                if maze[ny][nx] == 0:
                    check[ny][nx] = 0
                    queue.appendleft([nx, ny])
                else:
                    check[ny][nx] = check[y][x] + 1
                    queue.append([nx, ny])


print(check[N-1][M-1])