import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

for _ in range(M):
    i,j = map(int, input().split())
    print(sum(arr[i-1:j]))

# sub_sum = [0 for _ in range(N + 1)]
#
# for i in range(1,N+1):
#     sub_sum[i] = arr[i]+arr[i-1]
