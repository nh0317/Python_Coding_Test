def max_sum(sequence, purse):
    purse = [x*y for x, y in zip(purse, sequence)]
    prefix = [x for x in purse]
    
    for i in range(1, len(purse)):
        prefix[i] += prefix[i-1]
        
    maxx = max(prefix)
    minn = min(prefix)
    if minn < 0:
        return maxx - minn
    return maxx
    
    
    


def solution(sequence):
    plus = [(-1)**(x) for x in range(len(sequence))]
    minus = [(-1)**(x+1) for x in range(len(sequence))]
    
    maxx = max(max_sum(sequence, minus),max_sum(sequence, plus))
    answer = maxx
    return answer