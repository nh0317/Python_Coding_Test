import sys

input = sys.stdin.readline

N = int(input())

profits = [0 for _ in range(N+1)]
costs = [0 for _ in range(N+1)]

for i in range(1,N+1):
    cost, profit = map(int, input().split())
    profits[i] = profit
    costs[i] = cost

# maxx = 0
# def dfs(day, profit):
#     global costs
#     global profits
#     global maxx
#     if day > N:
#         return
#
#     if day + costs[day] - 1 == N:
#         maxx = max(maxx, profit+profits[day])
#         dfs(day+1, profit)
#         return
#     elif day + costs[day] > N:
#         maxx = max(maxx, profit)
#         dfs(day+1, profit)
#         return
#     else:
#         dfs(day+1, profit)
#         dfs(day+costs[day], profit+profits[day])
#
# dfs(1,0)
# print(maxx)

dp = [0 for _ in range(N+1)]

for i in range(N-1, -1, -1):
    if i + costs[i+1] <= N:
        dp[i] = max(dp[i+1], dp[i+costs[i+1]]+profits[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])