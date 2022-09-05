def check(stones,k,n):
    temp = k
    for stone in stones:
        if stone < n:
            temp -= 1
        else:
            temp = k

        if temp == 0:
            return False
    return True

def solution(stones, k):
    l = 0
    r = 200000000
    while l<r-1:
        n = (l+r)//2
        canJump = check(stones,k,n)

        if canJump:
            l = n
        else:
            r = n

    rok = check(stones,k,r)
    if rok:
        return r
    else:
        return l