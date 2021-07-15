import sys
import heapq
if __name__=='__main__':
    input=sys.stdin.readline
    N=int(input())
    inClass=[]
    lecture=[]

    for i in range(N):
        r, s,e=map(int,input().split())
        heapq.heappush(lecture,(s,e,r))
    need=0

    while lecture:
        if inClass:
            # 진행 중인 수업이 안 끝난 경우
            if inClass[0][0] > lecture[0][0]:
                need+=1

            else:
                heapq.heappop(inClass)
        else:
            need+=1
        if lecture:
            s,e,r= heapq.heappop(lecture)
            heapq.heappush(inClass,(e,s,r))

    print(need)