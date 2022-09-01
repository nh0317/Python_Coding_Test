import itertools
import copy

board = []
def move(y, x, ny, nx):
    global board

    if y == ny and x == nx:
        return 0
    elif y != ny and x != nx:
        cnt1 = move_y(y, x, ny) + move_x(ny, x, nx)
        cnt2 = move_x(y, x, nx) + move_y(y, nx, ny)
        return min(cnt1, cnt2)
    elif y == ny:
        return move_x(y, x, nx)
    elif x == nx:
        return move_y(y, x, ny)


def move_y(y, x, ny):

    global board
    cnt = 0
    dy = -1
    if ny > y:
        dy = 1
    cury = y
    curx = x
    while y != ny:
        y, x = ctrl(y, x,ny,curx, dy, 0)
        if y == -1 and x == -1:
            y = cury + dy
            x = curx
        cury = y
        cnt += 1

    return cnt


def move_x(y, x, nx):
    global board
    cnt = 0
    dx = -1
    if nx > x:
        dx = 1
    curx = x
    cury = y
    while x != nx:
        y, x = ctrl(y, x,cury,nx, 0, dx)
        if y == -1 and x == -1:
            x = curx + dx
            y = cury
        curx = x
        cnt += 1
    return cnt

def ctrl(y,x,ny,nx,dy,dx):
    global board
    nny,nnx = y+dy,x+dx
    while 0<=nny<4 and 0<=nnx<4:
        if board[nny][nnx] != 0:
            return nny,nnx
        elif nny == ny and nnx == nx:
            if (nny == 3 or nny == 0) and dx == 0:
                return nny, nnx
            elif (nnx == 3 or nnx == 0) and dy == 0:
                return nny, nnx
            return -1, -1
        nny,nnx = nny+dy, nnx+dx
    return -1,-1

def solution(b, r, c):
    global board
    board = copy.deepcopy(b)
    
    card = [[] for _ in range(7)]
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                card[board[i][j]].append([i,j])
                cnt += 1
    cnt //= 2
    
    min_res = []
    minn = float('inf')
    orders = set(itertools.product([(0,1),(1,0)], repeat=cnt))

    for card_set in set(itertools.permutations([i+1 for i in range(cnt)])):
        for order in orders:
            op = 0
            y, x = r,c
            board = copy.deepcopy(b)
            for i in range(cnt):
                ny,nx = card[card_set[i]][order[i][0]]
                m = move(y,x,ny,nx)
                y,x = ny, nx
                op+= m 
                board[y][x] = 0
                
                ny,nx = card[card_set[i]][order[i][1]]
                m = move(y,x,ny,nx)
                y,x = ny, nx
                op+=m 
                board[y][x] = 0
            minn = min(minn, op)
    return minn + cnt * 2