from collections import deque


def bfs(begin, target, words):
    q = deque([[begin, 0]])
    min_cnt = float("inf")
    visited = [False for _ in range(len(words))]

    while q:
        word, cnt = q.popleft()

        if word == target:
            min_cnt = min(min_cnt, cnt)

        for i in range(len(word)):

            for j, w in enumerate(words):
                if not visited[j] and w[i] != word[i] and w[0:i] == word[0:i]:
                    if i < len(word) and w[i + 1:] == word[i + 1:]:
                        q.append([w, cnt + 1])
                        visited[j] = True

    return 0 if min_cnt == float("inf") else min_cnt


def solution(begin, target, words):
    answer = bfs(begin, target, words)
    return answer