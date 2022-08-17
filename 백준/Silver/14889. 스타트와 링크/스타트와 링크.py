import sys
import itertools

input = sys.stdin.readline

N =int(input())

ability = [list(map(int, input().split())) for _ in range(N)]

members = set([i for i in range(N)])

minn = float('inf')
for team in set(itertools.combinations(members, N//2)):
    team2 = members- set(team)
    sum1 = 0
    for i, j in set(itertools.combinations(team, 2)):
        sum1 += ability[i][j]
        sum1 += ability[j][i]

    sum2 = 0
    for i, j in set(itertools.combinations(team2,2)):
        sum2 += ability[i][j]
        sum2 += ability[j][i]
    minn = min(minn, abs(sum1-sum2))
print(minn)
