def solution(n, s, a, b, fares):
    D = [[float('inf') for _ in range(n)] for _ in range(n)]
    
    for u, v, w in fares:
        D[u-1][v-1] = w
        D[v-1][u-1] = w
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j : 
                    D[i][j] = 0
                else:
                    D[i][j] = min(D[i][j], D[i][k]+D[k][j])
                    
    minn = float('inf')
    for i in range(n):
        minn = min(minn, D[s-1][i]+D[i][a-1]+D[i][b-1])
    
    return minn