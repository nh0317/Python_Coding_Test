import sys

input = sys.stdin.readline

N = int(input())
arr = [[' ' for _ in range(N*2)]for _ in range(N)]

def triangle(n,y,x):
    # print(n,y,x)
    if n == 3:
        arr[y][x]="*"
        arr[y+1][x-1],arr[y+1][x+1]="*","*"
        arr[y+2][x-2],arr[y+2][x-1],arr[y+2][x],arr[y+2][x+1],arr[y+2][x+2]="*","*","*","*","*"
        # return
    else:
        triangle(n//2,y,x)
        triangle(n//2,y+n//2,x-n//2)
        triangle(n//2,y+n//2,x+n//2)

def draw(arr):
    for i in range(0,N):
        for j in range(1,N*2+1):
            print(arr[i][j],end="")
        print()

triangle(N,0,N-1)

# 그냥 print 하면 시간 초과 발생
# join 해서 한줄씩 출력
for i in arr:
    print("".join(i))