import sys

#1:위쪽 2:왼쪽 3:아래 3:오른쪽
def dfs(x,y,r):
    global cnt

    dy=[-1,0,1,0]
    dx=[0,1,0,-1]

    if Room[y][x]==1:
        return

    if not visited[y][x]:
        cnt+=1
        visited[y][x]=True

    for i in range(1,5):
        nr=(r-i+4)%4
        nx=x+dx[nr]
        ny=y+dy[nr]
        if 0<=nx<M and 0<=ny<N:
            if not visited[ny][nx] and Room[ny][nx]==0:
                dfs(nx,ny,(nr)%4)
                return
    #4방향 모두 청소 or 벽
    nx=x-dx[r]
    ny=y-dy[r]
    if 0<=nx<M and 0<=ny<N:
        # 후진
        if Room[ny][nx]==0:
            dfs(nx,ny,r)
        else: return
    return

input=sys.stdin.readline
N,M=map(int, input().split())
y,x,d=map(int, input().split())
Room=[list(map(int, input().split())) for _ in range(N)]
visited=[[False for _ in range(M)] for _ in range(N)]

cnt=0
dfs(x,y,d)
print(cnt)
