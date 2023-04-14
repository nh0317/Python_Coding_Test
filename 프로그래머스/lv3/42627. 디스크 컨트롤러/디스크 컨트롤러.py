import heapq

def solution(jobs):
    pq = []
    
    for start, job in jobs:
        heapq.heappush(pq, [start, job])
    
    time = 0
    processing = 0
    waiting = []
    while pq:
        if waiting:
            job, start = heapq.heappop(waiting)
            processing += time - start + job
            time += job
        else:
            start, job = heapq.heappop(pq)
            processing += job
            time = start + job
        
        while pq and pq[0][0] < time:
            start, job = heapq.heappop(pq)
            heapq.heappush(waiting, [job, start])
            
    while waiting:
        job, start = heapq.heappop(waiting)
        processing += time - start + job
        time += job
        
            
    return processing // len(jobs)