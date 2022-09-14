from collections import deque
import copy

def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    ori1 = copy.deepcopy(queue1)
    ori2 = copy.deepcopy(queue2)
    queue1 = deque(queue1)
    queue1.extend(queue2)
    queue2 = deque(queue2)
    queue2.extend(queue1)
    
    cnt = -1
    start1 = 0
    start2 = 0
    
    
    if (sum1 + sum2) % 2 == 1:
        return -1
    
    while queue1 and queue2:
        cnt += 1
        # print(queue1,queue2,sum1, sum2)
        
        if sum1 == sum2:
            break
            
        elif sum1 > sum2:
            u = queue1.popleft()
            sum1 -= u
            sum2 += u
            # start1 += 1
            
        elif sum1 < sum2:
            u = queue2.popleft()
            sum1 += u
            sum2 -= u
            # start2 += 1
        
#         if not queue1 and start2 <= len(queue2):
#             q = ori2[:start2]
#             start1 = 0
#             queue1.extend(q)
            
#         if not queue2 and start1<= len(queue1):
#             q = ori1[:start1]
#             start2 = 0
#             queue2.extend(q)
        
        
        if queue1 == ori1 and queue2 == ori2:
            cnt = -1
            break
            
            
    if not queue1 or not queue2:
        cnt = -1
    return cnt