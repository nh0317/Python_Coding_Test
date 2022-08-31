import sys

input = sys.stdin.readline

def make_seq(n, i):
    seq = [n]
    while i >= 0:
        tmp = i
        i = seq[-1] - i
        seq.append(tmp)
    return seq

N = int(input())
maxx = -1
max_seq = []
for i in range(1, N+1):
    seq = make_seq(N,i)
    if maxx <= len(seq):
        max_seq = seq
        maxx = len(seq)

print(len(max_seq))
for s in max_seq:
    print(s, end=" ")
