# def check(stones,k,n):
#     temp = k
#     for stone in stones:
#         if stone < n:
#             temp -= 1
#         else:
#             temp = k

#         if temp == 0:
#             return False
#     return True

# def solution(stones, k):
#     l = 0
#     r = 200000000
#     while l<r-1:
#         n = (l+r)//2
#         canJump = check(stones,k,n)

#         if canJump:
#             l = n
#         else:
#             r = n

#     rok = check(stones,k,r)
#     if rok:
#         return r
#     else:
#         return l

def solution(stones, k):
    if k == len(stones):
        return max(stones)
    elif k == 1:
        return min(stones)
    check = sorted(stones, reverse=True)
    if check == stones:
        return stones[-k]
    maxx = 0
    i = 0
    minn =float('inf')
    
    while i < len(stones)-k+1:
        nextt = i
        for j in range(k):
            if maxx <= stones[i+j]:
                maxx = stones[i+j]
                nextt = i+j

        if maxx < minn:
            minn = maxx

        i = 1 + nextt
        if i < len(stones):
            maxx = stones[i]
        else: break

    return minn