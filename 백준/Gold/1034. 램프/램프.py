import sys
from collections import Counter, defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

lamps = []
checks = defaultdict(int)
dp = [0 for _ in range(M+1)]
m=0
for i in range(N):
    row = input().rstrip()
    lamps.append(list(map(int, row)))
    checks[row] += 1

K = int(input())

maxx = 0
for key in checks.keys():
    k=key.count('0')
    if k <= K and k %2 == K %2:
        maxx = max(maxx, checks[key])

print(maxx)
