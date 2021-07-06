import sys
import heapq

def Dijkstra(graph, start):
    distance = [float('inf')] * (V + 1)
    distance[start] = 0

    PQ = []
    heapq.heappush(PQ, (0, start))

    while PQ:
        weight, next = heapq.heappop(PQ)
        for v in graph[next]:
            sum = weight + 1
            if (sum < distance[v]):
                distance[v] = sum
                heapq.heappush(PQ, (sum, v))

    return distance

if __name__ =='__main__':
    V, E, min, start =map(int, sys.stdin.readline().split())
    graph =[[]for i in range(V+1)]

    for i in range(E):
        A,B=map(int, sys.stdin.readline().split())
        graph[A].append(B)

    distance=Dijkstra(graph,start)

    result = []
    for i in range(1, V + 1):
        if (distance[i] == min):
            result.append(i)

    result.sort()
    if not result:
        print(-1)
    else:
        for r in result:
            print(r)

