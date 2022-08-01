import sys, re

input = sys.stdin.readline

sound = input().rstrip()

def judge_sound(sound):
    p100 = re.compile('((01)*(100+1+)+)*')
    if p100.fullmatch(sound) and str(p100.fullmatch(sound).group()) == sound:
        return 'SUBMARINE'

    p01 = re.compile('((100+1+)*(01)+)*')
    if p01.fullmatch(sound) and str(p01.fullmatch(sound).group()) == sound:
        return 'SUBMARINE'
    return 'NOISE'


print(judge_sound(sound))

