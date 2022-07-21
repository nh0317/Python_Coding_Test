import sys

input = sys.stdin.readline

N, M = map(int, input().split())
times = []
for _ in range(N):
    times.append(int(input()))

start = 0
end = (10**19)

min_time = float('inf')
while start < end:
    mid = (start + end)//2
    total = 0
    for time in times:
        total += mid // time

    if total >= M:
        min_time = min(min_time, mid)
        end = mid

    else:
        start = mid + 1

print(min_time)