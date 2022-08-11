import sys
import itertools

input = sys.stdin.readline

N, M = map(int, input().split())


def move(y, x, dir):
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

class CCTV1:
    def __init__(self):
        self.dir = 0

    def count(self,y,x):
        global mapp
        global directions
        global visited
        cnt = move(y,x,self.dir)
        return cnt

    def turn(self,num):
        self.dir = num


class CCTV2:
    def __init__(self):
        self.dir1 = 0
        self.dir2 = 2

    def count(self,y,x):
        global mapp
        global directions
        global visited
        cnt = move(y,x,self.dir1)
        cnt += move(y,x,self.dir2)
        return cnt

    def turn(self,num):
        self.dir1 = num
        self.dir2 = (self.dir1 + 2) % 4


class CCTV3:
    def __init__(self):
        self.dir1 = 0
        self.dir2 = 1

    def count(self,y,x):
        global mapp
        global directions
        global visited
        cnt = move(y,x,self.dir1)
        cnt += move(y,x,self.dir2)
        return cnt

    def turn(self,num):
        self.dir1 = num
        self.dir2 = (self.dir1+1)%4

class CCTV4:
    def __init__(self):
        self.dir1 = 0
        self.dir2 = 1
        self.dir3 = 2


    def count(self,y,x):
        global mapp
        global directions
        global visited
        cnt = move(y,x,self.dir1)
        cnt += move(y,x,self.dir2)
        cnt += move(y,x,self.dir3)
        return cnt

    def turn(self,num):
        self.dir1 = num
        self.dir2 = (self.dir1+1)%4
        self.dir3 = (self.dir2+1)%4

class CCTV5:
    def __init__(self):
        self.dir1 = 0
        self.dir2 = 1
        self.dir3 = 2
        self.dir4 = 3


    def count(self,y,x):
        global mapp
        global directions
        global visited
        cnt = move(y,x,self.dir1)
        cnt += move(y,x,self.dir2)
        cnt += move(y,x,self.dir3)
        cnt += move(y,x,self.dir4)
        return cnt

    def turn(self,num):
        self.dir1 = num
        self.dir2 = (self.dir1+1)%4
        self.dir3 = (self.dir2+1)%4
        self.dir4 = (self.dir3+1)%4


# mapp = [list(map(int, input().split())) for _ in range(N)]
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
    cctv1 = CCTV1()
    cctv2 = CCTV2()
    cctv3 = CCTV3()
    cctv4 = CCTV4()
    cctv5 = CCTV5()
    for i,value in enumerate(cctvs):
        cctv, y, x = value
        if cctv == 1:
            cctv1.turn(turns[i])
            cnt += cctv1.count(y,x)
        elif cctv == 2:
            cctv2.turn(turns[i])
            cnt += cctv2.count(y,x)
        elif cctv == 3:
            cctv3.turn(turns[i])
            cnt += cctv3.count(y,x)
        elif cctv == 4:
            cctv4.turn(turns[i])
            cnt += cctv4.count(y,x)
        elif cctv == 5:
            cnt += cctv5.count(y,x)
    maxx = max(cnt, maxx)

print(max(N*M-maxx-len(cctvs)-walls,0))