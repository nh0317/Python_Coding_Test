import datetime
import heapq
# import time


def solution(n, t, m, timetable):
    answer = ''
    times = []
    for T in timetable:
        hour, minute =map(int, T.split(":"))
        heapq.heappush(times, datetime.datetime.strptime(T,"%H:%M"))
        # times.append(datetime.time(hour, minute))
    
    startTime = datetime.datetime.strptime("09:00","%H:%M")
    for i in range(n):
        capa=m
        lastTime = startTime
        if i != 0:
            startTime = startTime + datetime.timedelta(minutes=t)
        for j in range(m):
            if ( times and startTime >= times[0]):
                lastTime = heapq.heappop(times)
                capa -= 1
            if i==n-1 and capa==0:
                lastTime = lastTime - datetime.timedelta(minutes=1)
                answer = lastTime.strftime("%H:%M")
            elif i==n-1 and capa>0:
                answer = startTime.strftime("%H:%M")
    
    return answer