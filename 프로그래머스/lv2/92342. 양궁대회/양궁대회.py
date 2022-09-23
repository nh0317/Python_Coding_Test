import copy

maxx = -1
answer = []
info = []
n = 0

def cal_score(lions):
    global n
    global info
    global answer
    global maxx
    
    lion_score = 0
    apeach_score = 0
    for i in range(len(lions)):
        if lions[i] > info[i]:
            lion_score+= 10 - i
        elif lions[i] == 0 and info[i] == 0:
            continue
        else:
            apeach_score+= 10 - i

    if lion_score - apeach_score > 0 and maxx < lion_score - apeach_score:
        answer = copy.deepcopy(lions)
        maxx = lion_score - apeach_score

def backtracking(lions, summ, idx):

    global n
    global info
    if idx < 0 or summ > n:
        return 

    if summ == n:
        cal_score(lions)

    else:
        lions[idx] += 1
        backtracking(lions, summ +1, idx)
        lions[idx] -= 1
        
        backtracking(lions, summ, idx-1)

def solution(N, i):
    global n
    global info
    global answer
    
    n = N
    info = i
    lions = [0 for _ in range(len(info))]
    
    backtracking(lions, 0, 10)
    return answer if answer else [-1]