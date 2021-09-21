import math
import sys
from itertools import combinations

def vector_sum(v):
    sumX=0
    sumY=0
    for x,y in v:
        sumX+=x
        sumY+=y
    return sumX, sumY

def vector_length(v1,  v2):
    return math.sqrt((v1[0]-v2[0])**2 + (v1[1]-v2[1])**2)

input=sys.stdin.readline
T=int(input())

for _ in range(T):
    N=int(input())
    P=[]

    totalX,totalY=0,0
    for i in range(N):
        x,y = map(int,input().split())
        P.append((x,y))
        totalX+=x
        totalY+=y

    plus = list(combinations(P,N//2))
    print(plus)
    minLen = float('inf')
    for i in range(len(plus)//2):
        sumV=vector_sum(plus[i])
        sumV2= totalX-sumV[0], totalY-sumV[1]
        length= vector_length(sumV, sumV2)
        minLen=min(length,minLen)
    print(minLen)