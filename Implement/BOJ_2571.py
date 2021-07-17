import sys

def check(x,y,w,maxArea):
    area=0
    minHeight=100
    for i in range(x,x+w):
        height=0
        for j in range(y,100):
            if(white[j][i]==0): break
            height+=1
        minHeight= min(minHeight,height)
        area=minHeight*w
        if maxArea>area: break
    return area

input = sys.stdin.readline
n=int(input())
white=[[0 for _ in range(100)] for _ in range(100)]

for i in range(n):
    y,x= map(int,input().split())

    for j in range(10):
        for k in range(10):
            if white[j+y][k+x]!=1:
                white[j+y][k+x]=1

maxArea=0
for i in range(100):
    for j in range(100):
        if white[i][j]!=0:
            for w in range(100):
                x=j+w
                if(x>=100):break
                area=check(j,i,w+1,maxArea)
                maxArea=max(area,maxArea)
print(maxArea)