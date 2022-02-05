import sys
import itertools

# 0: 빈칸
# 1: 집
# 2: 치킨집
input=sys.stdin.readline
N,M=map(int,input().split())

homes=set()
chickens=set()

for i in range(N):
    city = list(map(int,input().split()))
    for j in range(len(city)):
        if city[j]==1:
            homes.add((i,j))
        if city[j]==2:
            chickens.add((i, j))

selected = list(itertools.combinations(chickens, M))

min_chicken=float('inf')

for c in selected:
    sum_d = 0
    for home in homes:
        hy,hx=home
        min_distance=float('inf')
        for cy, cx in c:
            d=abs(cy-hy)+abs(cx-hx)
            min_distance=min(min_distance,d)
        sum_d=sum_d+min_distance
    min_chicken=min(min_chicken,sum_d)

print(min_chicken)
