#121. Best Time to Buy and Sell Stock


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_value = prices[0] #O(1)

        for i in range(1,len(prices)): # O(N-1)
            profit = max(profit, prices[i]-min_value) #O(1)
            min_value = min(min_value,prices[i])
        return profit

sol = Solution()
print(sol.maxProfit(prices = [7,1,5,3,8]))

# time complexity = O(1)+O(N-1)+O(1) ignore constants
# O(N)
