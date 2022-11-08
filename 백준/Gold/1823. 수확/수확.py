import sys

input = sys.stdin.readline

N = int(input())
rice = [0]
for i in range(N):
    rice.append(int(input()))

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1,len(dp)):
    dp[i][i] = rice[i] * N

for j in range(1, N+1):
    for i in range(j-1, 0, -1):
        cnt = N - (j - i)
        dp[i][j] = max(dp[i+1][j] + rice[i] * cnt, dp[i][j-1] + rice[j] * cnt)

print(dp[1][N])