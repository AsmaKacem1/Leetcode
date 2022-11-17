class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sale=prices[0]
        buy=prices[0]
        res=0
        for i in range(1,len(prices)):
            if buy>prices[i]:
                buy=prices[i]
            else: 
                res=max(res,prices[i]-buy)
            sale=prices[i]
        return res
    
    
   
            
            
            
            
            
           
                