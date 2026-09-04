class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Have two pointer from 0, and 1
        #   if left is bigger than right, then just replace left and move forward, want to buy from the smaller day
        left, right = 0, 1
        maxProfit = 0

        while right < len(prices):
            if prices[left] >= prices[right]:
                left = right
                right += 1
            else:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
                right += 1
        return maxProfit

# Time: O(n)    -    n = size of the input array
# Space: O(1)   -   didn't use extra space, only need two pointer
