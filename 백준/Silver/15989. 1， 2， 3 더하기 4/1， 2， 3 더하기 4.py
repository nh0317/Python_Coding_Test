import sys

input = sys.stdin.readline

T= int(input())
dp = [[0 for _ in range(4)] for _ in range(10001)]
dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for _ in range(T):
    N = int(input())
    n= N
    for i in range(4,N+1):
        if dp[i][3] : continue
        dp[i][1] = 1
        dp[i][2] = dp[i-2][1]+dp[i-2][2]
        dp[i][3] = dp[i-3][1] + dp[i-3][2] + dp[i-3][3]
    print(sum(dp[N]))
