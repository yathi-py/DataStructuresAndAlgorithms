# 1. Two Sum


# Solution : Hashing

# https://leetcode.com/problems/two-sum/
from typing import List
class Solution:

    def two_sum_hashing(self, nums: List[int], target: int) -> List[int]:
        out_dict = {} #O(1)

        for idx, val in enumerate(nums):  # O(N)
            diff = target-val
            if diff in out_dict:  # O(N)
                return [out_dict[diff],idx]
            out_dict[val] = idx

#solution
# time complexity O(N)
    # calculations
    # O(1)+O(N)+O(N) = O(1+2N) ignore all the constants
    # O(N)
# space complexity O(N) we need extra dict


    def two_sum_two_pointer(self, nums: List[int], target: int) -> List[int]:
       sort_nums = sorted(nums)
       left, right = 0, len(nums)-1
       while left < right:
           total_sum = sort_nums[right] + sort_nums[left]
           if total_sum == target:
               return [left, right]
           elif total_sum < target:
               left += 1
           else:
               right -= 1

#solution
# time complexity O(N)
# space complexity O(1)

sol = Solution()
print(sol.two_sum_two_pointer(nums = [2,7,11,15], target = 4))
