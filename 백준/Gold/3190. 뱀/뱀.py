import sys
from collections import deque

input = sys.stdin.readline

# 뱀 길이가 늘어남
# 기어다니다가 몸 또는 벽에 부딪히면 게임 끝
# 머리를 다음칸에
# 이동한 칸에 사과가 있으면 사과 없어지고 꼬리는 움직이지 않음
# 사과 X -> 꼬리가 위치한 칸을 비워줌

def bfs():
    global mapp
    global directions
    global dydx

    snake = deque([[0,0]])
    q = deque()
    t = 0
    q.append([0,0,t,0])
    while q:
        y,x,t,d = q.popleft()
        if directions and directions[-1][0] == t:
            if directions[-1][1] == "D":
                d = (d + 1)%4
            elif directions[-1][1] == "L":
                d = (4 + d - 1)%4
            directions.pop()

        ny, nx = y+dydx[d][0], x+dydx[d][1]
        if 0<=ny<len(mapp) and 0<=nx<len(mapp[0]):
            if [ny,nx] in snake:
                break
            snake.append([ny,nx])
            if mapp[ny][nx] == 1:
                mapp[ny][nx] = 0
            else:
                snake.popleft()
            q.append([ny,nx,t+1,d])
        else:
            break
    return t+1

N = int(input())
K = int(input())
mapp = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(K):
    i,j = map(int, input().split())
    mapp[i-1][j-1] = 1

dydx = [[0,1],[1,0],[0,-1],[-1,0]]

directions = []
L = int(input())
for _ in range(L):
    x, c = input().split()
    directions.append([int(x),c])
directions.sort(reverse=True)
print(bfs())