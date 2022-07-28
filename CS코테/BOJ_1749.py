import sys

input = sys.stdin.readline

N,M = map(int, input().split())

board = [[int(x) for x in input().split()]for _ in range(N)]

maxx = -float('inf')


sub_sum = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        summ = 0
        for row in board[:i]:
            summ += sum(row[:j])
        sub_sum[i][j] = summ

for y1 in range(1,N+1):
    for x1 in range(1,M+1):
        for y2 in range(y1,N+1):
            for x2 in range(x1,M+1):
                summ = sub_sum[y2][x2] - sub_sum[y2][x1-1] - sub_sum[y1-1][x2] + sub_sum[y1-1][x1-1]
                maxx = max(maxx, summ)

print(maxx)