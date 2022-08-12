import sys
import itertools

input = sys.stdin.readline

N, M = map(int, input().split())

class CCTV:
    def __init__(self, dir1=-1, dir2=-1, dir3=-1, dir4=-1):
        self.dir = [-1 for _ in range(4)]
        self.dir[0] = dir1
        self.dir[1]=dir2
        self.dir[2]= dir3
        self.dir[3]=dir4

    def move(self, y, x, dir):
        global mapp
        global directions
        global visited
        cnt = 0
        while 0 <= y + directions[dir][0] < N and 0 <= x + directions[dir][1] < M:
            y += directions[dir][0]
            x += directions[dir][1]
            if mapp[y][x] == 6:
                break
            elif not visited[y][x] and mapp[y][x] == 0:
                cnt += 1
                visited[y][x] = True
        return cnt

    def count(self,y,x):
        cnt = 0
        for d in self.dir:
            if d != -1:
                cnt += self.move(y,x,d)
        return cnt

    def turn(self,num):
        self.dir[0] = num
        for i in range(1,4):
            if self.dir[i] != -1:
                self.dir[i] = (self.dir[0] + i) % 4


mapp = [[0 for _ in range(M)] for _ in range(N)]

# 0 :  상 1: 오 2: 하 3: 좌
directions = [[-1,0],[0,1],[1,0],[0,-1]]
cctvs = []
walls = 0

for i in range(N):
    row = list(map(int, input().split()))
    for j, r in enumerate(row):
        mapp[i][j] = r
        if 0<r<6:
            cctvs.append([r,i,j])
        elif r == 6:
            walls += 1

maxx = 0
for turns in set(itertools.product([0,1,2,3],repeat=len(cctvs))):
    cnt = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    cctv_num = [CCTV(0),CCTV(0,-1,2),CCTV(0,1), CCTV(0,1,2), CCTV(0,1,2,3)]
    for i,value in enumerate(cctvs):
        cctv, y, x = value
        cctv_num[cctv-1].turn(turns[i])
        cnt+=cctv_num[cctv-1].count(y,x)
    maxx = max(cnt, maxx)

print(max(N*M-maxx-len(cctvs)-walls,0))