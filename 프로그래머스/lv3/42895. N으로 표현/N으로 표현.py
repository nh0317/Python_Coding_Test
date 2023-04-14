from collections import defaultdict

dp = defaultdict(set)

def cal(i, a, b, number):
    
    if b != 0:
        dp[i].add(a//b)
    if a != 0:
        dp[i].add(b//a)
    dp[i].add(a*b)
    dp[i].add(a+b)
    dp[i].add(a-b)
    dp[i].add(b-a)
    
    if a != 0 and abs(b//a) == number:
        return True
    elif b != 0 and abs(a//b) == number:
        return True
    elif abs(a*b) == number:
        return True
    elif abs(a+b) == number:
        return True
    elif abs(a-b) == number:
        return True
    elif abs(b-a) == number:
        return True
    
    return False
    

def solution(N, number):
    if N == number:
        return 1
    
    dp[1].add(N)
    
    for i in range(2, 9):
        n = N
        for _ in range(i-1):
            n *= 10
            n += N
        
        if n == number:
            return i
        
        dp[i].add(n)
        
        for j in range(1,i):
            for a in dp[i-j]:
                for b in dp[j]:
                    if cal(i, a, b, number):
                        return i 
            
    return -1