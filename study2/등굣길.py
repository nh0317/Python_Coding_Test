def solution(m, n, puddles):
    board = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for x, y in puddles:
        board[y][x] = -1

    for i in range(1, m + 1):
        if board[1][i] == -1:
            break
        else:
            dp[1][i] = 1

    for i in range(1, n + 1):
        if board[i][1] == -1:
            break
        else:
            dp[i][1] = 1

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            if board[i][j] == -1:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    return dp[n][m]