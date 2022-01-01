import sys

input=sys.stdin.readline

answer=0
cnt =0
def queens(i, col):
    # print(i, col, memo)
    global cnt
    cnt+=1
    #i-1번째 퀸까지 서로 위협하는 가
    if (promising(i,col)):
        if (i==N):
            global answer
            answer+=1
        else:
            for j in range(1, N+1):
                #col[i] =j : i번째 행의 j 열에 퀸을 하나 둔다
                if (memo[j]):
                    col[i + 1] = j
                    memo[j]=False
                    queens(i + 1, col)
                    memo[j]=True

#서로 위협하는 가
def promising(i,col):
    switch = True #위협하지 않는 경우
    k=1
    while(k<i and switch):
        #같은 열에 있거나 대각선상에 있거나
        if (col[i]==col[k]) or abs(col[i]-col[k]) == abs(i-k) :
           switch = False
        k+=1
    return switch

N=int(input())
col = [ 0 for _ in range(N+1)]
memo = [ True for _ in range(N+1)]
queens(0,col)
print(answer)