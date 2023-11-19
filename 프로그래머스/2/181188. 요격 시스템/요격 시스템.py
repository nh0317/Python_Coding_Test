def solution(targets):
    answer = 1
    targets = sorted(targets)
    
    end = targets[0][1]
    for s,e in targets:
        if end > s:
            end = min(end, e)
        else:
            end = e
            answer += 1
            
    return answer