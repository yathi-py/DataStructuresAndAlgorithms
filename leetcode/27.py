# 27. Remove Element
# https://leetcode.com/problems/remove-element/description/
from typing import List


# two pointers


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1
        count = 1

        while l < r:
            if nums[l] != val:
                l += 1
                count += 1
            else:
                if nums[r] == val:
                    r -= 1
                else:
                    nums[l] = nums[r]
                    l += 1
                    count += 1
                    r -= 1
        return count


sol = Solution()
print(sol.removeElement(nums = [3,2,2,3], val = 3))
