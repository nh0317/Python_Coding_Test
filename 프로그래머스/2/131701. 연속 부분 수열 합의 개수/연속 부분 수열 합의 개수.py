def next_element(i, n):
    return (i+1) % n

def sum_n(elements, n, sums):
    visited = set()
    start = 0
    end = start + n
    summ = sum(elements[start:end])
    sums.add(summ)
    
    visited.add((start, end))
    while True:
        summ -= elements[start]
        summ += elements[end]
        
        start = next_element(start, len(elements))
        end = next_element(end, len(elements))
        
        if (start, end) in visited:
            break
        else:
            sums.add(summ)
    

def solution(elements):
    answer = 0
    sums = set()
    for i in range(1, len(elements)):
        sum_n(elements, i, sums)
    
    return len(sums) + 1