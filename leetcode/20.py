# 20. Valid Parentheses
# solution : stack + hashmap

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open ={
            ']':'[', '}':'{', ')':'('
        }

        for c in s:
            if c not in close_to_open:
                stack.append(c)
            else:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False


sol = Solution()
print(sol.isValid(s = "()[]{}"))
