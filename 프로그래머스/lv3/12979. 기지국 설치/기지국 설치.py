from collections import deque

def solution(n, stations, w):
    answer = 0
    first = 1
    sets = deque([])
    for i,s in enumerate(stations):
        if i > 0:
            if stations[i-1] + w < stations[i] - w:
                sets.append([stations[i] - w, stations[i] + w+1])
            else:
                sets[-1][1] = stations[i] + w + 1
        else: sets.append([s-w, s+w+1])
        
        if s-w <= first <= s+w:
            first = s+w+1
                
    idx = first
    cnt = 0
    step = w * 2 + 1
    while idx <= n:
        if sets:
            if idx < sets[0][0]:
                idx+= step
                cnt += 1
            elif idx <= sets[0][1]:
                idx = sets[0][1]
                sets.popleft()
        else:
            idx += step
            cnt += 1
        
    return cnt