import sys

input = sys.stdin.readline

# 산성 양수, 알칼리 음수
# 혼합 용약은 특성 값의 합
# 세 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만든다.

def sol():
    three=[]
    min_l=float('inf')
    for i in range(N-3):
        standard=liquids[i]
        start = i+1
        end=N-1
        sum_l=0
        while start<end:
            sum_l = standard+liquids[start]+liquids[end]
            if abs(sum_l) <= abs(min_l):
                three=[standard,liquids[start],liquids[end]]
                min_l=sum_l
            if sum_l<0:
                start+=1
            elif sum_l>0:
                end-=1
            else:
                three=[standard,liquids[start],liquids[end]]
                return three
    return three

N=int(input())
liquids=list(map(int,input().split()))
liquids.sort()
three=sol()
three.sort()
for liquid in three:
    print(liquid,end=" ")
