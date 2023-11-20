import heapq 

def solution(n, works):
    answer = 0
    pq = []
    for work in works:
        heapq.heappush(pq, -work)
        
    for i in range(n):
        if pq:
            n = -heapq.heappop(pq)
        if n != 0:
            heapq.heappush(pq, -(n-1))
    
    for n in pq:
        answer += n ** 2
        
    return answer