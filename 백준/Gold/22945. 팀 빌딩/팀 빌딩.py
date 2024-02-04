import sys
input = sys.stdin.readline

N = int(input())
skill = list(map(int, input().split()))

start = 0
end = len(skill) -1
maxx = 0

while start <= end:
    team = (end - start - 1) * min(skill[start], skill[end])
    maxx = max(team, maxx)

    if skill[start] < skill[end]:
        start += 1
    else :
        end -= 1

print(maxx)