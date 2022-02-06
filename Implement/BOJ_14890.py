import sys

def move(y,x,dy,dx):
    while x < M and y<M and board[y-dy][x - dx] == board[y][x]:
        x = x + dx
        y = y + dy
    return y, x

def slope_x(y,x):
    #위에서 아래로
    if board[y][x-1] - board[y][x] == 1:
        for j in range(L):
            if x+j>=M:
                return False
            elif board[y][x] != board[y][x + j] or visited[y][x+j]:
                return False
        for j in range(L):
            visited[y][x+j]=True
        return y, x+L
        #아래에서 위로
    if board[y][x-1] - board[y][x] == -1:
        for j in range(L):
            if x - j - 1<0:
                return False
            elif board[y][x - 1] != board[y][x - j-1] or (visited[y][x - j - 1]):
                return False
        for j in range(L):
            visited[y][x-j-1]=True
        return y, x+1
    return False

def slope_y(y,x):
    if board[y-1][x] - board[y][x] == 1:
        for j in range(L):
            if y+j>=M:
                return False
            elif board[y][x] != board[y+j][x] or visited[y+j][x]:
                return False
        for j in range(L):
            visited[y+j][x]=True
        return y+L,x
    elif board[y-1][x] - board[y][x] == -1:
        for j in range(L):
            if y-j-1<0:
                return False
            elif board[y-1][x] != board[y-j-1][x] or visited[y-j-1][x]:
                return False
        for j in range(L):
            visited[y-j-1][x]=True
        return y+1,x
    return False

input = sys.stdin.readline
M, L = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(M)]
visited = [[False for _ in range(M)]for _ in range(M)]
# print(board)
answer=0
for i in range(M):
    x = 1
    check=True
    while check and x < M and (board[i][x - 1] == board[i][x] or abs(board[i][x - 1] - board[i][x])==1):
        y,x=move(i,x,0,1)
        if x!=M:
            check = slope_x(i,x)
            if check:
                y,x=check
    if x >= M:
        answer=answer+1
    else:
        for j in range(M):
            visited[i][j]=False

check=True
visited = [[False for _ in range(M)]for _ in range(M)]
for i in range(M):
    y = 1
    check=True
    while check and  y < M and (board[y-1][i] == board[y][i] or abs(board[y-1][i] - board[y][i])==1):
        y,x=move(y,i,1,0)
        if y!=M:
            check = slope_y(y,i)
            if check:
                y,x=check
    if y >= M:
        answer=answer+1
    else:
        for j in range(M):
            visited[j][i]=False
            
print(answer)