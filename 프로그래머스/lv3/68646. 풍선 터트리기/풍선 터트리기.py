# def check(a, start, end, i):
#     cnt = 0    
#     if start < i:
#         min1 = min(a[start:i])
#         if a[i] > min1:
#             cnt += 1
        
#     if i+1 < end:
#         min2 = min(a[i+1:end])
#         if a[i] > min2:
#             cnt += 1
#     return True if cnt <= 1 else False



def solution(a):
    answer = 0
    
    left = [a[0] for _ in range(len(a))]
    minn_left = a[0]
    
    right = [a[len(a)-1] for _ in range(len(a))]
    minn_right = a[len(a)-1]
    
    for i in range(1,len(a)):
        j = len(a) - i
        
        if minn_left > a[i]:
            minn_left = a[i]
            
        if left[i] > minn_left:
            left[i] = minn_left
            
        if minn_right > a[j]:
            minn_right = a[j]
            
        if right[j] > minn_right:
            right[j] = minn_right
    
    for i in range(len(a)):
        if not (right[i] < a[i]  and left[i] < a[i]):
            answer += 1
    
    return answer