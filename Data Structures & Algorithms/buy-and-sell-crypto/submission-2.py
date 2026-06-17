class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        lmin = prices[0]
        rmax = prices[0]
        res = 0

        for i in range(1, len(prices)):
            if prices[i] > rmax:
                rmax = prices[i]
            if prices[i] <= lmin:
                lmin = prices[i]
                rmax = prices[i]
            if rmax - lmin > res:
                res = rmax - lmin
            
        
        return res