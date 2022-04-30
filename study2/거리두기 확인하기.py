from collections import deque


def check(y, x, k, people, places):
    q = deque([[y, x, 0, False]])
    d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    visited = [[False for _ in range(5)] for _ in range(5)]
    visited[y][x] = True

    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if 0 <= ny < 5 and 0 <= nx < 5 and places[k][ny][nx] != "X":
            break
    else:
        return True

    while q:
        cy, cx, cnt, isPartition = q.popleft()

        for dy, dx in d:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < 5 and 0 <= nx < 5 and not visited[ny][nx]:
                if places[k][ny][nx] != "P":
                    if cnt + 1 <= 2:
                        visited[ny][nx] = True
                        if places[k][ny][nx] == "X":
                            q.append([ny, nx, cnt + 1, True])
                        else:
                            q.append([ny, nx, cnt + 1, False])

                elif places[k][ny][nx] == "P":
                    if cnt + 1 <= 2 and not isPartition:
                        return False
    return True


def solution(places):
    people = [[] for _ in range(len(places))]
    for i in range(5):
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == "P":
                    people[i].append([j, k])

    answer = [1 for _ in range(5)]
    for k in range(5):
        for y, x in people[k]:
            isOK = check(y, x, k, people, places)
            if not isOK:
                answer[k] = 0
                break
    return answer