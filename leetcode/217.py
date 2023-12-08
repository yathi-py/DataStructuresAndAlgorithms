# 217. Contains Duplicate
from typing import List

class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        # sets use hashing for lookups which makes them faster . NOTE: dont use lists for duplicates
        hashset = set(nums) #O(N)
        if len(hashset) <len(nums): #O(1)
            return True
        return False


sol = Solution()
print(sol.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))
# time complexity = O(N)+O(1)
# = O(N)
