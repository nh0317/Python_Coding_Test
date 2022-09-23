import itertools
import math

def convert(time):
    h, m = map(int, time.split(":"))
    m += 60 *h
    return m 

def solution(fees, records):
    answer = []
    
    infos = []
    for record in records:
        infos.append(record.split(" "))
        
    
    records = itertools.groupby(sorted(infos, key=lambda x:x[1]),key=lambda x: x[1])
    records = {k:list(g) for k, g in records}
    records = dict(sorted(records.items()))
    
    for key in records.keys():
        n = len(records[key])
        record = records[key]
        ins = [convert(record[i][0]) for i in range(0,n,2)]
        outs = [convert(record[i][0]) for i in range(1,n,2)]
        if n % 2 == 1:
            outs.append(convert("23:59"))
        time = sum([b-a for a, b in zip(ins, outs)])
        
        m = fees[1]
        if time > fees[0]:
            time -= fees[0]
            m += math.ceil(time / fees[2]) * fees[3]
        answer.append(m)
        
        
    return answer