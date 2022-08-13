from collections import defaultdict 

dic = defaultdict(str)
for i in range(10):
    dic[i] = str(i)
    
for i in range(6):
    dic[i+10] = chr(ord('A')+i)

def notation(n, step):
    result = []
    global dic
    while n // step > 0:
        result.append(dic[n % step])
        n //= step
    result.append(dic[n % step])
    result.reverse()
    
    return ''.join(result)

def solution(n, t, m, p):
    answer = ''
    length = 0
    total = ''
    num = 0
    while length <= m * t:
        total+=(notation(num, n))
        length = len(total)
        num += 1
    
    for i,s in enumerate(total):
        if len(answer) == t: 
            break
        if i % m == p-1:
            answer+= s
            
    return answer