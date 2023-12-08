# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/solutions/3938575/video-visualization-and-explanation-of-o-n-solution/

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      ans = [1]* len(nums)
      for i in range(1,len(nums)):
          ans[i] = nums[i-1] * ans[i-1]

      right = nums[-1]

      for i in range(len(nums)-2, -1, -1):
          ans[i]= ans[i]*right
          right = right*nums[i]
      return ans

sol = Solution()
print(sol.productExceptSelf( nums = [1,2,3,4]))
# O(N)