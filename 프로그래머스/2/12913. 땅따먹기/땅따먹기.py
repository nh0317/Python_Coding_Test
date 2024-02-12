
def solution(land):
    dp = [[x for x in land[y]] for y in range(len(land))]
    for i in range(1,len(land)):
        for j in range(len(land[i])):
            maxx = 0
            for k in range(len(land[i])):
                if j == k: continue
                maxx = max(maxx, dp[i-1][k])
            dp[i][j] += maxx
    
    return max(dp[-1])