def make_filter(skill, m, n):
    filters = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            degree *= -1

        filters[r1][c1] += degree
        filters[r1][c2+1] += degree * -1
        filters[r2+1][c1] += degree * -1
        filters[r2+1][c2+1] += degree
    
    for i in range(len(filters)):
        for j in range(1, len(filters[0])):
            filters[i][j] += filters[i][j-1]
            
    for i in range(1, len(filters)):
        for j in range(len(filters[0])):
            filters[i][j] += filters[i-1][j]
    
    return filters
    
def solution(board, skill):
    answer = 0
    filters = make_filter(skill, len(board[0]), len(board))
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += filters[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer