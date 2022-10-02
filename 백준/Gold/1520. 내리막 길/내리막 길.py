import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**5)

def dfs(y,x):
    global maps
    global dp
    if dp[y][x] != -1:
        return dp[y][x]

    if y == M-1 and x == N-1:
        return 1

    dp[y][x] = 0

    for dy, dx in [[1,0],[0,1],[-1,0],[0,-1]]:
        ny, nx = y+dy, x+dx
        if 0<= ny < M and 0<=nx <N:
            if maps[ny][nx] < maps[y][x]:
                dp[y][x] += dfs(ny,nx)

    return dp[y][x]

M, N =  map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]

dfs(0,0)
print(dp[0][0])