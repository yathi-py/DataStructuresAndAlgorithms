# 1. Two Sum
from typing import List
class Solution:

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        out_list = [nums[0]] #O(1)

        # looping through all the elements in the list O(N)
        for i in range(1,len(nums)):
            if target - nums[i] in out_list: #O(N) because of the in operator
                return [nums.index(target - nums[i]), i]
            else:
                out_list.append(nums[i])


sol = Solution()
print(sol.two_sum(nums = [3,3], target = 6))
# Time complexity
# O(1)+O(N)+O(N) = O(1+2N) ignore all the constants
# O(N)