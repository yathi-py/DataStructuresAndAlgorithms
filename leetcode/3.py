# 3. Longest Substring Without Repeating Characters
#Solution: Two pointer
class Solution:

    def twopointer(self, s: str) -> int:
        maxi=0
        l=0
        dic = {}
        for r in range(len(s)):
            char= s[r]
            if char in dic and dic[char]>=1:
                l = dic[char] + 1
            else:
                maxi = max(maxi, r - l + 1)

            dic[char] = r
        return maxi

    def two_pointer_with_set(self, s: str) -> int:
        maxi = 0
        l = 0
        r = 0
        a = set()
        if len(s) == 0 or len(s) == 1:
            return len(s)
        while r < len(s):
            if s[r] in a:
                maxi = max(maxi, len(a))
                l += 1
                r = l
                a.clear()
            else:
                a.add(s[r])
                r = r + 1
        return max(maxi, len(a))

    # bruteforce
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            temp = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in temp:
                    temp+=s[j]
                else:
                    break
            max_len = max(max_len,len(temp))

        return max_len


sol = Solution()
print(sol.twopointer(s = "tmmzuxt"))