import re

def solution(files):
    file_infos = []
    for i,file in enumerate(files):
        head=re.split('[0-9]+', file.lower())[0]
        num=int(re.split('[^0-9]+', file)[1])
        file_infos.append([file, i, head, num])
        
    file_infos.sort(key=lambda x : (x[2],x[3],x[1]))
    answer = [file[0] for file in file_infos]
    return answer