import sys

input = sys.stdin.readline


def learn_word(word, cnt):
    global learned
    global words
    global maxx

    if cnt ==  K:
        read = 0
        for ws in words:
            for w in ws:
                if not learned[ord(w)-ord('a')]:
                    break
            else: read += 1
        maxx = max(maxx, read)

    else:
        for w in range(word, 26):
            if not learned[w] and cnt < K:
                learned[w] = True
                learn_word(w,cnt+1)
                learned[w] = False


N, K = map(int, input().split())
words = [input().rstrip()[4:-4] for _ in range(N)]

maxx = 0
learned = [0 for _ in range(26)]
for a in 'anict':
    learned[ord(a) - ord('a')] = True

if K < 5:
    print(0)

elif K == 26:
    print(N)
else :
    K-=5
    learn_word(0,0)
    print(maxx)