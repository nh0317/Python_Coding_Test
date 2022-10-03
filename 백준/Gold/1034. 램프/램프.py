import sys
from collections import Counter

input = sys.stdin.readline

N, M = map(int, input().split())

lamps = []
checks = []
dp = [0 for _ in range(M+1)]
m=0
for i in range(N):
    row = input().rstrip()
    lamps.append(list(map(int, row)))
    checks.append(int(row, 2))

K = int(input())

checks = Counter(checks)
maxx = 0
for key in checks.keys():
    k=format(key,'0'+str(len(lamps[0]))+'b').count('0')
    if k <= K and k %2 == K %2:
        maxx = max(maxx, checks[key])

print(maxx)
