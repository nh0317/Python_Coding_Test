import sys

input = sys.stdin.readline

def floyd(friends):
    for i in range(N):
        for j in range(N):
            if i == j:
                friends[i][j] = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                friends[i][j] = min(friends[i][j], friends[i][k] + friends[k][j])
    return friends

def pick(friends):
    scores = [max(friends[i]) for i in range(len(friends))]
    minn = min(scores)
    picked = []

    for i, score in enumerate(scores):
        if score == minn:
            picked.append(i+1)
    picked.sort()
    return minn, picked


N = int(input())
friends = [[float('inf') for _ in range(N)] for _ in range(N)]

u , v = 0, 0
while u != -1 and v != -1:
    u, v = map(int, input().split())
    friends[u-1][v-1] = 1
    friends[v-1][u-1] = 1

minn, candidate = pick(floyd(friends))

print(minn, len(candidate))
for c in candidate:
    print(c, end=" ")

