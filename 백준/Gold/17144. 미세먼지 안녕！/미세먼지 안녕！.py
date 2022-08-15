import sys

input = sys.stdin.readline

R, C, T = map(int, input().split())

def print_arr(arr):
    for row in arr:
        for a in row:
            print(a, end=" ")
        print()
    print()

class Air_Cleaner:
    def __init__(self, point1=[0, 0], point2=[0, 0]):
        if point1[0] < point2[0]:
            self.upper = point1
            self.lower = point2
        else:
            self.upper, self.lower = point2, point1

    def blow(self):
        global mapp
        right_bottom = mapp[self.upper[0]][-1]
        right_top = mapp[0][-1]
        left_top = mapp[0][0]
        left_bottom = mapp[self.upper[0]][0]

        mapp[self.upper[0]][1:] = mapp[self.upper[0]][0:-1]

        for i in range(0, self.upper[0] - 1):
            mapp[i][-1] = mapp[i + 1][-1]

        mapp[0][:-2] = mapp[0][1:-1]

        for i in range(self.upper[0], 1, -1):
            mapp[i][0] = mapp[i - 1][0]

        if self.upper[0] > 0:
            mapp[self.upper[0] - 1][-1] = right_bottom
        mapp[0][-2] = right_top
        mapp[1][0] = left_top
        mapp[self.upper[0]][1] = left_bottom

        mapp[self.upper[0]][self.upper[1]] = -1
        if self.upper[1] + 1 < len(mapp[0]):
            mapp[self.upper[0]][self.upper[1]+1] = 0


        right_top = mapp[self.lower[0]][-1]
        right_bottom = mapp[-1][-1]
        left_top = mapp[self.lower[0]][0]
        left_bottom = mapp[-1][0]

        mapp[self.lower[0]][1:] = mapp[self.lower[0]][0:-1]

        for i in range(len(mapp)-1,self.lower[0], -1):
            mapp[i][-1] = mapp[i - 1][-1]

        mapp[-1][:-2] = mapp[-1][1:-1]

        for i in range(self.lower[0],len(mapp)-1):
            mapp[i][0] = mapp[i + 1][0]

        if self.lower[0] > 0:
            mapp[self.lower[0] + 1][-1] = right_top
        mapp[-1][-2] = right_bottom
        mapp[-2][0] = left_bottom
        mapp[self.lower[0]][1] = left_top

        mapp[self.lower[0]][self.lower[1]] = -1
        if self.lower[1] + 1 < len(mapp[0]):
            mapp[self.lower[0]][self.lower[1]+1] = 0

        # print_arr(mapp)


mapp = [[0 for _ in range(C)] for _ in range(R)]
p = []
mess = set()
for i in range(R):
    row = map(int, input().split())
    for j,r in enumerate(row):
        if r == -1:
            p.append([i,j])
        if r > 0:
            mess.add((r,i,j))
        mapp[i][j] = r

air_cleaner = Air_Cleaner(p[0],p[1])

# print(mess)
for _ in range(T):
    # news = set()
    # print(mess)
    for i, m in enumerate(mess):
        cnt = 0
        mm, y, x = m
        if mm < 0:
            continue
        amount = mm // 5
        for dy, dx in [[1,0],[-1,0],[0,1],[0,-1]]:
            ny, nx = y+dy, x+dx
            if 0<= ny < R and 0<= nx < C:
                if mapp[ny][nx] != -1:
                    cnt += 1
                    mapp[ny][nx] += amount
                    # news.add((ny, nx))
        if cnt > 0:
            mapp[y][x] -= amount * cnt
            # mapp[y][x] = max(mapp[y][x] - (amount * cnt), 0)

    # print_arr(mapp)
    air_cleaner.blow()
    mess = set()
    for i in range(R):
        for j in range(C):
            if mapp[i][j] >= 5:
                mess.add((mapp[i][j], i, j))

print(sum(map(sum,mapp)) + 2)