import sys
import heapq

def Dijkstra(W, distance, start):
    PQ = []
    heapq.heappush(PQ, (0, start))

    while PQ:
        weight, next = heapq.heappop(PQ)
        for v, w in W[next]:
            sum = weight + w
            if (sum < distance[v]):
                distance[v] = sum
                heapq.heappush(PQ, (sum, v))
    return distance


if __name__ == '__main__':
    V, E = map(int, sys.stdin.readline().split())
    start = int(sys.stdin.readline())

    W = [[] for i in range(V + 1)]
    for i in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        W[u].append((v, w))

    distance = [float('inf')] * (V + 1)
    distance[start] = 0

    result = Dijkstra(W, distance, start)

    for i in range(1, V + 1):
        if result[i] == float('inf'):
            print("INF")
        else:
            print(result[i])



# 틀렸던 부분
# 메모리 부족
# 우선순위 큐를 사용하지 않았고, 2차원 배열을 사용해서 발생한 문제
# 우선순취 큐를 이용하고, 2차원 배열 대신 리스트에 튜플을 추가하여 경로와 가중치를 저장
# 파이썬 문법에 익숙해질 것

# vertices를 0부터 시작하여 문제 발생
# 정확한 이유는 모르겠지만 가독성을 위해서도 vertices 번호를 1부터 시작하자