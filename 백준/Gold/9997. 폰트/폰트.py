import sys

input = sys.stdin.readline

def addBit(S, num):
    return S | (1<<num)

def deleteBit(S, num):
    return S & ~(1<<num)

def checkBit(S, num):
    return S & (1<< num)

def dfs(n, alphabets):
    global dic
    global cnt
    if n >= len(dic):
        if alphabets == (1<<27) -1:
            cnt += 1
        return

    dfs(n + 1, alphabets)

    new_alphabets = alphabets | dic[n]
    dfs(n+1, new_alphabets)

N = int(input())
dic = []

for _ in range(N):
    word = input().rstrip()
    S = (1<<26)
    for w in word:
        S = addBit(S, ord(w)-ord('a'))
    dic.append(S)

cnt = 0
dfs(0, 1 << 26)
print(cnt)