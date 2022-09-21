def convert_time(h,m,s):
    m += h * 60 
    s += m * 60
    return int(s * 1000)
    
def solution(lines):
    answer = 0
    times = []
    for line in lines:
        day, time, period = line.split()
        period = float(period.replace("s",""))
        period = int(period * 1000)
        h, m, s = map(float, time.split(":"))
        t = convert_time(h,m,s)
        times.append([t- period + 1,t])
    
    max_end = times[0][1]
    cnt = 0
    max_cnt = 0
    
    for start, end in times:
        cnt = 0
        for j in range(len(times)):
            if end <= times[j][0] < end +1000:
                cnt += 1
            elif end <= times[j][1] < end +1000:
                cnt += 1
            elif times[j][0] <= end and end+1000 <= times[j][1]:
                cnt += 1
        max_cnt = max(max_cnt, cnt)
            
    max_cnt = max(max_cnt, cnt)
    return max_cnt