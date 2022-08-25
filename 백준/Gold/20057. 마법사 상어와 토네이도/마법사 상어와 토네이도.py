import sys

input = sys.stdin.readline

N = int(input())

sand = []
mapp = [[] for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    for j,r in enumerate(row):
        if r > 0:
            sand.append([r,i,j])
    mapp[i].extend(row)

y, x = N//2, N//2
dydx = [[0,-1],[1,0],[0,1],[-1,0]]
d = 0
cnt = 1
summ = 0
while 0<= y < N and 0<= x < N:
    for _ in range(cnt):
        y, x = y+dydx[d][0], x +dydx[d][1]

        s = 0
        out = 0
        if mapp[y][x] > 0:
            if 0<= y + dydx[d][0] * 2 <N and 0<= x + dydx[d][1] * 2<N:
                s += int(mapp[y][x] * 0.05)
                mapp[y + dydx[d][0] * 2][x + dydx[d][1] * 2] += s
            else:
                out += int(mapp[y][x] * 0.05)

            # 7%
            for i in (1,3):
                if 0<= y + dydx[(d+i)%4][0] <N and 0<= x + dydx[(d+i)%4][1]<N:
                    s += int(mapp[y][x] * 0.07)
                    mapp[y + dydx[(d+i)%4][0]][x + dydx[(d+i)%4][1]] += int(mapp[y][x] * 0.07)
                else: out += int(mapp[y][x] * 0.07)
            # 2%
            for i in (1,3):
                if 0<= y + dydx[(d+i)%4][0] * 2 <N and 0<= x + dydx[(d+i)%4][1] * 2<N:
                    s += int(mapp[y][x] * 0.02)
                    mapp[y + dydx[(d+i)%4][0]* 2][x + dydx[(d+i)%4][1]* 2]  += int(mapp[y][x] * 0.02)
                else: out += int(mapp[y][x] * 0.02)

            # 10
            for i in (1,3):
                if 0<= y + dydx[d][0] + dydx[(d+i)%4][0] <N and 0<= x + dydx[d][1] + dydx[(d+i)%4][1]<N:
                    s += int(mapp[y][x] * 0.1)
                    mapp[y + dydx[d][0] + dydx[(d+i)%4][0]][x + dydx[d][1] + dydx[(d+i)%4][1]] += int(mapp[y][x] * 0.1)
                else: out += int(mapp[y][x] * 0.1)

            # 1
            for i in (1,3):
                if 0<= y - dydx[d][0] + dydx[(d+i)%4][0] <N and 0<= x - dydx[d][1] + dydx[(d+i)%4][1]<N:
                    s += int(mapp[y][x] * 0.01)
                    mapp[y - dydx[d][0] + dydx[(d+i)%4][0]][x - dydx[d][1] + dydx[(d+i)%4][1]] += int(mapp[y][x] * 0.01)
                else: out += int(mapp[y][x] * 0.01)

            #a
            if 0<= y + dydx[d][0] <N and 0<= x + dydx[d][1]<N:
                mapp[y + dydx[d][0]][x + dydx[d][1]] += mapp[y][x] - s -out
                mapp[y][x] = 0
            else:
                out += mapp[y][x] - s - out
                mapp[y][x] = 0

        summ += out

    d = (d + 1) % 4
    if d == 2 or (cnt > 1 and (d == 2 or d == 0)):
        cnt+=1

print(summ)