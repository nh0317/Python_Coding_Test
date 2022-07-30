def solution(n, times):
    start = 0
    end = 10 ** 19
    mid = ( start + end ) // 2
    
    min_time = end
    while start <= end:
        total = 0
        mid = (start + end)//2
        
        for time in times: 
            total += mid // time
            
        if total < n: 
            start = mid + 1
            
        elif total >= n:
            min_time = min(mid, min_time)
            end = mid - 1
    
    return min_time