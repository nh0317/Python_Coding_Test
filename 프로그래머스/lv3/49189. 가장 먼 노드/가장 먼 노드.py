import heapq

def dijkstra(start, n, graph):
    distance = [float('inf') for _ in range(n+1)]
    distance[start] = 0
    pq = []
    heapq.heappush(pq, [0, start])
    
    while pq:
        d, u = heapq.heappop(pq)
        
        for v, w in graph[u]:
            if d + w < distance[v]:
                distance[v] = d + w
                heapq.heappush(pq, [distance[v], v])
                
    return distance[1:]
            
    

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    
    for u, v in edge:
        graph[u].append([v,1])
        graph[v].append([u,1])
    
    distance = dijkstra(1, n, graph)
    maxx = max(distance)
        
    return distance.count(maxx)