import sys
from collections import deque
input=sys.stdin.readline

def sort_singers():
    que = deque()
    for i in range(1, N + 1):
        if degree[i] == 0:
            que.append(i)

    result = []
    while que:
        u = que.popleft()
        result.append(u)
        for v in singers[u]:
            degree[v] -= 1
            if degree[v] == 0:
                que.append(v)
    return result

N,M=map(int, input().split())

singers=[[]for _ in range(N+1)]
degree=[0 for _ in range(N+1)]

for i in range(M):
    pd=list(map(int, input().split()))
    n=pd[0]
    for j in range(1,n):
        singers[pd[j]].append(pd[j+1])
        degree[pd[j+1]]+=1

result = sort_singers()
if len(result)==N:
    for r in result:
        print(r)
else : print(0)

