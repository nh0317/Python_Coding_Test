import sys
import heapq

if __name__=='__main__':
    jewNum,bagNum=map(int,sys.stdin.readline().split())

    items=[]
    for i in range(jewNum):
        w,p=map(int, sys.stdin.readline().split())
        heapq.heappush(items,(w,p))

    bags=[]
    for i in range(bagNum):
        heapq.heappush(bags,int(sys.stdin.readline()))

    profitSum=0
    canSteal=[]
    while bags:
        bag=heapq.heappop(bags)
        while items and items[0][0]<=bag:
            p=heapq.heappop(items)[1]
            heapq.heappush(canSteal,-p) #maxheap
        if canSteal:
            profitSum-=heapq.heappop(canSteal)
        elif not items: break

    print(profitSum)



# 시간 초과
# 자료구조를 2개 사용하자
# lindearsearch 보다 heapq를 사용하자
# input 사용하지 말것..
