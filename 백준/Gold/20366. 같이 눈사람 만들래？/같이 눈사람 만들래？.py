import sys

input = sys.stdin.readline

N = int(input())
snowball = list(map(int, input().split()))
snowball.sort()
minn = (snowball[-1] - snowball[0]) * 2

for i in range(N-3):
    for j in range(i+3, N):
        fix = snowball[i] + snowball[j]
        start = i + 1
        end = j - 1
        while start < end:
            snowman = snowball[start] + snowball[end]
            minn = min(minn, abs(fix-snowman))
            if fix > snowman:
                start += 1
            else:
                end -= 1
print(minn)
