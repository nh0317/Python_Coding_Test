from collections import Counter

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
        
        # dp[i] = maxx
        if maxx < minn:
            minn = maxx
        
        i = 1 + nextt
        if i < len(stones):
            maxx = stones[i]
        else: break
            
    return minn