# 53. Maximum Subarray
# Kadane's algorithm (Dynamic programming)

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = nums[0]   #O(1)

        for val in nums:   #O(N)
            cur_sum = max(val, cur_sum+val)  #O(1)
            max_sum = max(cur_sum, max_sum)

        return max_sum

# Time Complexity
# = O(1) + O(N) + O(1)
# = O(N) ignore constants
sol = Solution()
print(sol.maxSubArray(nums = [1, 4, 2, 10, 2, 3, 1, 0, -20]))