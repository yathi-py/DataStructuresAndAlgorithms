# 153. Find Minimum in Rotated Sorted Array
# Solution : Binary search

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0, len(nums)-1
        while l<=r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])

            mid = (l+r) // 2
            res = min(nums[mid], res)

            if nums[mid]>= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return res

# timecomplexity
# O(logn)

sol = Solution()

print(sol.findMin([3,4,5,1,2]))