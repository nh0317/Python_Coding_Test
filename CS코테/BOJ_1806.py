import sys

input = sys.stdin.readline

N, S = map(int, input().split())
seqs = list(map(int, input().split()))


start = 0
end = 0
minn = float('inf')
summ = seqs[0]

while start <= end < N:
    if summ >= S:
        minn = min(minn, end-start+1)
        summ -= seqs[start]
        start += 1

    elif summ < S:
        end += 1
        if end < N:
            summ += seqs[end]

print(minn) if minn <= N else print(0)

