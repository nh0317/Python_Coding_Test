import sys,copy

def moveCommon(blocks,check,ny,nx,d):
    dy=[1,-1,0,0]
    dx=[0,0,1,-1]
    if blocks[ny][nx] != 0:
        while 0 <= ny + dy[d] < N and 0 <= nx + dx[d] < N:
            preY, preX=ny,nx
            ny += dy[d]
            nx += dx[d]
            if( blocks[ny][nx]==0 or (blocks[ny][nx]==blocks[preY][preX] and not check[ny][nx] and not check[preY][preX])):
                if blocks[ny][nx] == 0:
                    blocks[ny][nx] = blocks[preY][preX]
                    blocks[preY][preX]=0

                    check[ny][nx] = check[preY][preX]
                    check[preY][preX] = False

                elif blocks[ny][nx] == blocks[preY][preX]:
                    if not check[ny][nx] and not check[preY][preX]:
                        blocks[ny][nx] += blocks[preY][preX]
                        blocks[preY][preX] = 0

                        check[ny][nx] = True
                        check[preY][preX] = False
    return

def move(blocks,d):
    dy=[1,-1,0,0]
    dx=[0,0,1,-1]

    check = [[False for _ in range(N)] for _ in range(N)]
    if d==0:
        for i in range(N-1,-1,-1):
            for j in range(N):
                moveCommon(blocks,check,i,j,d)

    elif d==1:
        for i in range(N):
            for j in range(N):
                moveCommon(blocks,check,i,j,d)

    elif d==2:
        for j in range(N-1,-1,-1):
            for i in range(N):
                moveCommon(blocks,check,i,j,d)
    elif d==3:
        for j in range(N):
            for i in range(N):
                moveCommon(blocks,check,i,j,d)
    return

def printArr(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()
    print()
    return

def play(blocks, cnt):
    global maxBlock
    if cnt ==5:
        for i in range(N):
            for j in range(N):
                maxBlock=max(maxBlock,blocks[i][j])
        return
    temp=copy.deepcopy(blocks)
    for i in range(4):
        move(blocks,i)
        play(blocks, cnt+1)
        blocks=copy.deepcopy(temp)

input=sys.stdin.readline
N=int(input())
blocks = [[ int(x) for x in (input().split())] for _ in range(N)]
global maxBlock
maxBlock=0
play(blocks, 0)
print(maxBlock)


