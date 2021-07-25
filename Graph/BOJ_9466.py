import sys
from collections import deque

def matching(start,visited):
    que=deque([start])
    team=[]
    while que:
        s=que.popleft()
        if not visited[s]:
            visited[s]=True
            team.append(s)
            next=students[s]
            if visited[next]:
                if next in team:
                    return team[team.index(next):]
            else:
                que.append(next)

input=sys.stdin.readline
T=int(input())
for _ in range(T):
    N=int(input())
    tmp=(list(map(int,input().split())))
    students=[0 for _ in range(N+1)]
    for i in range(1,N+1):
        students[i]=tmp[i-1]
    visited=[False for _ in range(N+1)]
    cnt=N
    for i in range(1,N+1):
        if not visited[i]:
            team=matching(i,visited)
            if team:
                cnt-=len(team)
    print(cnt)


