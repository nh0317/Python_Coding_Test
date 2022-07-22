import sys
import itertools

input = sys.stdin.readline

def count_금민수(bound):
    # bound보다 작은 금민수의 개수
    # = (bound 자리수까지의 금민수의 개수) - (그중 bound 보다 큰 것의 개수)

    nums = ['4','7']
    n=len(str(bound)) + 1

    # bound 자리수까지 금민수의 개수
    # ex) bound = 74
    # -> 4,7,44,47,74,77
    # -> 2 ** 1 + 2 ** 2
    # -> 2 ** 3 - 2
    bound_total = 2 ** n - 2

    # bound 자리수인 금민수 중, bound 보다 큰 것
    # ex) bound = 74
    # -> 77 -> 1개
    arr = list(itertools.product(nums, repeat=n-1))
    cnt = 0
    for a in arr:
        num = int(''.join(a))
        if num > bound:
            cnt += 1
        if num == bound: # 경계값 예외처리
            global check
            check= True

    return bound_total - cnt

check = False
A, B = map(int, input().split())

cnt_A = count_금민수(A)
if check : cnt_A -= 1 # A가 금민수에 포함 되는 경우
# 74 77의 경우
# 4 7 44 47
# 4 7 44 47 74 77

cnt_B = count_금민수(B)

print(cnt_B - cnt_A)

