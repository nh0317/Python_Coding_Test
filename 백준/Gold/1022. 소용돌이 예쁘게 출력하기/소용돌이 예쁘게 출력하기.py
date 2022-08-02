import sys

input = sys.stdin.readline

r1, c1, r2, c2 =map(int, input().split())

m = max(abs(r1), abs(r2), abs(c1), abs(c2)) * 2 + 1

r1 += m//2
r2 += m//2
c1 += m//2
c2 += m//2

arr = [[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]

N = m * m

n = m
cur = -1
y = m -1
x = m

while n >= 0 :
    for _ in range(n):
        x += cur
        if c1<=x<=c2 and r1<= y <= r2:
            arr[y-r1][x-c1] = N
        N-=1

    n-=1
    for _ in range(n):
        y += cur
        if c1 <=x<=c2 and r1<= y <= r2:
            arr[y-r1][x-c1] = N
        N-=1

    cur *= -1

max_len = -1
for i in range(len(arr)):
    max_len = max(max_len, len(str(max(arr[i]))))

for i in range(len(arr)):
    for j in range(len(arr[0])):
        k = len(str(arr[i][j]))
        print(' '* (max_len - k), end="")
        print(arr[i][j], end=" ")
    print()



