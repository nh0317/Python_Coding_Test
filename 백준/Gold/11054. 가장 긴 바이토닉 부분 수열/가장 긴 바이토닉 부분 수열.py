import sys

input = sys.stdin.readline

N = int(input())
sequence = list(map(int, input().split()))
dp = [0 for _ in range(N)]
dp2 = [0 for _ in range(N)]

def dfs(i):
    if dp[i]: return dp[i]
    dp[i]=1
    cur = sequence[i]
    for j in range(i-1, -1,-1):
        if sequence[j] < cur:
            # cur=sequence[j]
            dp[i]=max(dp[i],dfs(j)+1)
    return dp[i]

def dfs2(i):
    if dp2[i]:return dp2[i]
    dp2[i]=1
    cur = sequence[i]

    for j in range(i + 1, N):
        if cur > sequence[j]:
            # cur=sequence[j]
            dp2[i]=max(dp2[i],dfs2(j)+1)

    return dp2[i]

max_cnt = 0
for i in range(N):
    max_cnt=max(max_cnt,dfs(i)+dfs2(i)-1)

# print(dp,dp2)
print(max_cnt)
