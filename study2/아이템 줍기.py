from collections import deque


def print_map(mapp):
    for i in range(len(mapp)):
        for j in range(len(mapp[i])):
            print(mapp[i][j], end=" ")
        print()


def fill_map(rectangle):
    recs = set()

    max_x = -1
    max_y = -1
    for x1, y1, x2, y2 in rectangle:
        max_x = max(max_x, x2)
        max_y = max(max_y, y2)
        for i in range(y1 * 2, y2 * 2 + 1):
            for j in range(x1 * 2, x2 * 2 + 1):
                recs.add((i, j))

    mapp = [[0 for _ in range(max_x * 2 + 2)] for _ in range(max_y * 2 + 2)]

    for y, x in recs:
        mapp[y][x] = 1

    return mapp


def bfs(mapp, character, item):
    q = deque([[character[1] * 2, character[0] * 2, 0]])
    mapp[character[1] * 2][character[0] * 2] = 3
    dydx = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    ddyddx = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    maxx = 0
    while q:
        y, x, cnt = q.popleft()
        if y == item[1] * 2 and x == item[0] * 2:
            maxx = max(maxx, cnt)
            continue

        for dy, dx in dydx:
            ny = y + dy
            nx = x + dx
            if 0 <= nx < len(mapp[0]) and 0 <= ny < len(mapp):
                if mapp[ny][nx] == 1:
                    for ddy, ddx in ddyddx:
                        if mapp[ny + ddy][nx + ddx] == 0:
                            break
                    else:
                        continue
                    mapp[ny][nx] = 3
                    q.append([ny, nx, cnt + 1])
    return maxx


def solution(rectangle, characterX, characterY, itemX, itemY):
    mapp = fill_map(rectangle)
    answer = bfs(mapp, [characterX, characterY], [itemX, itemY])

    return answer // 2