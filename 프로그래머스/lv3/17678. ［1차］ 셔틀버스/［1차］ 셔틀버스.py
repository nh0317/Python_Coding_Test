import heapq

def convert(time):
    h, m = map(int, time.split(":"))
    m += h * 60
    return m

def format_time(h):
    if h < 10:
        h = '0'+str(h)
    else: h = str(h)
    return h 

def str_convert(m):
    h = m // 60
    m = m % 60
    return ':'.join([format_time(h),format_time(m)])
    
def solution(n, t, m, timetable):
    times = []
    for time in timetable:
        time = convert(time)
        heapq.heappush(times, time)
        
    start = convert("09:00")
    for i in range(n):
        capa = m
        last = start
        
        while times and capa > 0 and times[0] <= start:
            last = heapq.heappop(times)
            capa -= 1
        
        start+=t
        
    if capa == 0:
        return str_convert(last-1)
    else: 
        return str_convert(start-t)