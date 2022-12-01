import sys
from collections import defaultdict

input = sys.stdin.readline

while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    row = list(map(int, input().split()))
    children = defaultdict(list)
    parents = defaultdict(int)
    cur = -1
    for i in range(1,len(row)):
        if abs(row[i] - row[i-1]) != 1:
            cur += 1
        children[row[cur]].append(row[i])
        parents[row[i]] = row[cur]
    grandparent = parents[parents[k]]
    cousin = 0
    for siblings in children[grandparent]:
        if siblings == parents[k]:
            continue
        cousin += len(children[siblings])
    print(cousin)
