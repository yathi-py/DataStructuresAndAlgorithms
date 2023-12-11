# 11. Container With Most Water
# Solution : Two pointer
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        l,r = 0, len(height)-1
        while l<=r:
            if height[r]>=height[l]:
                maxi = max(maxi, height[l] * (r-l))
                l+=1
            else:
                maxi = max(maxi, height[r] * (r-l))
                r-=1
        return maxi

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))