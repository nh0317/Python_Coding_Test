import sys

if __name__=='__main__':
    input=sys.stdin.readline
    N, K = map(int,input().split())
    num=list(map(int,input().strip()))

    stack = []
    cnt=0
    for i in range(N):
        while stack and cnt<K and stack[-1]<num[i]:
            stack.pop()
            cnt+=1
        stack.append(num[i])
    result=''.join(map(str,stack))
    print(result[:N-K]) #숫자가 모두 같아서 반복문으로 제거가 안되는 경우 방지


