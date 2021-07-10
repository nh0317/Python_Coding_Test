import sys

R=0
C=0
cnt=0
pipeline=False

def dfs(visited, bakery, y,x):
    dx=[1,1,1]
    dy=[-1,0,1]

    visited[y][x]=True
    global pipeline
    if x==C-1:
        pipeline=True
        global cnt
        cnt+=1
        return

    for i in range(3):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<C and 0<=ny<R:
            if bakery[ny][nx] =='.'and not visited[ny][nx]:
                dfs(visited,bakery,ny,nx)
                if pipeline: return


if __name__=='__main__':
    input=sys.stdin.readline
    R, C = map(int,input().split())
    bakery=[[x for x in input().strip() ] for _ in range(R)]

    visited=[[False for _ in range(C)]for _ in range(R)]
    for i in range(R):
        pipeline=False
        dfs(visited,bakery,i,0)
    print(cnt)