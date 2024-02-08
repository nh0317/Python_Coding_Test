import re
def solution(s):
    A = s.split("}")
    A = list(filter(lambda x: x, A))
    A = [re.sub("{|^,", "", x) for x in A]
    A.sort(key=lambda x : len(x))
    
    answer = []
    for a in A:
        for a in a.split(','):
            if a not in answer:
                answer.append(a)
    return list(map(int, answer))