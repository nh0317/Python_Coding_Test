import sys

def sumOfSubset():
    subSum=0
    minLength=N+1
    top=0
    bottom=0
    while top<=N and top>=bottom:
        if subSum>=S:
            minLength=min(top-bottom,minLength)
            subSum-=seq[bottom]
            bottom+=1
        elif top==N:
            break
        elif(subSum<S):
            subSum+=seq[top]
            top+=1
    return minLength

input=sys.stdin.readline

N,S=map(int,input().split())
seq=list(map(int, input().split()))
minn=sumOfSubset()
if(minn>len(seq)):
    print(0)
else: print(minn)
