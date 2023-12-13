# 49. Group Anagrams
# solution: ASCII character of letters ord(l=i) - ord('a') = idx

from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0]*26

            for c in s:
                count[ord(c)-ord('a')] +=1
            res[tuple(count)].append(s)
        return res.values()

sol = Solution()
print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))