import sys

input = sys.stdin.readline

N, M, L = map(int, input().split())
rest_area = [0] + list(map(int, input().split())) + [L]
rest_area.sort(reverse=True)

start = 1
end = L
res = 0
while start <= end:
    mid = (start + end)//2
    n = 0
    for i in range(len(rest_area)-1):
        if rest_area[i] - rest_area[i+1] > mid:
            n += (rest_area[i] - rest_area[i+1] - 1)//mid

    if n > M:
        start = mid + 1
    else:
        res = mid
        end = mid - 1

print(res)
