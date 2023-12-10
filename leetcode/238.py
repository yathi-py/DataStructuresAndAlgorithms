# 238. Product of Array Except Self

# Solution: Prefix-Postfix product technique
# https://leetcode.com/problems/product-of-array-except-self/solutions/3938575/video-visualization-and-explanation-of-o-n-solution/

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]* len(nums)
        prefix = 1
        for i in range(0, len(nums)):
            ans[i] = prefix
            prefix = prefix*nums[i]

        postfix = 1

        for i in range(len(nums)-1 ,-1, -1):
            ans[i] = ans[i]* postfix
            postfix = postfix * nums[i]

        return ans


sol = Solution()
print(sol.productExceptSelf( nums = [2,2,3,4]))
# O(N)