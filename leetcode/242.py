# 242. Valid Anagram


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0)+1
            count[t[i]] = count.get(t[i],0)-1

        if max(count.values()) == 0 and min(count.values()) == 0:
            return True
        else:
            return False


sol = Solution()
print(sol.isAnagram(s = "anagram", t = "nagara"))