res = []

def hanoi(n, src, dest, sub):
    if n == 1:
        res.append([src, dest])
        return 
    
    hanoi(n-1, src, sub, dest)
    res.append([src, dest])
    hanoi(n-1, sub, dest, src)
        
                    
        

def solution(n):
    hanoi(n, 1, 3, 2)
    return res