import itertools

def solution(k, dungeons):
    answer = 0
    
    for route in list(itertools.permutations([ x for x in range(len(dungeons))], len(dungeons))):
        heart = k
        cnt = 0
        for u in route:
            if heart < dungeons[u][0]:
                break
            heart -= dungeons[u][1]
            cnt += 1
        answer = max(answer, cnt)
                
    
    return answer