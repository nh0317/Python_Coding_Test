cnt = 0
visited = set()

def move(y,x,d):
    global visited
    global cnt
    
    dydx = [[1,0],[0,1],[-1,0],[0,-1]]
    
    ny, nx = y + dydx[d][0], x + dydx[d][1]
    if 0<= ny <11 and 0<= nx<11:
        if (y,x,ny,nx) not in visited:
            cnt += 1
            visited.add((y,x,ny,nx))
            visited.add((ny,nx,y,x))
    else: 
        ny, nx = y, x
    return ny, nx

def solution(dirs):
    global cnt 
    global visited
    y, x = 5, 5
    
    for d in dirs:
        if d == "U":
            y, x = move(y,x,2)
        elif d == "D":
            y, x = move(y,x,0)
        if d == "R":
            y, x = move(y,x,1)
        if d == "L":
            y, x = move(y,x,3)
        # print(y,x,cnt)
        
    return cnt