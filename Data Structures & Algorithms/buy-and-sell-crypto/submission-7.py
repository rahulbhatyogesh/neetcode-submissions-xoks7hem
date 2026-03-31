class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        diff = 0
        while (j<len(prices)):
            if (prices[j] > prices[i]):
                if (prices[j]-prices[i])>diff:
                    diff = prices[j] - prices[i]
                j+=1
                continue
            if (prices[j] == prices[i]):
                j+=1
                continue
            if (prices[j] < prices[i]):
                i = j
                j+=1
        
        return diff