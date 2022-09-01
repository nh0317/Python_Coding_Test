import sys


input = sys.stdin.readline
N = int(input())
dp = [[0 for _ in range(N+1)] for _ in range(N)]
dp[1][1] = 2

for i in range(2,N):
    for j in range(1,i+1):
        dp[i][j] = (dp[i-1][j] * 2 + dp[i-1][j-1] + dp[i-1][j+1]) % 10007

# print(dp)
print(sum(dp[N-1])% 10007)