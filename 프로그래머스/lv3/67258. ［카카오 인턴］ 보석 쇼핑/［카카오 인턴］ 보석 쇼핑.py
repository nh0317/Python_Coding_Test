import heapq
from collections import defaultdict 

def solution(gems):
    answer = []
    n = len(set(gems))
    N = len(gems)
    length = []
    
    start = 0
    end = 0
    picked = defaultdict(int)
    picked[gems[start]] = 1
    while start <= end <= N:
        if len(picked) == n:
            heapq.heappush(length,[end-start, start+1, end+1])
            picked[gems[start]] -= 1
            if picked[gems[start]] == 0:
                picked.pop(gems[start])
            start += 1
            
        else:
            end += 1
            if end < N:
                picked[gems[end]] += 1
    
    answer = [length[0][1], length[0][2]]
    return answer