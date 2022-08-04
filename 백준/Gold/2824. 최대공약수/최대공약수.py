import sys

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline


N = int(input())
arrA = [int(x) for x in input().split()]

M = int(input())
arrB = [int(x) for x in input().split()]

def gcb(A, B):
    if A % B == 0:
        return B
    return gcb(B, A%B)

A = 1
for i in arrA:
    A *= i

B = 1
for i in arrB:
    B *= i

print(str(gcb(A,B))[-9:])