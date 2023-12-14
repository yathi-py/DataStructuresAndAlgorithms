# 5. Longest Palindromic Substring
# Solution: Three pointers

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            l=i
            r=i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if len(s[l:r+1])>len(res):
                    res = s[l:r+1]
                l-=1
                r+=1
            l,r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r+1])>len(res):
                    res = s[l:r + 1]
                l -= 1
                r += 1
        return res
sol = Solution()
print(sol.longestPalindrome(s = "babad"))
