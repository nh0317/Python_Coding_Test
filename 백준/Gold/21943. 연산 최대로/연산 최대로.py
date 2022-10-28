import sys
import itertools

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
plus, mul = map(int, input().split())
maxx = 0

operation_set = set(itertools.product(['*',"+"], repeat = N-1))
operation_set=list(filter(lambda x:x.count("+") == plus and x.count("*")==mul, operation_set))

for num_sets in list(set(itertools.permutations(nums, N))):
    for operations in operation_set:
            pluss = []
            i = 0
            n=num_sets[0]
            for op in operations:
                if op == "+":
                    n += num_sets[i+1]
                    i+= 1
                else:
                    pluss.append(n)
                    n = num_sets[i+1]
                    i+=1
            pluss.append(n)
            res = pluss[0]
            for i in range(1,len(pluss)):
                res *= pluss[i]
            maxx = max(res, maxx)

print(maxx)