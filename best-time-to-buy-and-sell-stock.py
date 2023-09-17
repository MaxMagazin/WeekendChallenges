# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice = prices[0]
        maxPrice = prices[0]
        minPriceCandidate = prices[0]
        maxDiff = maxPrice - minPrice

        for x in prices[1:]:
            if x - minPriceCandidate > maxDiff:
                minPrice = minPriceCandidate

            if (diff := (x - minPrice)) > maxDiff:
                maxDiff = diff
                maxPrice = x

            elif x < minPriceCandidate:
                minPriceCandidate = x
        
        return maxDiff


s = Solution()
#print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,12,3,99]))



    

            
