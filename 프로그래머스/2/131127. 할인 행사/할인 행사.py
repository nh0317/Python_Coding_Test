from collections import defaultdict 

def signin(want, number, discount, products):
    for j in range(len(want)):
        if products[want[j]] < number[j]:
            break
    else:
        return 1
    
    return 0

def solution(want, number, discount):
    products = defaultdict(int)
    answer = 0
    
    for i in range(10):
        products[discount[i]] += 1
    
    answer += signin(want, number, discount, products)
    
    for i in range(10, len(discount)):
        products[discount[i-10]] -= 1
        products[discount[i]] += 1
        
        answer += signin(want, number, discount, products)
    
    return answer