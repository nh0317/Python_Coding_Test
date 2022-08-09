import sys
input = sys.stdin.readline

R, C, Q = map(int, input().split())

picture = [[0 for _ in range(C+2)]for _ in range(R+2)]

for i in range(1,R+1):
    tmp = list(map(int, input().split()))
    picture[i][1] = tmp[0]
    for j in range(2,C+1):
        picture[i][j] = picture[i][j-1] + tmp[j-1]

    if i > 1:
        for j in range(1,C+1):
            picture[i][j] += picture[i-1][j]


points = [list(map(int, input().split())) for _ in range(Q)]
average = [0 for _ in range(Q)]
for n, point in enumerate(points):
    y1, x1, y2, x2 = point
    average[n] = picture[y2][x2] - picture[y1-1][x2] - picture[y2][x1-1] + picture[y1-1][x1-1]
    average[n] //= (x2-x1+1) *(y2-y1+1)

for avg in average:
    print(avg)