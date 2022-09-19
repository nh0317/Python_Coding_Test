from collections import deque
import heapq

minn = float('inf')
dp = []

def dfs(y,x,d,cost,board):
    global minn
    global dp
            
    if y == len(board)-1 and x == len(board[0])-1:
        minn = min(minn, cost)
        return
    
    for i, dydx in enumerate([[1,0],[0,1],[-1,0],[0,-1]]):
        dy, dx = dydx
        ny, nx = dy+y, dx+x
        if 0<= ny < len(board) and 0<= nx < len(board[0]):
            if board[ny][nx] == 0 and cost + 100 < dp[ny][nx][i]:
                if d == -1 or d == i:
                    board[ny][nx]=2
                    dp[ny][nx][i] = min(dp[ny][nx][i],cost+100)
                    dfs(ny,nx,i,cost+100,board)
                    board[ny][nx]=0
                elif d != i:
                    board[ny][nx]=2
                    dp[ny][nx][i] = min(dp[ny][nx][i],cost+600)
                    dfs(ny,nx,i,cost+600,board)
                    board[ny][nx]=0
                        
def solution(board):
    global minn
    global dp
    
    dp = [[[float('inf') for _ in range(4)] for _ in range(len(board[0]))] for _ in range(len(board))]
    
    dfs(0,0,-1,0,board)
    return minn if minn != float('inf') else 0