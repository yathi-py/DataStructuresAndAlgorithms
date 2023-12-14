# 125. Valid Palindrome
# Solution Two pointers with ASCII

class Solution:

    def is_palindrome_without_builtin(self, s: str) -> bool:
        l,r=0,len(s)-1

        while l<=r:
            if not self.is_alphanum(s[l]):
                l+=1
                continue
            if not self.is_alphanum(s[r]):
                r-=1
                continue
            if s[l].lower() != s[r].lower:
                return False
            l+=1
            r-=1
        return True


    def is_alphanum(self,c):
        return (ord('A')<=ord(c)<=ord('Z')or
                ord('a')<=ord(c)<=ord('z')or
                ord('0')<=ord(c)<=ord('9'))

    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<=r:
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1

        return True

sol = Solution()
print(sol.is_palindrome_without_builtin(s = ""))