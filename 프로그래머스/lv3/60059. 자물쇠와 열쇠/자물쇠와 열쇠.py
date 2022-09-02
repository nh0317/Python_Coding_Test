
def rotate90(key):
    tmp = [[0 for _ in range(len(key))] for _ in range(len(key[0]))]
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j] == 1:
                tmp[j][-i-1] = 1
    return tmp

def push(y,x,n,key, board):
    cnt = 0
    h = min(y+len(key), n*2)
    w = min(x+len(key), n*2)
    for i in range(y, h):
        for j in range(x, w):
            if board[i][j] == 1 and key[i-y][j-x] == 1:
                if n <= i < n*2 and n <=j < n*2:
                    return 0
            elif board[i][j] == 0 and key[i-y][j-x] == 1:
                cnt += 1
    return cnt

def solution(key, lock):  
    board = [[1 for _ in range(len(lock)*3)] for _ in range(len(lock)*3)]
    n = len(lock)
    cnt = 0
    for i in range(n,n*2):
        for j in range(n,n*2):
            board[i][j] = lock[i-n][j-n]
            if lock[i-n][j-n] == 0:
                cnt+=1
            
    for i in range(n-len(key),n*2+len(key)):
        for j in range(n-len(key),n*2+len(key)):
            for _ in range(4):
                key = rotate90(key)
                match = push(i,j,n,key,board)
                if match == cnt:
                    return True
                
    return False