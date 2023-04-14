from collections import defaultdict
import itertools

def solution(s):
    l = 1
    maxx = 1
    for i in range(1, len(s)):
        for j in range(1, i+1):
            if i - j >= 0 and i + j < len(s):
                if s[i-j] == s[i+j]:
                    l = 1 + j*2
                    maxx = max(maxx, l)
                else: break
                
    
    for i in range(1, len(s)):
        for j in range(1, i+1):
            if i - j >= 0 and i + j -1 < len(s):
                if s[i-j] == s[i+j-1]:
                    l = j*2
                    maxx = max(maxx, l)
                else: break
    return maxx