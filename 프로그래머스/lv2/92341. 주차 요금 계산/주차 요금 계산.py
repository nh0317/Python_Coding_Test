from collections import defaultdict
import itertools
import math

def cal_fee(time, fee):
    money = fee[1]
    if time > fee[0]:
        time -= fee[0]
        money += math.ceil(time / fee[2]) * fee[3]
    
    return money

def convert(time):
    h, m = map(int, time.split(":"))
    m += 60 *h
    return m 

def solution(fees, records):
    answer = []
    
    infos = []
    cars = defaultdict(list)
    for record in records:
        r = record.split(" ")
        if not cars[r[1]]: cars[r[1]] = [0,False]
        
        if r[2] == "IN":
            cars[r[1]][0] -= convert(r[0])
            cars[r[1]][1] = False
            
        elif r[2] == "OUT":
            cars[r[1]][0] += convert(r[0])
            cars[r[1]][1] = True
    
    cars = dict(sorted(cars.items()))
    for key in cars.keys():
        if not cars[key][1]:
            cars[key][0] += convert("23:59")
        
        answer.append(cal_fee(cars[key][0], fees))
    return answer