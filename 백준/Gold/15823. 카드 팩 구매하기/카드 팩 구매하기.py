import sys
from collections import defaultdict

input = sys.stdin.readline


def pick_cards(card,n):

    start = 0
    end = 0

    check = defaultdict(int)
    # check[card[start]] = 0
    cnt = 0

    while start <= end < len(card):
        # print(start, end)
        # print(check)
        if card[end] in check:
            for i in range(check[card[start]], check[card[end]] + 1):
                start = check[card[i]]
                check.pop(card[i])
            start += 1
            check[card[end]] = end
        else:
            check[card[end]] = end

        end += 1
        if len(check) == n:
            # print(check)
            cnt += 1
            check.clear()
            start = end

    return cnt

N, M = map(int, input().split())

card = list(map(int, input().split()))

cnt = 0
maxx = 0
end = N
start = 1
while start <= end:
    mid = (start + end) // 2
    cnt = pick_cards(card,mid)
    # print(mid, cnt)
    if cnt >= M:
        maxx = max(maxx, mid)
        start = mid + 1
    else:
        end = mid - 1

print(maxx)
