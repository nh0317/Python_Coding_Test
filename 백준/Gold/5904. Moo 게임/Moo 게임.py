import sys
sys.setrecursionlimit(10 ** 4)

input = sys.stdin.readline

N = int(input())

def Moo(k, l, n):
    pre = (l - (k + 3)) // 2
    if n <= pre:
        return Moo(k - 1, pre, n)
    elif n > pre + k + 3:
        return Moo(k - 1, pre, n - pre - k - 3)
    else:
        if n - pre == 1:
            return 'm'
        return 'o'

s0 = 3
k = 0
while s0 < N:
    k+=1
    s0 = s0 * 2 + k+3

print(Moo(k,s0,N))