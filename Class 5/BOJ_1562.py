import sys

input = sys.stdin.readline
N=int(input())

mask=(1<<10)-1
mod=1000000000

dp = [[[0 for _ in range(1<<10)]for _ in range(10)]for _ in range(N+1)]
#dp[n][last][bit]
#마지막 숫자가 last 인 n자리 자연수 bit는 0~9를 썼는가

for i in range(10):
    dp[1][i][1<<i]=1

for i in range(2,N+1):
    for j in range(10):
        for k in range(1,mask+1):
            if j==0:
                dp[i][j][k | (1<<j) ] = (dp[i][j][k|(1<<j)] + dp[i-1][j+1][k]) % mod
            elif j==9:
                dp[i][j][k|(1<<j)] = (dp[i][j][k|(1<<j)] + dp[i-1][j-1][k]) % mod
            else:
                dp[i][j][k|(1<<j)] = (dp[i][j][k|(1<<j)] + dp[i-1][j-1][k]) % mod
                dp[i][j][k|(1<<j)] = (dp[i][j][k|(1<<j)] + dp[i-1][j+1][k]) % mod

answer=0
for j in range(1,10):
    answer = (answer+ dp[N][j][mask]) % mod

print(answer)


