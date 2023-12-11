# 33. Search in Rotated Sorted Array
# Solution binary search

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = nums[0]
        l,r =0, len(nums)-1

        while l<=r:
            if res == target:
                return 0
            m = (l+r)//2
            if nums[m] == target:
                res = m
                return res

            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l=m+1
                else:
                    r=m-1
            else:
                if target < nums[m] or target > nums[r]:
                    r=m-1
                else:
                    l=m+1
        return -1

sol = Solution()
print(sol.search(  [4,5,6,7,0,1,2], target = 0))

# time complexity
# O(logN)