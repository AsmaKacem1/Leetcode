class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sale=prices[0]
        buy=prices[0]
        res=0
        for i in range(1,len(prices)):
            if buy>prices[i]:
                buy=prices[i]
            sale=prices[i]
            res=max(res,sale-buy)
        return res
    
    
   
            
            
            
            
            
           
                