import heapq
import math

def solution(alp, cop, problems):
    answer = 0
    max_alp = max(x[0] for x in problems)
    max_cop = max(x[1] for x in problems)
    
    if alp > max_alp and cop > max_cop:
        return 0
    elif alp > max_alp:
        alp = max_alp
    elif cop > max_cop:
        cop = max_cop 
    
    dp = [[float('inf') for _ in range(max_cop + 2)] for _ in range(max_alp + 2)]
    dp[alp][cop] = 0
    
    problems = sorted(problems, key = lambda x : x[0] + x [1])
    for i in range(alp,max_alp+1):
        for j in range(cop,max_cop+1):
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if alp_req <= i and cop_req <= j:
                    if i + alp_rwd > max_alp and j + cop_rwd > max_cop:
                        dp[max_alp][max_cop] = min(dp[max_alp][max_cop], dp[i][j]+cost)
                    elif i + alp_rwd <= max_alp and j + cop_rwd > max_cop:
                        dp[i + alp_rwd][max_cop] = min(dp[i + alp_rwd][max_cop], dp[i][j]+cost) 
                    elif i + alp_rwd > max_alp and j + cop_rwd <= max_cop:
                        dp[max_alp][j + cop_rwd] = min(dp[max_alp][j + cop_rwd], dp[i][j]+cost) 
                    elif i + alp_rwd <= max_alp and j + cop_rwd <= max_cop:
                        dp[i+alp_rwd][j+cop_rwd] = min(dp[i+alp_rwd][j+cop_rwd], dp[i][j]+cost) 
                    
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
    
    return dp[max_alp][max_cop]