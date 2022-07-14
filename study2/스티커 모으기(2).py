def dp(dp):
    for i in range(1, len(dp)):
        if i < 2:
            dp[i] = max(dp[i], dp[i - 1])

        else:
            dp[i] = max(dp[i - 1], dp[i] + dp[i - 2])

    return dp[len(dp) - 1]


def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    answer = max(dp(sticker[1:]), dp(sticker[:-1]))
    return answer