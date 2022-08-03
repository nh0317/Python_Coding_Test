import sys

input = sys.stdin.readline

def floyd(friends):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                friends[i][j] = min(friends[i][j], friends[i][k] + friends[k][j])
    return friends

def cal_scores(friends):
    scores = [0 for _ in range(N)]
    for i,friend in enumerate(friends):
        scores[i] = 0
        for f in friend:
            if f == float('inf'):
                continue
            if scores[i] < f:
                scores[i] = f
    return scores


N = int(input())
friends = [[float('inf') for _ in range(N)] for _ in range(N)]

u , v = 0, 0
while u != -1 and v != -1:
    u, v = map(int, input().split())
    friends[u-1][v-1] = 1
    friends[v-1][u-1] = 1

scores = cal_scores(floyd(friends))

minn = min(scores)
candidate = []

cnt = 0
for i, score in enumerate(scores):
    if score == minn:
        candidate.append(i)
        cnt += 1
candidate.sort()

print(minn, cnt)
for c in candidate:
    print(c+1, end=" ")

