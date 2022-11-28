import sys

input = sys.stdin.readline

def pay_back(m,A,subSum):
    minn = float('inf')
    for i in range(m,len(subSum)):
        summ = subSum[i] - subSum[i-m]
        minn = min(minn, A[i-1] * m-summ)
    return minn

T = int(input())
for _ in range(T):
    A = list(map(int, input().split()))
    N = A.pop(0)
    A.sort()
    subSum = [0]+A[:]
    for i in range(1,N+1):
        subSum[i] += subSum[i-1]
    total = 0
    for i in range(2,N+1):
        total += pay_back(i,A,subSum)
    print(total)
