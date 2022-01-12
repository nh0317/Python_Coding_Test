import sys
from collections import deque

input = sys.stdin.readline
# N : 학생수
# M : 키를 비교한 횟수
# M개 줄에 비교한 두 학생의 번호
# A가 B앞에 서야한다는 의미

N,M = map(int, input().split())
students=[[] for _ in range(N+1)]
degree=[0for _ in range(N+1)]
for _ in range(M):
    a,b=map(int, input().split())
    students[a].append(b)
    degree[b]+=1

que = deque()
result = []
for i in range(1,N+1):
    if degree[i]==0:
        que.append(i)

while que:
    u=que.popleft()
    result.append(u)
    for v in students[u]:
        degree[v]-=1
        if degree[v]==0:
            que.append(v)

for r in result:
    print(r,end=" ")