import itertools
from collections import deque

left, right, center = [], [], []


def shiftRow(rc, n):
    global left
    global right
    global center

    n = n % len(rc)
    for _ in range(n):
        left.appendleft(left.pop())
        right.appendleft(right.pop())
        center.appendleft(center.pop())
    return rc


def rotate(rc, n):
    global left
    global right
    m = (len(rc) + len(rc[0])) * 2 - 4
    n = n % m

    if n == 0:
        return rc

    else:
        for _ in range(n):
            if not center[0] and not center[-1]:
                right.appendleft(left.popleft())
                left.append(right.pop())
            else:
                right.appendleft(center[0].pop())
                left.append(center[-1].popleft())
            
                center[-1].append(right.pop())
                center[0].appendleft(left.popleft())
    return rc


def solution(rc, operations):
    global left
    global right
    global center

    n = 1
    new_rc = deque()
    for i in range(len(rc)):
        new_rc.append(rc[i])

    left = deque([0 for _ in range(len(rc))])
    right = deque([0 for _ in range(len(rc))])
    center = deque()

    for i in range(len(rc)):
        center.append(deque(rc[i][1:-1]))
        
    for i in range(len(rc)):
        right[i] = rc[i][-1]
        left[i] = rc[i][0]

    for k, g in itertools.groupby(operations):
        if k == "ShiftRow":
            new_rc = shiftRow(new_rc, len(list(g)))
        if k == "Rotate":
            new_rc = rotate(new_rc, len(list(g)))

    for i in range(len(rc)):
        new_rc[i][-1] = right[i]
        new_rc[i][0] = left[i]
        
    for i in range(len(rc)):
        for j in range(1, len(rc[0])-1):
            new_rc[i][j] = center[i][j-1]
    return list(new_rc)