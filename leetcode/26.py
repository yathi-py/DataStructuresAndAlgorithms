# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# two pointer
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = l+1
        count = 1
        while r < len(nums):
            if nums[l] == nums[r]:
                r+=1
            else:
                count +=1
                nums[l+1] = nums[r]
                l+=1
                r+=1
        return nums, count


sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))