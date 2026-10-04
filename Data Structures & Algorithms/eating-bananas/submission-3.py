class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k -> Speed of which Koko can eat which range from [1...max(piles)]
        # do binary serach on this speed

        l, r = 1, max(piles)
        res = r

        while l <= r:
            # Find mid
            k = (l + r) // 2

            # Do something with mid
            hour = 0
            for pile in piles:
                hour += math.ceil(pile / k)
            
            # Update l and r, and res
            if hour <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res
