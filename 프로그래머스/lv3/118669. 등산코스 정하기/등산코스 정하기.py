import heapq

graph = []
def dijkstra(start, n):
    global graph
    global intensity
    
    intensity[start] = 0
    pq = []
    heapq.heappush(pq, [0,start])
    
    while pq:
        w, u = heapq.heappop(pq)
        
        if intensity[u] < w:
            continue
            
        for v, weight in graph[u]:
            # max(intensity[u], weight) = 최대 intensity
            # intensity가 최대인 것이 최소이면
            if intensity[v] > max(intensity[u], weight):
                # 최대 intensity를 저장
                intensity[v] = max(intensity[u], weight)
                heapq.heappush(pq, [intensity[v],v])
                
    return intensity


def solution(n, paths, gates, summits):
    global graph
    global intensity
    intensity = [float('inf') for _ in range(n+1)]
    
    summits = set(summits)
    gates = set(gates)
    graph = [[] for _ in range(n+1)]
    for i, j, w in paths:
        if i in gates or j in gates:
            if i in gates:
                graph[i].append([j,w])
            else:
                graph[j].append([i,w])
        elif i in summits or j in summits:
            if j in summits:
                graph[i].append([j,w])
            else:
                graph[j].append([i,w])
        else:
            graph[i].append([j,w])
            graph[j].append([i,w])
            
    top_list = []
    for gate in gates:
        intensity = dijkstra(gate, n)
    
    # print(intensity)
    for summit in summits:
        heapq.heappush(top_list, [intensity[summit], summit])
        
    return [top_list[0][1], top_list[0][0]]