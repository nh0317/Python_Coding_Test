def solution(n, s):
    if (s % n == 0):
        return [(s//n) for _ in range(n)]
    
    if (s // n == 0):
        return [-1]

    answer = [s//n for _ in range(n)]
    cnt = s - sum(answer)
    
    for i in range(cnt):
        answer[i % n] += 1
    
    return sorted(answer)