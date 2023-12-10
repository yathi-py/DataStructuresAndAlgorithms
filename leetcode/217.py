# 217. Contains Duplicate
from typing import List
# Solution : Hashing
# NOTE: dont use lists for lookups
class Solution:

    def contains_duplicate_hashing(self, nums: List[int]) -> bool:
        count_dict = {}

        for idx,val in enumerate(nums):
            if val in count_dict:
                return True
            count_dict[val] = idx
        return False

    def contains_duplicate_using_sets(self, nums: List[int]) -> bool:
        # sets use hashing for lookups which makes them faster . NOTE: dont use lists for duplicates
        hashset = set(nums) #O(N)
        if len(hashset) <len(nums): #O(1)
            return True
        return False


sol = Solution()
print(sol.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))
# time complexity = O(N)+O(1)
# = O(N)
