import sys
import itertools
input = sys.stdin.readline


def floyd(graph):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j: graph[i][j] = 0

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph

def pick_buildings(graph):
    buildings = list(itertools.combinations(range(1,N+1),2))
    times = cal_min_times(graph, buildings)
    min_idx = pick_min_time(times)
    return buildings[min_idx][0], buildings[min_idx][1], times[min_idx] * 2

def cal_min_times(graph, buildings):
    times = []
    for u, v in buildings:
        time = 0
        for i in range(1, N + 1):
            time += min(graph[i][u], graph[i][v])
        times.append(time)
    return times

def pick_min_time(times):
    min_time = times[0]
    min_idx = 0
    for i in range(len(times)):
        if times[i] < min_time:
            min_time = times[i]
            min_idx = i
    return min_idx


N,M = map(int, input().split())

graph = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    u,v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

graph = floyd(graph) # 건물별 거리 구하기
for answer in pick_buildings(graph):
    print(answer, end=" ")



