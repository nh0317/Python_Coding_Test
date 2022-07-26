import sys, heapq

input = sys.stdin.readline

N, E = map(int, input().split())

graph = [[]for _ in range(N+1)]

def dijkstra(start, graph):
    distance = [float('inf') for _ in range(N+1)]
    distance[start] = 0
    PQ = []
    heapq.heappush(PQ,[0, start])

    while PQ:
        w, u = heapq.heappop(PQ)

        for v, weight in graph[u]:
            summ = w + weight
            if summ < distance[v]:
                distance[v] = summ
                heapq.heappush(PQ,[summ, v])
    return distance

for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append([v,w])
    graph[v].append([u,w])

v1, v2 = map(int, input().split())

# start -> v1 -> v2 -> N
# start -> v2 -> v1 -> N

start = dijkstra(1,graph)
start_v1 = start[v1]
start_v2 = start[v2]

v1_distance = dijkstra(v1,graph)
v1_v2 = v1_distance[v2]
v1_N = v1_distance[N]

v2_distance = dijkstra(v2,graph)
v2_v1 = v2_distance[v1]
v2_N = v2_distance[N]

minn = float('inf')
minn=min(minn, start_v1+v1_v2+v2_N, start_v2+v2_v1+v1_N)
print(minn) if minn != float('inf') else print(-1)