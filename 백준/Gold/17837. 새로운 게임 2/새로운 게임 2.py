import sys
from collections import defaultdict

input = sys.stdin.readline

class Player:
    def __init__(self,i,arr):
        self.y = arr[0] - 1
        self.x = arr[1] - 1
        self.d = arr[2] - 1
        self.idx = i

    def move(self):
        global mapp
        global dydx
        global points
        global players
        ny, nx = self.y + dydx[self.d][0], self.x + dydx[self.d][1]
        y, x = self.y, self.x
        
        if 0 <= ny < len(mapp) and 0 <= nx < len(mapp):
            if mapp[ny][nx] == 0:
                p = points[(self.y,self.x)]
                id = p.index(self.idx)
                
                for i in p[id:]:
                    players[i].x = nx
                    players[i].y = ny

                if p[id:]:
                    points[(ny, nx)].extend(p[id:])
                    points[(y,x)]=p[:id]

                if not points[(y,x)]:
                    points.pop((y, x))

            if mapp[ny][nx] == 1:
                p = points[(self.y,self.x)]
                id = p.index(self.idx)

                for i in p[id:]:
                    players[i].x = nx
                    players[i].y = ny
                if p[id:]:
                    r = p[id:]
                    r.reverse()
                    points[(ny, nx)].extend(r)
                    points[(y,x)]=p[:id]

                if not points[(y,x)]:
                    points.pop((y, x))

            if mapp[ny][nx] == 2:
                ny, nx = y - dydx[self.d][0], x - dydx[self.d][1]

                if self.d == 0:
                    self.d = 1
                elif self.d == 1:
                    self.d = 0
                elif self.d == 2:
                    self.d = 3
                elif self.d == 3:
                    self.d = 2

                if 0 <= ny < len(mapp) and 0 <= nx < len(mapp):
                    if mapp[ny][nx] != 2:
                        self.move()
        else:
            ny, nx = y - dydx[self.d][0], x - dydx[self.d][1]
            if self.d == 0: self.d = 1
            elif self.d == 1: self.d = 0
            elif self.d == 2: self.d = 3
            elif self.d == 3: self.d = 2

            if 0 <= ny < len(mapp) and 0 <= nx < len(mapp):
                if mapp[ny][nx] != 2:
                    self.move()

        if len(points[(self.y, self.x)]) >= 4:
            return True
        else: return False

dydx = [[0,1],[0,-1],[-1,0],[1,0]]

N, K = map(int, input().split())

mapp = [list(map(int, input().split())) for _ in range(N)]
players = []

points = defaultdict(list)
for i in range(K):
    y,x,d = map(int, input().split())
    points[(y-1,x-1)].append(i)
    players.append(Player(i, [y,x,d]))
cnt = 0
find = False
while not find:
    cnt += 1

    for p in players:
        if p.move():
            find = True

    if cnt > 1000:
        break

print(cnt) if cnt <= 1000 else print(-1)



