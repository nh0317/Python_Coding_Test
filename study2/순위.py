from collections import deque, Counter


def bfs(start, graph):
    visited = [False for _ in range(len(graph))]
    q = deque([start])
    visited[start] = True
    cnt = 0

    while q:
        u = q.popleft()
        for v in graph[u]:
            if not visited[v]:
                cnt += 1
                q.append(v)
                visited[v] = True
    return cnt


def solution(n, results):
    answer = 0
    wins = [[] for _ in range(n)]
    loses = [[] for _ in range(n)]
    outdegree = [0 for _ in range(n)]
    indegree = [0 for _ in range(n)]

    for u, v in results:
        wins[u - 1].append(v - 1)
        loses[v - 1].append(u - 1)

    for i in range(n):
        outdegree[i] = bfs(i, wins)

    for i in range(n):
        indegree[i] = bfs(i, loses)

    answer = Counter(a + b for a, b in zip(indegree, outdegree))[n - 1]

    # 플로이드를 이용한 풀이

    #     scores = [['?' for _ in range(n)] for _ in range(n)]

    #     for i in range(n):
    #         for j in range(n):
    #             scores[i][i] = 'self'

    #     for u,v in results:
    #         scores[u-1][v-1] = 'win'
    #         scores[v-1][u-1] = 'lose'

    #     for k in range(n):
    #         for i in range(n):
    #             for j in range(n):
    #                 if scores[i][k] == 'win' and scores[k][j]=='win':
    #                     scores[i][j] = 'win'
    #                 elif scores[i][k] == 'lose' and scores[k][j]=='lose':
    #                     scores[i][j] = 'lose'

    #     for score in scores:
    #         if '?' not in score:
    #             answer +=1
    return answer

