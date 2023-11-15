from collections import deque

def find_start(maps):
    for i,low in enumerate(maps):
        for j, column in enumerate(low):
            if maps[i][j] == 'S':
                return i, j
            
def find_end(maps):
    for i,low in enumerate(maps):
        for j, column in enumerate(low):
            if maps[i][j] == 'E':
                return i, j
            
def find_lever(maps):
    for i,low in enumerate(maps):
        for j, column in enumerate(low):
            if maps[i][j] == 'L':
                return i, j

def bfs(maps, start, end):
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    q = deque([[start[0], start[1]]])
    
    while q:
        y, x = q.popleft()
        # if maps[y][x] == 'E' and lever:
        #     return cnt
        
        for dy, dx in [[0,1],[1,0],[-1,0],[0,-1]]:
            ny, nx = y + dy, x + dx
            if 0<= ny < len(maps) and 0<= nx < len(maps[0]) and visited[ny][nx] == 0:
                if maps[ny][nx] != 'X':
                    q.append([ny, nx])
                    visited[ny][nx] = visited[y][x] + 1

    return visited[end[0]][end[1]]

def solution(maps):
    answer1 = bfs(maps, find_start(maps), find_lever(maps))
    answer2 = bfs(maps, find_lever(maps), find_end(maps))
    
    return answer1 + answer2 if answer1 != 0 and answer2 != 0 else -1