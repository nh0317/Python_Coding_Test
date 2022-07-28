import sys

input = sys.stdin.readline

N, M = map(int, input().split())

know = set(map(int, input().split()[1:]))

parties = [0]+[set(map(int, input().split()[1:])) for _ in range(M)]

for _ in range(M):
    for i in range(1,M+1):
        if know.intersection(parties[i]):
            know = parties[i].union(know)

cnt = 0
for i in range(1, M + 1):
    if know.intersection(parties[i]):
        continue
    else:
        cnt +=1

print(cnt)