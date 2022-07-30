def solution(n,a,b):
    answer = 0
    end = n + 1
    start = 0
    
    
    while start <= end:
        mid = (start + end)//2
        A = min(a,b)
        B = max(a,b)
        for _ in range(mid-1):
            A = (A+1)//2
            B = (B+1)//2

        if B-A == 1 and A % 2 == 1:
            answer = mid
            break
        if B-A > 1 or (B-A == 1 and A %2 == 0):
            start = mid + 1
        else:
            end = mid - 1
            
    return 1 if answer == 0 else answer