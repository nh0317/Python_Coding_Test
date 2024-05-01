from collections import defaultdict

def solution(names, yearnings, photos):
    answer = []
    longing = defaultdict(int)
    
    for name, yearnings in zip(names, yearnings):
        longing[name] = yearnings
    
    for photo in photos:
        score = 0
        for name in photo:
            score += longing[name]
        answer.append(score)
    
    return answer