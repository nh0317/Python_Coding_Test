import itertools
import copy

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        reverse = sorted(nums, reverse=True)
        if nums == reverse:
            nums.reverse()
            return
        
        for i in range(len(nums)-1,0,-1):
            if nums[i-1] < nums[i]:
                if i == len(nums)-1:
                    least = nums[-1]
                    nums[-1] = nums[-2]
                    nums[-2] = least
                    return
                else:
                    print(nums[i-1],nums[i])
                    # nums[i-1] 보다 큰 바로 다음 수를 찾는다. 
                    minn = nums[i-1]
                    idx = i-1
                    for j in range(i, len(nums)):
                        if nums[i-1] < nums[j]:
                            minn = min(nums[j], minn)
                            idx = j
                    
                    print(nums[idx], idx)
                    # nums[i-1]과 nums[idx]를 swap
                    least = nums[i-1]
                    nums[i-1] = nums[idx]
                    nums[idx] = least
                    
                    # nums[i]부터 sort
                    
                    nums[i:] = sorted(nums[i:])
                    return 
                    
                    