import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mapp = [ [int(x) for x in input().rstrip()] for _ in range(N)]
maxx = 0
for i in range(1,N):
    for j in range(M):
        if mapp[i][j] == 1:
            mapp[i][j] += mapp[i-1][j]

for i in range(N):
    mapp[i].sort(reverse= True)
    for j in range(M):
        area = mapp[i][j] * (j+1)
        maxx = max(area, maxx)

print(maxx)

