def solution(A,B):
    summ = 0
    A = sorted(A)
    B = sorted(B, reverse=True)
    
    for i in range(len(A)):
        summ += A[i] * B[i]
    
    return summ