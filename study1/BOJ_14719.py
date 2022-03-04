import sys

input = sys.stdin.readline

H,W = map(int,input().split())

blocks = [[0 for _ in range(W)]for _ in range(H)]
heights = list(map(int,input().split()))

for i in range(W):
    for j in range(0,heights[i]):
        blocks[j][i]=1

rains = 0
for i in range(H):
    left=-1
    right=-1
    for j in range(W):
        if blocks[i][j]==1:
            # 오른쪽 벽
            if j>0 and blocks[i][j-1]==0:
                right=j
                if left != -1:
                    rains += right - left -1
            #왼쪽 벽
            if j<W-1 and blocks[i][j+1]==0:
                left=j
print(rains)