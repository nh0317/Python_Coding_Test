import itertools
import re

def operation(op, expression):
    while re.search("(^-[0-9]+|[0-9]+|[\+\*-]-[0-9]+)"+op+"-*[0-9]+", expression):
        fun = re.search("(^-[0-9]+|[0-9]+|[\+\*-]-[0-9]+)"+op+"-*[0-9]+", expression).group()
        if re.search("[\+\*-]-[0-9]+"+op+"-*[0-9]+("+op+"-*[0-9]+)*", fun):
            fun = fun[1:]
        expression=expression.replace(fun,str(eval(fun)))
        
    return expression

def cal(seq, e):
    for i in seq:
        if i == 0: e=operation("\+",e)
        elif i == 1: e=operation("-",e)
        elif i == 2: e=operation("\*",e)
    # print("res",e)
    return eval(e)

def solution(expression):
    answer = 0
    for seq in set(itertools.permutations([i for i in range(3)],3)):
        answer = max(abs(cal(seq, expression)), answer)
    return answer