from collections import deque
board = []
maxx = -1
flag = False

def move(board, loc, d):
    dydx = [[-1,0],[0,1],[1,0],[0,-1]]
    
    ny, nx = loc[0] + dydx[d][0], loc[1] + dydx[d][1]
    
    if 0 <= ny < len(board) and 0<=nx < len(board[0]):
        return ny, nx
    else:
        return -1, -1

# True : A turn, False: B Turn 
def dfs(turn, a, b, cnt):
    global board
    global flag
    result = []
    
    # print(turn, a, b, cnt)
    if board[a[0]][a[1]] == 0:
        return not turn, cnt
    if board[b[0]][b[1]] == 0:
        return turn, cnt
    
    win_a = False
    win_b = False
    for i in range(4):
        ny, nx = move(board, a, i)
        if ny!= -1 and nx != -1 and board[ny][nx] == 1:
            board[a[0]][a[1]] = 0
            win, length = dfs(not turn, b, [ny,nx], cnt + 1)
            board[a[0]][a[1]] = 1
            if win:
                win_a = True
            else:
                win_b = True
                
            result.append([win, length])
            
    
    if not result:
        flag = False
        return not turn, cnt
    
    elif (turn and win_a) or (not turn and win_b):
        minn = min(r[1] for r in result if r[0] == turn)
        # print('A turn and A will win',turn, result, minn)
        return turn, minn
    
    else:
        maxx = max(r[1] for r in result if r[0] != turn)
        # print('A turn and A will Lose',turn, result, maxx)
        return not turn, maxx
    
def solution(mapp, aloc, bloc):
    answer = -1
    global board
    board = mapp
    answer=dfs(True, aloc, bloc, 0)
    print(answer)
    return answer[1]