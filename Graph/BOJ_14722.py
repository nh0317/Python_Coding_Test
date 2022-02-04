import sys

#맨 처음에는 딸기우유 한 팩
#딸기우유 -> 초코우유 -> 바나나 우유 -> 딸기우유
# 0->1->2

input = sys.stdin.readline
N = int(input())
cities = [[int(x) for x in input().split()]for _ in range(N)]
milk =[[0 for _ in range(N)]for _ in range(N)]

if cities[0][0]==0:
    milk[0][0]=1

for i in range(1,N):
    if milk[0][i-1] == 0 and cities[0][i]==0:
        milk[0][i]=1
    elif milk[0][i-1]!=0 and cities[0][i]==milk[0][i-1] % 3:
        milk[0][i]=max(milk[0][i],milk[0][i-1]+1)
    elif milk[0][i-1]!=0 and cities[0][i]!=milk[0][i-1] % 3:
        milk[0][i]=max(milk[0][i],milk[0][i-1])

for i in range(1,N):
    if milk[i-1][0] == 0 and cities[i][0]==0:
        milk[i][0]=1
    elif milk[i-1][0]!=0 and cities[i][0]==milk[i-1][0] % 3:
        milk[i][0]=max(milk[i][0],milk[i-1][0]+1)
    elif milk[i-1][0]!=0 and cities[i][0]!=milk[i-1][0] % 3:
        milk[i][0]=max(milk[i][0],milk[i-1][0])

# print(milk)

for i in range(1,N):
    for j in range(1,N):
        di = milk[i-1][j]%3
        if cities[i][j] == di:
            milk[i][j]=max(milk[i][j],milk[i-1][j]+1)
        else:
            milk[i][j]=max(milk[i][j],milk[i-1][j])
        di = milk[i][j-1] % 3
        if cities[i][j] == di:
            milk[i][j]=max(milk[i][j],milk[i][j-1]+1)
        else:
            milk[i][j]=max(milk[i][j],milk[i][j-1])
print(milk[N-1][N-1])

