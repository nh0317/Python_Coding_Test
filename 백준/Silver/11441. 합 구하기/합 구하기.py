import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

for _ in range(M):
    i,j = map(int, input().split())
    print(sum(arr[i-1:j]))
