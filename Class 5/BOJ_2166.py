import sys

input = sys.stdin.readline
N= int(input())
xpoints=[]
ypoints=[]
for _ in range(N):
    x,y=map(int,input().split())
    xpoints.append(x)
    ypoints.append(y)
xpoints.append(xpoints[0])
ypoints.append(ypoints[0])

A=0
B=0
for i in range(N):
    A+=xpoints[i]*ypoints[i+1]
    B+=ypoints[i]*xpoints[i+1]

print(round(abs(A-B)/2,1))