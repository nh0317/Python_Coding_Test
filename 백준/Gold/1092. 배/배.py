import sys
from collections import deque
input = sys.stdin.readline

def load(weights, boxes):
    weights.sort(reverse=True)
    boxes.sort(reverse=True)
    boxes = deque(boxes)

    if weights[0] < boxes[0]:
        return -1

    cnt = 0
    while boxes:
        for i, w in enumerate(weights):
            for box in boxes:
                if w >= box:
                    boxes.remove(box)
                    break
        cnt+=1
    return cnt

N = int(input())
weights = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

print(load(weights, boxes))

