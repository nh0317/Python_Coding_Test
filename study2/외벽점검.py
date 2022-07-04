from collections import deque
import itertools


def bfs(start, weak, n, dist):
    d = dist[0]
    L = len(weak)
    S = 2 ** L
    full = 2 ** (L + 1) - 1
    visited = S | (1 << start)
    q = deque([[start, d, 1, visited]])
    min_cnt = float('inf')

    while q:
        i, d, cnt, visited = q.popleft()
        if visited == full:
            min_cnt = min(cnt, min_cnt)
            continue

        pre = (L + (i - 1)) % L
        post = (L + (i + 1)) % L
        min_pre = min(abs(n - weak[pre] + weak[i]), abs(weak[i] - weak[pre]))
        min_post = min(abs(n - weak[post] + weak[i]), abs(weak[i] - weak[post]))

        # 시계 반시계 중 더 짧은 길이 선택
        if min_pre < min_post:
            if not visited & (1 << pre):
                if d >= min_pre:
                    q.append([pre, d - min_pre, cnt, visited | (1 << pre)])

                # 인원을 더 추가하는 경우
                elif cnt < len(dist):
                    d = dist[cnt]
                    q.append([pre, d, cnt + 1, visited | (1 << pre)])

            # 더 짧은 길이로 갈 수 없고
            # 반대 방향은 방문하지 않은 경우에만 선택
            elif not visited & (1 << post):
                if d >= min_post:
                    q.append([post, d - min_post, cnt, visited | (1 << post)])

                elif cnt < len(dist):
                    d = dist[cnt]
                    q.append([post, d, cnt + 1, visited | (1 << post)])

        else:
            if not visited & (1 << post):
                if d >= min_post:
                    q.append([post, d - min_post, cnt, visited | (1 << post)])

                elif cnt < len(dist):
                    d = dist[cnt]
                    q.append([post, d, cnt + 1, visited | (1 << post)])

            elif not visited & (1 << pre):
                if d >= min_pre:
                    q.append([pre, d - min_pre, cnt, visited | (1 << pre)])

                elif cnt < len(dist):
                    d = dist[cnt]
                    q.append([pre, d, cnt + 1, visited | (1 << pre)])

    return visited, min_cnt


def solution(n, weak, dist):
    L = len(weak)

    min_cnt = float('inf')
    full = 2 ** (L + 1) - 1

    per_dist = itertools.permutations(dist)
    for dist in per_dist:
        for i in range(L):
            visited, cnt = bfs(i, weak, n, dist)
            if visited == full:
                min_cnt = min(min_cnt, cnt)

    if min_cnt > len(dist):
        return -1

    return min_cnt