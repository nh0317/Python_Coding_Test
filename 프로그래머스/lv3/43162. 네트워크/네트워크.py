from collections import deque

def bfs(start, visited, graph):
    visited[start] = True
    q = deque()
    q.append(start)
    
    while q:
        u = q.popleft()
        
        for v in graph[u]:
            if not visited[v]:
                q.append(v)
                visited[v] = True

def solution(n, computers):
    graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
    
    visited = [False for _ in range(n)]
    
    network = 0
    for u in range(n):
        if not visited[u]:
            bfs(u, visited, graph)
            network+=1
            
    return network