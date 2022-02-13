import sys
import copy
import itertools

max_safe=-1

def spread(y,x,maze):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    if maze[y][x]==2:
        for i in range(4):
            ny=dy[i]+y
            nx=dx[i]+x
            if 0<=ny<N and 0<=nx<M and maze[ny][nx]!=1:
                if maze[y][x]==2 and maze[ny][nx]==0:
                    maze[ny][nx]=2
                    spread(ny,nx,maze)

def cnt_safe_zone(maze):
    cnt=0
    for i in range(N):
        for j in range(M):
            if maze[i][j]==0:
                cnt+=1
    return cnt

def bfs():
    walls = list(itertools.combinations(blank, 3))
    # print(blank)
    for i in range( len(walls)):
        maze=copy.deepcopy(initMaze)
        for x,y in walls[i]:
            maze[x][y]=1
        # print(maze)
        for y,x in virus:
            spread(y,x,maze)
        global max_safe
        max_safe=max(max_safe,cnt_safe_zone(maze))

# def select_walls(i):

# def select_walls(cnt):
#     if cnt ==3:
#         bfs()
#     else:
#         for i in range(N):
#             for j in range(M):
#                 if initMaze[i][j]==0:
#                     initMaze[i][j]=1
#                     select_walls(cnt+1)
#                     initMaze[i][j]=0

input=sys.stdin.readline

# 0 : 빈칸, 1: 벽, 2: 바이러스
N,M=map(int,input().rsplit())
initMaze=[list(map(int,input().rsplit())) for _ in range(N)]
virus=[]
blank=[]
for i in range(N):
    for j in range(M):
        if(initMaze[i][j]==2):
            virus.append([i,j])
        if(initMaze[i][j]==0):
            blank.append([i,j])
# select_walls(0)
bfs()
print(max_safe)

