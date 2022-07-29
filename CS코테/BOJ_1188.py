import sys
input = sys.stdin.readline


def cut(n,m):
    if m == 0:
        return 0, n, m
    if n/m > 1:
        n = n % m
    piece = n/m
    for i in range(2,101):
        if piece >= 1/i:
            return (i-1)*n, n, m
    return 0, n, m

def check(n,m):
    if n == 0 or m == 0:
        return False
    rest = min((m%n)/m,n/m)
    eat = max((m%n)/m, n/m)
    if rest != 0 and eat % rest == 0:
        return False
    else: return True


N,M = map(int, input().split())
if N / M == 1 or N % M ==0:
    print(0)
else:
    if N/M > 1:
        N = N % M
    cnt_cut, n, m = cut(N,M)
    cnt = cnt_cut
    while check(n,m):
        m = m % n
        cnt_cut, n, m = cut(n,m)
        cnt+=cnt_cut
        if m != 0 and n/m >= 1:
            n = n % m

    print(cnt)


# def gcd(a,b):
#     if a % b == 0:return b
#     return gcb(b, a%b)
#
# M - 1 - (gcd - 1)
# print(M-gcd(N,M))