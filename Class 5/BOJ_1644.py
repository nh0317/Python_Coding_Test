import math
import sys

def isPrime(n):
    nums=[True for i in range(n+1)]

    for i in range(2, int(math.sqrt(n))+1):
        if nums[i]==True:
            j=2
            while i*j<=n:
                nums[i*j]=False
                j+=1
    return [i for i in range(2,n+1) if nums[i]]

input = sys.stdin.readline

N=int(input())
primes=isPrime(N)
top=0
end=0
answer=0
sum=0
ans=[]
while top<=len(primes) and end<=top:
    if sum == N:
        answer+=1
        sum-=primes[end]
        end+=1
    elif sum>N:
        sum-=primes[end]
        end+=1
    elif top==len(primes):
        break
    elif sum<N:
        sum+=primes[top]
        top+=1

print(answer)