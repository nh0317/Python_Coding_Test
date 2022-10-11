from collections import deque

import sys

input = sys.stdin.readline
N, M, T = map(int, input().split())
cycle = [deque(list(map(int, input().split()))) for _ in range(N)]
total = 4 * M
summ = sum([sum(x) for x in cycle])

def clock_spin(cycle,x,k):
    for _ in range(k):
        for i in range(len(cycle)):
            if (i + 1) % x == 0:
                last=cycle[i].pop()
                cycle[i].appendleft(last)
    return cycle

def counter_spin(cycle, x, k):
    for _ in range(k):
        for i in range(len(cycle)):
            if (i + 1) % x == 0:
                last=cycle[i].popleft()
                cycle[i].append(last)
    return cycle

def find_same(cycle):
    is_find = False
    delete = []

    for i in range(len(cycle)):
        for j in range(len(cycle[0])):
            find_item = False
            for dy, dx in [[1,0],[0,1],[-1,0],[0,-1]]:
                ny, nx = i + dy, j + dx
                if ny >= len(cycle) or ny < 0:
                    continue
                if nx >= len(cycle[0]):
                    nx = 0
                if cycle[i][j] != 0 and cycle[ny][nx] == cycle[i][j]:
                    delete.append([ny,nx])
                    find_item = True
                    is_find = True

            if find_item:
                delete.append([i,j])

    for i, j in delete:
        cycle[i][j] = 0
    return cycle, is_find

def tunning(cycle):
    summ = sum([sum(x) for x in cycle])
    total = sum([x.count(0) for x in cycle])
    total = len(cycle) * len(cycle[0]) - total

    avg = summ / total

    for i in range(len(cycle)):
        for j in range(len(cycle[0])):
            if cycle[i][j] != 0:
                if cycle[i][j] > avg:
                    cycle[i][j] -= 1
                elif cycle[i][j] < avg:
                    cycle[i][j] += 1
    return cycle

for _ in range(T):
    x, d, k = map(int, input().split())
    if d == 0:
        cycle = clock_spin(cycle,x,k)
    else:
        cycle = counter_spin(cycle,x,k)

    cycle, is_find = find_same(cycle)
    if not is_find:
        cycle = tunning(cycle)

    summ = sum([sum(x) for x in cycle])
    if summ == 0:
        break
print(summ)



