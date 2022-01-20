import sys
import itertools

input=sys.stdin.readline


def make_password():
    results=[]
    passwords = list(itertools.combinations(words, L))
    for password in passwords:
        vowels = ['a', 'e', 'i', 'o', 'u']
        cnt = 0
        for p in password:
            for v in vowels:
                if v == p:
                    cnt += 1
        if cnt == L or cnt == 0:
            continue
        elif L-cnt < 2:
            continue
        else:
            result = list(password)
            result.sort()
            results.append("".join(result))
    return results

# L개의 알파벳, 최소 모음 1개 최소 자음 2개
# 암호에서 증가하는 순서로 배열됨
# 조교가 암호를 사용한 문자의 종류는 C가지

L, C = map(int, input().split())
words=list(input().split())
visited = [False for _ in range(L)]
result=make_password()
result.sort()
for r in result:
    print(r)