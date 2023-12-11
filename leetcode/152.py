# 152. Maximum Product Subarray

# solution : prefix suffix product

from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre, suf =1,1
        max_pro = max(nums)
        n = len(nums)
        for i in  range(n):
            if pre == 0: pre = 1
            if suf == 0: suf = 1

            pre *= nums[i]
            suf *= nums[n-i-1]
            max_pro = max(max_pro, max(pre, suf))

        return max_pro

# O(N) time
#O(1) space



sol = Solution()
print(sol.maxProduct(([2,-5,-2,-4,3])))