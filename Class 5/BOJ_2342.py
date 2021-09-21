import sys

def calPower(cur,next):
    if cur==0:
        return 2
    elif cur==next:
        return 1
    elif abs(cur-next)==2:
        return 4
    else: return 3

def solve(n,l,r):
    if n>=len(seq)-1:
        return 0
    if dp[n][l][r] != float('inf'):
        return dp[n][l][r]
    dp[n][l][r]= min(solve(n+1,seq[n],r)+calPower(l,seq[n]),solve(n+1,l,seq[n])+calPower(r,seq[n]))
    return dp[n][l][r]

input = sys.stdin.readline

seq=list(map(int,input().split()))

dp = [[[float('inf') for _ in range(5)] for _ in range(5)]for _ in range(len(seq))]
print(solve(0,0,0))

# https://0902.tistory.com/41