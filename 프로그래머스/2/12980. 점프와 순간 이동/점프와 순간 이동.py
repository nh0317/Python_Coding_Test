import sys
sys.setrecursionlimit(10**8)

minn = float('inf')
def dfs(i,battery):
    global minn 
    if i == 0:
        minn = min(minn, battery)
        return
    
    if i % 2 == 1:
        dfs(i-1, battery+1)
    else : 
        dfs(i//2, battery)

def solution(n):
    global minn 
    dfs(n, 0)
    
    return minn 