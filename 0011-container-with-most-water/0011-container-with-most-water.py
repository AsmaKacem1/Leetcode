class Solution:
    def maxArea(self, height: List[int]) -> int:
        result,l,r=0,0,len(height)-1
        while l<r:
            min_height=min(height[r],height[l])
            result=max(result,min_height*(r-l))
            if height[r]== min_height:
                r-=1
            elif height[l]== min_height:
                l+=1
        return result