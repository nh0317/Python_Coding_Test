import sys
input = sys.stdin.readline

N = int(input())

colors = input().rstrip()

red = 0
blue = 0

for i in range(len(colors)-1):
    if colors[i] != colors[i+1]:
        if colors[i]=='R': red += 1
        else: blue += 1
        
if colors[-1] == 'R': red += 1
else : blue += 1
print(min(blue, red) + 1)