from collections import deque

visited = []
def bfs(i,j, board):
    global visited
    q = deque()
    
    cnt = 0
    check = 0
    for dy, dx in [[0,1],[1,0],[1,1]]:
            ny, nx = i+dy, j+dx
            if 0<= ny < len(board) and 0<= nx < len(board[0]):
                if not visited[ny][nx] and board[i][j] == board[ny][nx]:
                    check += 1
    if check == 3:
        cnt += 4
        q.append([i, j])
        visited[i][j] = True
        if 0 <= ny < len(board) and 0 <= nx < len(board[0]):
            for dy, dx in [[0,1],[1,0],[1,1]]:
                ny, nx = i+dy, j+dx
                q.append([ny, nx])
                visited[ny][nx] = True
    while q:
        y,x = q.popleft()
        check = 0
        for dy, dx in [[0,1],[1,0],[1,1]]:
            ny, nx = y+dy, x+dx
            if 0<= ny < len(board) and 0<= nx < len(board[0]):
                if board[i][j] == board[ny][nx]:
                    check += 1
                    
        if check == 3:
            for dy, dx in [[0,1],[1,0],[1,1]]:
                ny, nx = y+dy, x+dx
                if 0 <= ny < len(board) and 0 <= nx < len(board[0]):
                    if not visited[ny][nx]:
                        q.append([ny, nx])
                        cnt += 1
                        visited[ny][nx] = True
    
    return cnt
def move(board):
    global visited
    for i in range(len(visited)-1,-1,-1):
        for j in range(len(visited[0])-1,-1,-1):
            if visited[i][j]:
                for k in range(i,-1,-1):
                    if not visited[k][j]:
                        tmp1, tmp2 = visited[i][j], board[i][j]
                        visited[i][j], board[i][j] = visited[k][j], board[k][j]
                        visited[k][j], board[k][j] = tmp1, tmp2
                        break
                
    return board
            
def solution(m, n, board):
    global visited
    answer = 0
    
    for i in range(len(board)):
        board[i] = list(board[i])
    
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    
    check = -1
    while check != 0:
        check = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if not visited[i][j]:
                    cnt= bfs(i,j,board)
                        
                    answer += cnt
                    check += cnt
        board=move(board)
    
    return answer