import sys
import heapq
if __name__=='__main__':
    input=sys.stdin.readline
    N=int(input())
    room=[]

    for i in range(N):
        r, s,e=map(int,input().split())
        heapq.heappush(room,(s,e,r))
    need=0
    inClass=[]
    while room:
        if inClass:
            if inClass[0][0] > room[0][0] :
                need+=1
            else:
                heapq.heappop(inClass)
        else:
            need+=1
        if room:
            s,e,r=heapq.heappop(room)
            heapq.heappush(room,(e,s,r))
    print(need)