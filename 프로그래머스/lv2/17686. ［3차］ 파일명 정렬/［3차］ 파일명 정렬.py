import re
def split_num(file):
    idx = 0
    head = ''
    for i,s in enumerate(file):
        idx = i
        if s.isdigit():
            break
        else:
            head += s
    else:
        return head, 0
    
    tail = file[idx:]
    
    idx = 0
    num = ''
    for i,s in enumerate(tail):
        if not s.isdigit():
            break
        else:
            num += s
    if num :
        num = int(num)
    return head, num

def solution(files):
    file_infos = []
    for i,file in enumerate(files):
        head, num = split_num(file.lower())
        file_infos.append([file, i, head, num])
        
    file_infos.sort(key=lambda x : (x[2],x[3],x[1]))
    answer = [file[0] for file in file_infos]
    return answer