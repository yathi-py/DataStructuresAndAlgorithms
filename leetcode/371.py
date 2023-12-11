# 371. Sum of Two Integers

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while b!=0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <=MAX else ~(a^mask)

sol = Solution()
print(sol.getSum(a = 1, b = 2))