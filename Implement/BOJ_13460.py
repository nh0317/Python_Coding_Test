import sys
from collections import deque

def init():
    rx,ry,by,bx=0,0,0,0
    for i in range(M):
        for j in range(N):
            if board[i][j]=='B':
                by,bx=i,j
            if board[i][j]=='R':
                ry,rx=i,j
    return ry, rx, by, bx

def move(y,x,i):
    cnt=0
    while board[y+dy[i]][x+dx[i]]!='#' and board[y][x]!='O':
        y+=dy[i]
        x+=dx[i]
        cnt+=1
    return y,x,cnt

def play(ry,rx,by,bx,pcnt):
    q=deque([[ry,rx,by,bx,pcnt]])
    while q:
        ry,rx,by,bx,pcnt=q.popleft()
        if pcnt > 10:
            return -1
        if [ry,rx,by,bx] not in visited:
            visited.append([ry,rx,by,bx])
            for i in range(4):
                nry,nrx,rcnt=move(ry,rx,i)
                nby,nbx,bcnt=move(by,bx,i)
                if board[nby][nbx] != 'O' and board[nry][nrx] == 'O':
                    return pcnt
                elif board[nry][nrx] != 'O':
                    if(nry == nby and nrx==nbx):
                        if rcnt>bcnt:
                            nry-=dy[i]
                            nrx-=dx[i]
                        else :
                            nby-=dy[i]
                            nbx-=dx[i]

                    if [nry,nrx,nby,nbx] not in visited:
                        q.append([nry,nrx,nby,nbx,pcnt+1])
    return -1

input = sys.stdin.readline
M, N = map(int, input().split())
board = [[n for n in input().rstrip()] for _ in range(M)]

dy=[-1,1,0,0]
dx=[0,0,-1,1]
visited=[]
ry,rx,by,bx=init()
print(play(ry,rx,by,bx,1))
