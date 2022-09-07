import re
import itertools
from collections import defaultdict
import bisect 

def solution(infos, querys):
    answer = []
    info_dict = defaultdict(list)
    
    for info in infos:
        info = info.split(' ')
        for product in set(itertools.product([True, False], repeat = 4)):
            query = []
            for i, exist in enumerate(product):
                if exist:
                    query.append(info[i])
                else: query.append('-')
                
            info_dict[' and '.join(query)].append(int(info[-1]))
    
    for q in info_dict.keys():
        # info_dict[q] = sorted(info_dict[q], reverse=True)
        info_dict[q] = sorted(info_dict[q])
    
    for query in querys:
        point = int(re.findall(r'[0-9]+', query)[0])
        query = query.replace(' '+str(point),"")
        if info_dict[query]:    
#             start = 0
#             end = len(info_dict[query])-1
#             mid = (start + end)//2
#             while start <= end:
#                 mid = (start + end)//2
#                 if mid >= len(info_dict[query]):
#                     mid = -1
#                     break
#                 if info_dict[query][mid] >= point:
#                     start = mid + 1
#                 elif info_dict[query][mid] < point:
#                     end = mid - 1
                    
#             if mid < len(info_dict[query]) and info_dict[query][mid] < point:
#                 mid -= 1
            mid = bisect.bisect_left(info_dict[query], point)
            answer.append(len(info_dict[query]) - mid)
        else: 
            answer.append(0)
    
    
    
                
    return answer