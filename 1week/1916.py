import sys
import heapq

def Dijkstra(start,W):
    distance = [float('inf')] * (V + 1)
    distance[start] = 0

    PQ = []
    heapq.heappush(PQ, (0, start))

    while PQ:
        weight, next = heapq.heappop(PQ)
        for v, w in W[next]:
            sum = w + weight
            if (sum < distance[v]):
                distance[v] = sum
                heapq.heappush(PQ, (sum, v))
    return distance

if __name__=='__main__':
    V = int(sys.stdin.readline())
    E = int(sys.stdin.readline())

    W=[[]for i in range(V+1)]

    for i in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        W[u].append((v,w))

    start, destination = map(int,sys.stdin.readline().split())
    result=Dijkstra(start,W)

    print(result[destination])



