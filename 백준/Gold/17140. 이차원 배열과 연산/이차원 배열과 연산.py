import sys
from collections import Counter

input = sys.stdin.readline

r, c, k = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(3)]

def op_r(arr):
    new_list = [[] for _ in range(len(arr))]
    maxx = 0
    for i,a in enumerate(arr):
        count = Counter(a)
        count = sorted(count.items(), key=lambda x: (x[1], x[0]))
        for k,v in count:
            if k == 0:
                continue
            new_list[i].extend([k,v])
        maxx = max(maxx, len(new_list[i]))

    for i in range(len(new_list)):
        new_list[i] += [0] * (maxx-len(new_list[i]))
    return new_list
def op_c(arr):
    t = [[0 for _ in range(len(arr))] for _ in range(len(arr[0]))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            t[j][i] = arr[i][j]
    arr_r = op_r(t)
    new_list = [[0 for _ in range(len(arr_r))] for _ in range(len(arr_r[0]))]
    for i in range(len(arr_r)):
        for j in range(len(arr_r[0])):
            new_list[j][i] = arr_r[i][j]
    return new_list

cnt = 0
while True:
    if r-1<len(A) and c-1 <len(A[0]) and A[r-1][c-1] == k:
        break
    if cnt > 100:
        cnt = -1
        break
    if len(A) >= len(A[0]):
        A = op_r(A)
    else:
        A = op_c(A)
    cnt+=1

print(cnt)