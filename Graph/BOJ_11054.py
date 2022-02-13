import sys

input = sys.stdin.readline

N = int(input())
sequence = list(map(int, input().split()))
dp_down = [0 for _ in range(N)]
dp_up = [0 for _ in range(N)]

def dfs_down(i):
    if dp_down[i]: return dp_down[i]
    dp_down[i]=1
    cur = sequence[i]
    for j in range(i-1, -1,-1):
        if sequence[j] < cur:
            dp_down[i]=max(dp_down[i], dfs_down(j) + 1)
    return dp_down[i]

def dfs_up(i):
    if dp_up[i]:return dp_up[i]
    dp_up[i]=1
    cur = sequence[i]

    for j in range(i + 1, N):
        if cur > sequence[j]:
            dp_up[i]=max(dp_up[i], dfs_up(j) + 1)

    return dp_up[i]

max_cnt = 0
for i in range(N):
    max_cnt=max(max_cnt, dfs_down(i) + dfs_up(i) - 1)

print(max_cnt)
