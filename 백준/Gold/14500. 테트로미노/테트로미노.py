import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]


def dfs(y, x,w, cnt):
    global board
    global maxx
    global visited

    if cnt == 4:
        maxx = max(maxx, w)
        return

    else:
        for dy, dx in [[1,0],[-1,0],[0,1],[0,-1]]:
            ny, nx = y + dy, x +dx
            if 0<= ny < N and 0<= nx < M:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    dfs(ny, nx,w+board[ny][nx], cnt +1)
                    visited[ny][nx] = False


def ㅗ(y,x):
    global board
    global maxx

    shapes = [[[0,1],[0,-1],[1,0]],
             [[0,1],[0,-1],[-1,0]],
             [[1,0],[-1,0],[0,1]],
             [[1,0],[-1,0],[0,-1]]]

    for shape in shapes:
        weight = board[y][x]
        for dy, dx in shape:
            ny, nx = y + dy, x +dx
            if 0<= ny < N and 0<= nx < M:
                weight += board[ny][nx]
            else: break
        else:
            maxx = max(maxx, weight)


dfs_max = -1
maxx = -1
visited = [[False for _ in range(M)] for _ in range(N)]
board_path = []
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i,j,board[i][j],1)
            visited[i][j] = False
            ㅗ(i,j)

print(maxx)

