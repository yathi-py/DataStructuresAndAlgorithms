#15. 3Sum
#solution: two pointer
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() #O(NlogN)

        for i, a in enumerate(nums): #O(N)
            if i >0 and a == nums[i-1]: continue

            l,r = i+1, len(nums)-1

            while(l<r):      #O(N)
                tsum = a+nums[l]+nums[r]
                if tsum >0:
                    r-=1
                elif tsum <0:
                    l+=1
                else:
                    res.append([nums[i]]+[nums[l]]+[nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res

# time complexity
# O(NLogN) + O(N^2)

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))