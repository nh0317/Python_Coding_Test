import sys

input = sys.stdin.readline

N, S, M = map(int, input().split())
dV = list(map(int, input().split()))
dp = [[False for _ in range(M+1)] for _ in range(N+1)]

dp[0][S] = True

for i in range(N):
    for j in range(M+1):
        if dp[i][j]:
            if j + dV[i] <= M:
                dp[i+1][j+dV[i]] = True
            if j - dV[i] >= 0:
                dp[i+1][j-dV[i]] = True

answer = -1
for i in range(M,-1,-1):
    if dp[N][i]:
        answer = i
        break

print(answer)
