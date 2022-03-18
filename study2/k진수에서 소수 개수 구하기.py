import math


def knotation(n, k):
    knot = []
    while n // k != 0:
        knot.append(n % k)
        n = n // k
    knot.append(n)
    knot.reverse()

    return "".join(str(_) for _ in knot)


def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, round(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
    return True


def solution(n, k):
    answer = 0
    knot = knotation(n, k)
    nums = knot.split("0")
    for i in nums:
        if i != "" and isPrime(int(i)):
            answer += 1
    return answer