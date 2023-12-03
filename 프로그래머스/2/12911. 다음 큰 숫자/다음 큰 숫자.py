def cnt_ones(num):
    ones =0 
    for n in num:
        if n == '1':
            ones+=1
            
    return ones 

def solution(n):
    answer = 0
    bin_n = bin(n)[2:]
    
    ones = cnt_ones(bin_n)
    
    for i in range(n+1, 1000001):
        if ones == cnt_ones(bin(i)[2:]):
            return i
    
    
    return answer