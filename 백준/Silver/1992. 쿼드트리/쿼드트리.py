import sys

input = sys.stdin.readline

def check(y,x,n,m):
    global video

    for i in range(y,y+n):
        for j in range(x, x+m):
            if video[y][x] != video[i][j]:
                return False
    return True

def zip_video(y,x,n,m):
    global video

    if check(y,x,n,m):
        return str(video[y][x])
    else:
        return "("+zip_video(y,x,n//2,m//2)+zip_video(y,x+m//2,n//2,m//2)\
               +zip_video(y+n//2,x,n//2,m//2)+zip_video(y+n//2,x+m//2, n//2,m//2)+")"

N = int(input())
video = [list(map(int, input().rstrip())) for _ in range(N)]

print(zip_video(0,0,N,N))
