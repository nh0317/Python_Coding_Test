import sys, math

input = sys.stdin.readline

A, B = map(int, input().split())

def is_prime(n):
    arr = [True for _ in range(n + 1)]
    arr[0]=False
    arr[1]=False
    arr[2]=True
    for i in range(2, n+1):
        if arr[i]:
            j = 2
            while i * j <= n:
                arr[i*j] = False
                j+=1

    return arr

cnt = 0
primes = is_prime(int(math.sqrt(B)))
for i, prime in enumerate(primes):
    if prime:
        j = i*i
        while j <= B:
            if j >= A:
                cnt +=1
            j = j*i

print(cnt)