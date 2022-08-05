import sys
import copy
input = sys.stdin.readline

def print_arr(arr):
    for a in arr:
        for aa in a:
            print(aa, end=" ")
        print()
    print()

def rotate90(puzzle):
    rotated = [[0 for _ in range(len(puzzle))] for _ in range(len(puzzle[0]))]

    for i in range(len(rotated)):
        for j in range(len(rotated[0])):
            rotated[i][-j-1] = puzzle[j][i]
    return rotated

def draw(y,x,puzzle):
    global mapp
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if y+i < len(mapp) and x+j < len(mapp[0]):
                if mapp[y+i][x+j] + puzzle[i][j] == 2:
                    return False
                mapp[y+i][x+j] = puzzle[i][j]
    return True

def check(y,x,puzzle):
    global mapp
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if y+i < len(mapp) and x+j < len(mapp[0]):
                if mapp[y+i][x+j] + puzzle[i][j] == 2:
                    return False
                # mapp[y+i][x+j] = puzzle[i][j]
    return True

def count(y,x):
    global turn
    global fixed

    y1 = min(y,len(mapp)//3)
    x1 = min(x,len(mapp)//3)

    y2 = max(y+len(turn) -1,len(mapp)//3+len(fixed) -1)
    x2 = max(x+len(turn[0]) -1,len(mapp)//3+len(fixed[0]) -1)

    return (y2 - y1 + 1) * (x2 - x1 + 1)

n1, m1 = map(int, input().split())
puzzle1 = [list(map(int, input().rstrip())) for _ in range(n1)]

n2, m2 = map(int, input().split())
puzzle2 = [list(map(int, input().rstrip())) for _ in range(n2)]


fixed, turn = puzzle1, puzzle2
if n1 * m1 <= n2 * m2:
    fixed = puzzle2
    turn = puzzle1
else:
    fixed = puzzle1
    turn = puzzle2

maxx = max(m1,n1,m2,n2)
mapp = [[0 for _ in range(maxx * 3 +1)] for _ in range(maxx * 3+1)]

draw(len(mapp)//3,len(mapp)//3,fixed)

cnt = 151 * 151
for i in range(len(mapp)-len(turn)):
    for j in range(len(mapp[0])-len(turn[0])):
        for _ in range(4):
            turn = rotate90(turn)
            if check(i, j, turn):
                cnt=min(cnt, count(i,j))

print(cnt)


