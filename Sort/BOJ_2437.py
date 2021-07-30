import sys
from collections import deque

def sol():
    weights.sort()
    check = deque(weights)
    sum = 0
    if (check[0] > 1):
        print(1)
        return

    while check:
        w = check.popleft()
        sum += w
        if check:
            if sum + 1 < check[0]:
                break

    print(sum + 1)
    return

input=sys.stdin.readline
N=int(input())
weights=list(map(int,input().split()))
sol()
