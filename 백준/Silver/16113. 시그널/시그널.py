import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
signals = list(input().rstrip())


def bfs(i, j):
    global m
    global board
    global visited
    q = deque()
    q.append([i, j])
    cnt = -1
    while q:
        y, x = q.popleft()
        cnt += 1
        for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < 5 and 0 <= nx < m:
                if board[ny][nx] != 0 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append([ny, nx])
    return cnt

m = N // 5
board = [[0 for _ in range(m)] for _ in range(5)]
visited = [[False for _ in range(m)] for _ in range(5)]

for i in range(5):
    for j in range(m):
        if signals[i*m+j] == "#":
            board[i][j] = 1

answer = ''

# 1:5 4:9, 7:7, 8:13
# 0:12, 6:12, 9:12
# 2:11 3:11, 5:11,
for j in range(m):
    if board[0][j] != 0 and not visited[0][j]:
        cnt = bfs(0,j)
        if cnt == 5:
            answer += '1'
        elif cnt == 9:
            answer += '4'
        elif cnt == 7:
            answer += '7'
        elif cnt == 13:
            answer += '8'

        elif cnt == 12:
            if board[2][1+j] == 0:
                answer += '0'
            elif board[1][2+j] == 0:
                answer += '6'
            else: answer += '9'

        elif cnt == 11:
            if board[1][j] == 0 and board[3][j] == 1:
                answer += '2'
            elif board[1][2+j] == 1 and board[3][2+j] == 1:
                answer += '3'
            else: answer += '5'

print(answer)