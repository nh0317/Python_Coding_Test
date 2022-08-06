import heapq

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    while A and B:
        if B[-1] > A[-1]:
            A.pop()
            B.pop()
            answer += 1
        else:A.pop()
        
        
    return answer