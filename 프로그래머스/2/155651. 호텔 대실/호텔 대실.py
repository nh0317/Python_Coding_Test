import heapq

def hourToMin(book_time):
    hour,mins = map(int, book_time.split(":"))
    mins += hour*60
    return mins

def solution(book_time):
    answer = 1
    times = []
    booked = []
    for start, end in book_time:
        times.append([hourToMin(start), hourToMin(end)+10])
    times.sort(key=lambda x : x[0])
    
    booked.append(times[0][1])
    times.pop(0)
    for time in times:
        if booked[0] > time[0]:
            answer += 1
        else:
            heapq.heappop(booked)
        heapq.heappush(booked, time[1])
        
    return answer