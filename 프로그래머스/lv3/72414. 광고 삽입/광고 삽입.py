import time
from collections import Counter
def int_to_strtime(time):
    if time < 10:
        time = '0'+str(time)
    else: time = str(time)
    return time

def strtime(sec):
    h = sec // 3600
    m = sec % 3600
    s = m % 60
    m = m // 60
    return ':'.join([int_to_strtime(h), int_to_strtime(m), int_to_strtime(s)])

def convert(time):
    h, m, s = map(int, time.split(":"))
    s += m * 60
    s += h * 60 * 60
    return s

def solution(play_time, adv_time, logs):
    play_time = convert(play_time)
    adv_time = convert(adv_time)
    dp = [0 for _ in range(play_time + 1)]
    
    for l in logs:
        start, end = l.split("-")
        dp[convert(start)] += 1
        dp[convert(end)] -= 1
    
    for i in range(len(dp)):
        dp[i] = dp[i]+dp[i-1]
    
    viewer = 0
    maxx = dp[adv_time] - dp[0]
    start_time = 0
    for i in range(play_time-adv_time):
        viewer += dp[i+adv_time] - dp[i]
        if maxx < viewer:
            start_time = i + 1
            maxx = viewer
    
    answer = strtime(start_time)
    return answer