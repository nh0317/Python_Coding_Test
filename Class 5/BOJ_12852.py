import sys
from collections import deque

input=sys.stdin.readline
N=int(input())
bit=1<<(N-1)
# q=deque([])
# q.append((N,bit,0))
# final=0
# result=[]
# minCnt=float('inf')
# while q:
#     n,bit,cnt=q.popleft()
#     if n==1 and cnt<minCnt:
#         minCnt=cnt
#         final=bit
#     if minCnt < cnt:
#         continue
#     # print(n,bit,cnt,final, minCnt,q)
#     if n % 2==0 and n//2>0 and minCnt>=cnt+1:
#         bit=bit | 1 << (n//2-1)
#         q.append((n//2,bit,cnt+1))
#         bit=bit & ~(1<<(n//2-1))
#     if n%3 ==0 and n//3>0 and minCnt>=cnt+1:
#         bit=bit | 1 << (n//3-1)
#         q.append((n//3,bit,cnt+1))
#         bit=bit & ~(1<<(n//3-1))
#     if n>1 and minCnt>=cnt+1:
#         bit=bit | 1 << (n-2)
#         q.append((n-1,bit,cnt+1))
#         bit=bit & ~(1<<(n-2))
# print(minCnt)
# for i in range(N,0,-1):
#     if final & 1<<(i-1)!=0:
#         print(i,end=" ")

dp=[i-1 for i in range(N+1)]

n=1
cur=bit
result=[0 for i in range(max(4,N+1))]
result[2]=1
result[3]=1
for n in range(1,N+1):
   if n*2 <=N:
       if dp[n*2] > dp[n]+1:
           dp[n*2]=dp[n]+1
           result[n*2]=n

   if n * 3 <= N:
       if dp[n*3] > dp[n]+1:
           dp[n*3]=dp[n]+1
           result[n*3]=n
   if n + 1 <= N:
       if dp[n+1] > dp[n]+1:
           dp[n+1]=dp[n]+1
           result[n+1]=n

print(dp[N])

n=N
while n >0:
    print(n, end=" ")
    n=result[n]

# 참고:https://code-conquer.tistory.com/57
