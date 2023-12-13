# 424. Longest Repeating Character Replacement
# Solution: sliding window + hashing

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxi = 0
        l=0
        count ={}
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)

            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -=1
                l+=1
            maxi = max(maxi,r-l+1)

        return maxi

sol = Solution()
print(sol.characterReplacement(s = "ABBB", k = 1))