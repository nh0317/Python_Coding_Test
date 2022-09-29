import sys
from collections import deque

sys = sys.stdin.readline

def print_arr(arr):
    for i in range(len(arr)):
        for a in arr[i]:
            print(a, end=" ")
        print()

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

r1, r2 = 0,N-1
c1, c2 = 0,M-1
n=0
while r1 < r2 and c1 < c2:
    
    length = (N - 2*n + M - 2*n) - 2
    r = R % (length * 2)
    left = deque()
    right = deque()
    center = deque()
    top= deque(arr[r1][c1+1:c2])
    bottom=deque(arr[r2][c1+1:c2])

    for i in range(r1,r2+1):
        left.append(arr[i][c1])
        right.append(arr[i][c2])

    for _ in range(r):
        if top:
            left.appendleft(top.popleft())
            bottom.appendleft(left.pop())
            right.append(bottom.pop())
            top.append(right.popleft())
        else:
            right.append(left.pop())
            left.appendleft(right.popleft())

    arr[r1][c1+1:c2] = top
    arr[r2][c1+1:c2] = bottom

    for i in range(r1,r2+1):
        arr[i][c1] = left[i-n]
        arr[i][c2] = right[i-n]
    r1+=1
    c1+=1

    r2-=1
    c2-=1
    n+=1

print_arr(arr)
