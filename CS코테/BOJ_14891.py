import sys
input = sys.stdin.readline

gears = ['' for i in range(5)]

def spin(gear, direction):
    if direction == -1:
        return gear[1:]+gear[0] # 반시계
    elif direction == 1:
        return gear[-1]+gear[0:-1] # 시계
    else :return gear


for i in range(1,5):
    gears[i]=(input()[:-1])

K = int(input())
for _ in range(K):
    idx, d=list(map(int, input().split()))
    spins = [ 0 for i in range(5)]
    spins[idx] = d
    for i in range(idx,4):
        if gears[i][2] == gears[i+1][6]:
            spins[i+1] = 0
            d = 0
        else:
            d *= -1
            spins[i+1] = d

    d = spins[idx]
    for i in range(idx,1,-1):
        if gears[i][6] == gears[i-1][2]:
            spins[i-1] = 0
            d=0
        else:
            d *= -1
            spins[i-1] = d

    for i in range(1,5):
        gears[i]=spin(gears[i],spins[i])

answer = 0
for i in range(1,5):
    answer += int(gears[i][0]) * (2**(i-1))

print(answer)
