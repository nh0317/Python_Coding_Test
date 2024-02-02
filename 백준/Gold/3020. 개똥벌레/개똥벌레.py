import sys
from collections import Counter

input = sys.stdin.readline

N, H = map(int, input().split())
up = [0 for _ in range(H)]
down = [0 for _ in range(H)]

for i in range(N):
    h = int(input())
    #석순
    if i % 2 == 0:
        up[h-1] += 1

    #종유석
    else:
        down[h-1] += 1

for i in range(H-2,-1,-1):
    # down[i] = down[i] + down[i-1]
    up[i] += up[i+1]
    down[i] += down[i+1]

down.reverse()
result = sorted(Counter(a+b for a, b in zip(down, up)).items(), key=lambda x:x[0])
print(result[0][0], result[0][1])

