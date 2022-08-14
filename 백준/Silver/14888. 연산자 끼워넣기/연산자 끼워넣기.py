import sys
import itertools

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
# 덧셈, 뺄셈, 곱셈, 나눗셈 순서
tmp = list(map(int, input().split()))

operations = '+'*tmp[0] + '-'*tmp[1] + '*'*tmp[2] + '/'*tmp[3]
maxx = -float('inf')
minn = float('inf')
for ops in set(itertools.permutations(operations, N-1)):
    func = str(nums[0])
    result = 0
    for i in range(N-1):
        if ops[i] == '/':
            if int(func) < 0:
                result = abs(int(func)) // nums[i+1]
                result *= -1
            else:
                result = int(func) // nums[i+1]
        else:
            result = eval(func + ops[i] + str(nums[i+1]))
        func = str(result)
    maxx = max(maxx, result)
    minn = min(minn, result)

print(maxx)
print(minn)