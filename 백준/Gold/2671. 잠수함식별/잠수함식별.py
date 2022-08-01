import sys, re

input = sys.stdin.readline

sound = input().rstrip()

def judge_sound(sound):
    p = re.compile('((01)|(100+1+))+')
    if p.fullmatch(sound) and str(p.fullmatch(sound).group()) == sound:
        return 'SUBMARINE'
    return 'NOISE'

print(judge_sound(sound))

