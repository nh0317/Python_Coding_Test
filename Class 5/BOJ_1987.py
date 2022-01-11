import sys

sys = sys.stdin.readline
R,C = map(int,input().split())
board = [[ ord(x)-65 for x in list(input())] for _ in range(R)]
visited = [[False for _ in range(C)]for _ in range(R)]
max_len=-1
alphabets = [False for _ in range(26)]
alphabets[board[0][0]]=True
def dfs(y,x,cnt):
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    global max_len
    if max_len==26:
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<C and 0<= ny <R:
            if not alphabets[board[ny][nx]] and not visited[ny][nx]:
                visited[ny][nx]=True
                alphabets[board[ny][nx]]=True
                dfs(ny,nx,cnt+1)
                visited[ny][nx]=False
                alphabets[board[ny][nx]]=False
    else :
        max_len = max(max_len,cnt)

dfs(0,0,1)
print(max_len)

#defaultdic의 시간 복잡도는 worst가 n
#따라서 문자열을 아스키 코드로 변환하고 이를 이용해서 중복을 확인해야 한다.