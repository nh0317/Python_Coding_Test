from collections import defaultdict

def solution(topping):
    answer = 0
    
    len_kinds = len(set(topping))
    # if len_kinds % 2 != 0:
    #     return 0
    
    oldder = defaultdict(int)
    for i,top in enumerate(topping):
        oldder[top]+=1
    
    younger = defaultdict(int)
    for i,top in enumerate(topping):
        oldder[top]-=1
        younger[top]+=1
        if oldder[top] == 0:
            oldder.pop(top)
        
        if len(oldder) == len(younger):
            answer += 1    
        
    return answer