import sys
import heapq

def Dijkstra(graph):
    distance = [float('inf')]*(V+1)
    start = 1
    distance[start] = 0
    PQ = []
    heapq.heappush(PQ, (0, start))

    while PQ:
        weight, next = heapq.heappop(PQ)
        for v, w in graph[next]:
            sum = w + weight
            if (sum < distance[v]):
                distance[v] = sum
                heapq.heappush(PQ, (sum, v))
    return distance

if __name__=='__main__':
    m,n= map(int, sys.stdin.readline().split())
    V=m*n
    Map =[[0 for j in range(m)]for i in range(n) ]
    Map = [list(map(int, input())) for y in range(n)]

    # Make Graph
    graph = [[]for i in range(V+1)]

    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    vertexNum=0
    for i in range(n):
        for j in range(m):
            vertexNum+=1
            for move in range(4):
                x=j+dx[move]
                y=i+dy[move]
                if(x>=0 and x<m and y>=0 and y<n):
                    u1=vertexNum+dx[move]+m*dy[move]
                    graph[vertexNum].append((u1,Map[y][x]))


    result = Dijkstra(graph)
    print(result[V])

