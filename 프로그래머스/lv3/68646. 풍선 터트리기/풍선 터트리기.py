def solution(a):
    answer = 0
    
    left = [float('inf') for _ in range(len(a))]
    right = [float('inf') for _ in range(len(a))]
    minn_left, minn_right = float('inf'), float('inf')
    
    for i in range(len(a)):
        if minn_left > a[i]:
            minn_left = a[i]
        left[i] = minn_left
            
    for i in range(len(a)-1, -1, -1):
        if minn_right > a[i]:
            minn_right = a[i]
        right[i] = minn_right
    
    for i in range(len(a)):
        if not (right[i] < a[i]  and left[i] < a[i]):
            answer += 1
    
    return answer