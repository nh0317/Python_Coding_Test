import sys
from collections import deque

def sol():
    tels.sort()
    check=deque(tels)
    while check:
        prefix=check.popleft()
        if check:
            start_index=check[0].find(prefix)
            if start_index ==0:
                print("NO")
                return
    print("YES")
    return

input=sys.stdin.readline

T=int(input())
for _ in range(T):
    N=int(input())
    tels=[]
    for _ in range(N):
        tels.append(input()[:-1])
    sol()