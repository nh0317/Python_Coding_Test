import sys
input = sys.stdin.readline

def choose_home(mid):
    pre=homes[0]
    cnt=1
    for i in range(N):
        if homes[i]-pre>=mid:
            pre=homes[i]
            cnt+=1
    return cnt

N,C = map(int,input().split())
homes=[]
for _ in range(N):
    homes.append(int(input()))
homes.sort()

min_gap=1
max_gap= homes[N - 1] - homes[0]
cnt=1
answer=0

while (min_gap <= max_gap):
    mid = (max_gap + min_gap) // 2
    cnt = choose_home(mid)
    if(cnt<C):
        max_gap= mid - 1
    else:
        answer=mid
        min_gap= mid + 1

print(answer)