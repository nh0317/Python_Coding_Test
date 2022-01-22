import sys

input = sys.stdin.readline

min_ladder = 4


def put_ladder(y, x, cnt):
    global min_ladder
    # print(y,x,cnt)
    if cnt == 4 or cnt >= min_ladder:
        return
    if promising():
        # print("can put ladder")
        for i in range(y, H + 1):
            k = x if i == y else 0
            for j in range(k, N):
                if not ladder[i][j] and not ladder[i][j + 1] and not ladder[i][j - 1]:
                    ladder[i][j] = True
                    # print("put ladder :", i, j)
                    put_ladder(i, j + 2, cnt + 1)
                    ladder[i][j] = False
                    # print("back ladder :", i, j)
    else:
        # print("answer :", min_ladder)
        min_ladder = min(min_ladder, cnt)


# 다시 하기
def promising():
    for i in range(1, N):  # 열
        start = i
        for j in range(1, H + 1):  # 행
            # print(j, i, start)
            if ladder[j][start]:
                start += 1
            elif ladder[j][start - 1]:
                start -= 1
        if start != i:
            return True
    return False


N, M, H = map(int, input().split())
if M == 0:
    print(0)
else :
    ladder = [[False for _ in range(N + 1)] for _ in range(H + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        ladder[a][b] = True

    put_ladder(1, 1, 0)
    if min_ladder > 3:
        print(-1)
    else:
        print(min_ladder)
