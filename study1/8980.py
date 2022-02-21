import sys
import heapq

input = sys.stdin.readline

# 트럭에 실으면 박스는 받는 마을에서만 내림
# 트럭은 지나온 마을로 되돌아가지 않는다.
# 박스 중 일부만 배송 가능
# 트럭으로 배송가능한 최대 박스 수?

N, C = map(int, input().split())
M = int(input())

# 도착지를 인덱스로 하는 그래프
cities = [[] for _ in range(N + 1)]
# 인덱스 까지의 적재량
delivery = [0 for _ in range(N+1)]

# 우선 박스는 분할해서 담을 수 있기 때문에 우선 순위가 높지 않다.
# 최대한 많은 지역에 배달해야함
# 따라서 도착지에 우선순위를 둔다
# 도착지를 기준으로 정렬

for i in range(M):
    u, v, w = map(int, input().split())
    # 도착지를 인덱스로 담아 정렬한 효과를 줌
    cities[v].append([u,w])

answer=0
# 역으로 도착지에서 이 박스를 내려 놓을 수 있는지
# (출발지에서 박스를 담을 수 있는 지)
# 생각해본다.
# 출발지 기준으로 탐색
for i in range(1,N+1):
    # 도착지가 i 인 출발지들에 대해서
    # 얼마다 실을 수 있는 지 계산한다.
    # deliver[i] : i까지 트럭의 용량
    # 출발지에서 최대 수화물보다 용량이 작으면 싣는다.
    # 도착지에 배달하기 전까지는 수화물을 가지고 있어야하므로
    # 출발지부터 도착지 전까지의 모든 도시의 트럭의 용량(deliver)을 싣은 수화물 양만큼 증가시켜야 한다
    # 그렇게 하면 중간 도시에서 최대 용량을 초과하는 문제가 발생한다
    # (예제 2에서 출발지 3, 도착지 4, 용량 50을 싣고 (deliver[3]=40),
    # deliver[2]=0이여서 출발지 2, 도착지 5, 용량 60을 싣는 경우
    # deliver[3]=40+60>60)
    # 따라서 기준을 출발지부터 도착지 사이의 최대 적재량으로 한다.
    for u,w in cities[i]:
        maxC=0
        # 출발지와 도착지 사이에서 최대 적재량을 찾는다.
        for j in range(u,i):
            maxC=max(maxC,delivery[j])

        # 최대 적재량이 트럭의 용량 이하이면
        if maxC+w<=C:
            # 도착지까지의 모든 도시에 대해 수화물을 싣는다.
            for j in range(u,i):
                delivery[j]=delivery[j]+w

            #현재 도시까지 배달한 수화물의 합
            answer=answer+w

        # 일부를 싣는 경우
        elif maxC < C:
            tmp = C-maxC
            for j in range(u,i):
                delivery[j]=delivery[j]+tmp
            answer=answer+tmp
            delivery[u]=C

print(answer)
