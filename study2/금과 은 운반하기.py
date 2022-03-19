def solution(a, b, g, s, w, t):
    start = 0
    # 최대 광물의 수 * 2(금, 은) * 최대 왕복 시간
    end = 2 * (10 ** 9) * 2 * (10 ** 5)
    answer = float('inf')

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        total = 0
        total_gold = 0
        total_sliver = 0

        for i in range(len(g)):
            cnt = (mid - t[i]) // (t[i] * 2) + 1

            # 금만 운반하는 경우
            # 현재 도시의 용량이 부족한 경우
            if cnt * w[i] > g[i]:
                total_gold += g[i]
            # 도시의 용량이 충분한 경우
            else:
                total_gold += cnt * w[i]

            # 은만 운반하는 경우
            if cnt * w[i] > s[i]:
                total_sliver += s[i]
            else:
                total_sliver += cnt * w[i]

            # 금과 은을 같이 운반하는 경우
            if cnt * w[i] > g[i] + s[i]:
                total += g[i] + s[i]
            else:
                total += cnt * w[i]

        # 목표하는 것보다 많은 양을 운반할 수 있는 경우
        if total_gold >= a and total_sliver >= b and total >= a + b:
            end = mid - 1
            # 많이 운반한 경우 중, 최소 시간이 정답
            answer = min(answer, mid)
        else:
            start = mid + 1

    return answer