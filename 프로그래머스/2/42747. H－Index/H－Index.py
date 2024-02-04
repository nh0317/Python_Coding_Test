def solution(citations):
    answer = 0
    for h in range(max(citations), 0, -1):
        cnt = 0
        for citation in citations:
            if citation > h:
                cnt += 1
        if cnt >= h:
            answer = cnt
            break
    
    return answer