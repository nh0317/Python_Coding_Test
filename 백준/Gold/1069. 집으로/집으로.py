import sys
import math

input = sys.stdin.readline

X, Y, D, T = map(int, input().split())
distance = math.sqrt(X**2 + Y**2)

cnt = 0
jmp = 0
if D/T > 1:
    if distance >= D:
        jmp = distance // D
        cnt = jmp * T
        distance %= D

    # 남은 거리를 걸어가는 경우, jump할 수 있는 거리까지 걸어간 다음 jump하는 경우,
    # 이등변 삼각형의 빗변이 남은 거리가 되도록 잘 2번 점프해서 도착하는 경우
    if jmp == 0:
        cnt += min(distance, T + (D-distance), 2.0*T)
    # 남은 거리를 걸어가는 경우, 다각형 모양으로 걸어가는 경우
    else:
        cnt += min(distance, T)
    print(cnt)
else:
    print(distance)

