import sys
from collections import deque

input=sys.stdin.readline

M=0
def printArr(arr):
    global M
    for i in range(M):
        for j in range(N):
            print(arr[i][j],end=" ")
        print()
    print()

def normal():
    visited = [[False for _ in range(N)] for _ in range(N) ]
    dy=[0,0,1,-1]
    dx=[1,-1,0,0]
    area=0
    que=deque()
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                que.append([i,j])
                visited[i][j]=True
                area+=1
                while que:
                    y,x=que.popleft()
                    for k in range(4):
                        ny,nx=y+dy[k],x+dx[k]
                        if 0<=ny<N and 0<=nx<N:
                            if not visited[ny][nx]:
                                if image[y][x] == image[ny][nx]:
                                    visited[ny][nx]=True
                                    que.append([ny,nx])
    return area

def color_blindness():
    visited = [[False for _ in range(N)] for _ in range(N) ]
    dy=[0,0,1,-1]
    dx=[1,-1,0,0]
    area=0
    que=deque()
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                que.append([i,j])
                visited[i][j]=True
                area+=1
                while que:
                    y,x=que.popleft()
                    for k in range(4):
                        ny,nx=y+dy[k],x+dx[k]
                        if 0<=ny<N and 0<=nx<N:
                            if not visited[ny][nx]:
                                if image[y][x] == 'R' and image[ny][nx]=='G':
                                    visited[ny][nx]=True
                                    que.append([ny,nx])
                                elif image[y][x] == 'G' and image[ny][nx]=='R':
                                    visited[ny][nx]=True
                                    que.append([ny,nx])
                                elif image[y][x]==image[ny][nx]:
                                    visited[ny][nx]=True
                                    que.append([ny,nx])
    return area

N = int(input())
image = [list(input().rstrip())for _ in range(N)]
print(normal(), color_blindness())