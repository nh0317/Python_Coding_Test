import sys
from collections import deque

input = sys.stdin.readline

N,M,K = map(int,input().split())

# 양분은 모두 5
# 나무 M개
# 봄에는 나무가 자신의 나이만큼 양분을 먹는다.
# 한칸에 여러 나무 -> 어린 나무부터 양분
# 양분이 부족해서 자기 나이 만큼 못 벅으면 죽음

def spring():
    global farm
    global trees
    global total

    for i in range(N):
        for j in range(N):
            for t in range(len(trees[i][j])):
                if trees[i][j][t] <= farm[i][j]:
                    farm[i][j] -= trees[i][j][t]
                    trees[i][j][t] += 1
                else:
                    for _ in range(t, len(trees[i][j])):
                        farm[i][j] += trees[i][j].pop()//2
                        total -= 1
                    break

# 가을에는 나무 번식, 번식하는 나무는 나이가 5의 배수 인접한 8칸에 나이가 1인 나무 생성
def autumn():
    global trees
    global farm
    global total

    new_trees = []
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                for tree in trees[i][j]:
                    if tree % 5 == 0:
                        for dy, dx in [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]:
                            ny, nx = i+dy, j+dx
                            if 0<= ny < len(farm) and 0<= nx < len(farm[0]):
                                trees[ny][nx].appendleft(1)
                                total += 1
            farm[i][j] += nutrients[i][j]

# K년 후의 나무 개수?
farm = [[5 for _ in range(N)] for _ in range(N)]
nutrients = [list(map(int, input().split())) for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    i, j, tree = map(int, input().split())
    trees[i-1][j-1].append(tree)

for i in range(N):
    for j in range(N):
        trees[i][j].sort()
        trees[i][j] = deque(trees[i][j])

total = M
for _ in range(K):
    spring()
    autumn()


print(total)