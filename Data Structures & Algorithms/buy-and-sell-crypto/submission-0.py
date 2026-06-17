class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointer for sliding window
        left, right = 0, 1
        maxProfit = 0

        #go until window at the end of the input array
        while right < len(prices):
            #if the day after is less than before change the buying day
            if prices[left] > prices[right]:
                left = right
            
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
            right += 1
        return maxProfit