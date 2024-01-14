cnt = 0
def make_number(i, summ, numbers, target):
    global cnt 
    if i >= len(numbers):
        if summ == target:
            cnt += 1
        return 

    make_number(i+1, summ + numbers[i], numbers, target)
    make_number(i+1, summ - numbers[i], numbers, target)

def solution(numbers, target):
    global cnt 
    
    make_number(0,0,numbers, target)
    
    return cnt