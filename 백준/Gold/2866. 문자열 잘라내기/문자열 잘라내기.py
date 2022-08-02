import sys


input = sys.stdin.readline

R, C = map(int, input().split())
table = [[0 for _ in range(R)] for _ in range(C)]
tmp = []

for _ in range(R):
    tmp.append(list(input().rstrip()))

for i in range(R):
    for j in range(C):
        table[j][i] = tmp[i][j]

cnt = 0
start = 0
end = R

while start <= end:
    mid = (start + end) // 2

    strs = set()
    for j in range(C):
        strs.add(tuple(table[j][mid:]))
        if len(strs) < j:
            break

    # 중복이 있으면
    if len(strs) != C:
        end = mid - 1
    else:
        cnt = max(cnt, mid)
        start = mid + 1

print(cnt)