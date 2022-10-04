import sys

input = sys.stdin.readline

N = int(input())
musics = [-1]+list(map(int, input().split()))
prefix_sum = [0 for _ in range(N+1)]

for i in range(1,N):
    if musics[i] > musics[i+1]:
        prefix_sum[i] = 1

for i in range(1, N+1):
    prefix_sum[i] += prefix_sum[i-1]

Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    print(prefix_sum[y-1]-prefix_sum[x-1])
