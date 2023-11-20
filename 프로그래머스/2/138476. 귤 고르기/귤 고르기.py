import itertools
from collections import defaultdict 

def solution(k, tangerines):
    answer = 0
    
    sizes = defaultdict(int)
    for tangerine in tangerines:
        sizes[tangerine] += 1
    
    sizes = sorted(sizes.items(), key = lambda x : -x[1])
    
    for size, cnt in sizes:
        if k - cnt >= 0:
            k -= cnt
            answer += 1
        else:
            answer += 1
            break
            
        if k == 0:
            break
    
    return answer