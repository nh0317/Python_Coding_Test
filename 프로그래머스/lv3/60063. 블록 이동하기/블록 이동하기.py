from collections import deque

minn = float('inf')
# y1, x1가 축 
def turn_point1(y1,x1,y2,x2,d,p,board):
    N = len(board)
    if p == 0: # 가로인 경우 
        ny, nx = y1+d, x1+1
        if 0 <= ny < N and nx < N and 0<= y2 +d < N:
            point1, point2 = sorted(([y1, x1], [y2+d, x1]))
            y1, x1 = point1
            y2, x2 = point2
            if board[ny][nx] == 0 and board[y1][x1] == 0 and board[y2][x2] == 0:
                return y1, x1, y2,x2, 1
    elif p == 1:
        ny, nx = y1+1, x1 + d
        if ny < N and 0<= nx < N and 0<= x2 + d < N:
            point1, point2 = sorted(([y1, x1], [y1, x2+d]))
            y1, x1 = point1
            y2, x2 = point2
            if board[ny][nx] == 0 and board[y1][x1] == 0 and board[y2][x2] == 0:
                return y1, x1, y2,x2, 0
    return None
        
# y2, x2가 축 
def turn_point2(y1,x1,y2,x2,d,p,board):
    N = len(board)
    if p == 0:
        ny, nx = y2-d, x2-1
        if 0<= ny <N and nx >=0 and 0 <= y1-d < N:
            point1, point2 = sorted(([y1-d, x2], [y2, x2]))
            y1, x1 = point1
            y2, x2 = point2
            if board[ny][nx] == 0 and board[y1][x1] == 0 and board[y2][x2] == 0:
                return y1, x1, y2,x2, 1
    elif p == 1:
        ny, nx = y2-1, x2-d
        if ny >=0 and 0<=nx<N and 0 <= x1-d < N:
            point1, point2 = sorted(([y2, x1-d], [y2, x2]))
            y1, x1 = point1
            y2, x2 = point2
            if board[ny][nx] == 0 and board[y1][x1] == 0 and board[y2][x2] == 0:
                return y1, x1, y2,x2, 0
    return None

def check(y1,x1,y2,x2,board, visited):
    N=len(board)
    if 0<= y1 < N and 0<= x1 < N and 0<= y2<N and 0<= x2 < N:
        if board[y1][x1] == 0 and board[y2][x2] == 0:
            if (y1,x1,y2,x2) not in visited:
                return True
    return False

def bfs(board):
    global minn
    N = len(board)
    q = deque()
    q.append([0,0,0,1,0,0])
    visited = set()
    visited.add((0,0,0,1))
    while q:
        y1, x1, y2, x2,p, cnt = q.popleft()
        
        if (y1 == N-1 and x1 == N-1) or (y2 == N-1 and x2 == N-1):
            minn = min(minn, cnt)
            continue
        
        for dy, dx in [[1,0],[0,1],[-1,0],[0,-1]]:
            ny1, nx1 = y1 + dy, x1+dx
            ny2, nx2 = y2 + dy, x2+dx
            if check(ny1,nx1,ny2,nx2,board,visited):
                q.append([ny1,nx1,ny2,nx2,p,cnt+1])
                visited.add((ny1,nx1,ny2,nx2))
                
            # else:
            for d in [1,-1]:
                turn1 = turn_point1(y1,x1,y2,x2,d,p,board)   
                turn2 = turn_point2(y1,x1,y2,x2,d,p,board)
                if turn1 :
                    ny1, nx1, ny2, nx2, np = turn1
                    if check(ny1,nx1,ny2,nx2,board,visited):
                        q.append([ny1,nx1,ny2,nx2,np,cnt+1])
                        visited.add((ny1,nx1,ny2,nx2))

                if turn2 :
                    ny1, nx1, ny2, nx2, np = turn2
                    if check(ny1,nx1,ny2,nx2,board,visited):
                        q.append([ny1,nx1,ny2,nx2,np,cnt+1])
                        visited.add((ny1,nx1,ny2,nx2))
    
    

def solution(board):
    global minn
    bfs(board)
    print(minn)
    print(sorted([[1,0],[0,0]]))
    return minn