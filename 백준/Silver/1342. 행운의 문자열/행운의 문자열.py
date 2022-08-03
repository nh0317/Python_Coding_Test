import sys
from collections import defaultdict, Counter
import math

input = sys.stdin.readline

S = input().rstrip()
alphabets = defaultdict(int)
for s in S:
    alphabets[s] += 1

cnt = 0
def lucky(word):
    global alphabets
    global cnt

    if len(word) == len(S):
        cnt += 1

    for s in alphabets.keys():
        if alphabets[s] > 0 and (s != word[-1:] or word==''):
            alphabets[s] -= 1
            lucky(word+s)
            alphabets[s] += 1

cnt_alphabets = Counter(alphabets.values())
if cnt_alphabets[1] == len(S):
    print(math.factorial(len(S)))
else:
    lucky('')
    print(cnt)

