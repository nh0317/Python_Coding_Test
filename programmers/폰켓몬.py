def solution(nums):
    answer = 0
    R = len(nums)//2
    answer = len(set(nums))
    if answer >= R:
        return R
    elif answer < R:
        return answer