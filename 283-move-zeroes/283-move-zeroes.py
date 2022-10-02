class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums1=[0] * len(nums)
        j=0
        for i in range(len(nums)):
            if nums[i]!=0 :
                nums1[j]=nums[i]
                j=j+1
        for i in range(len(nums)):
              if nums1[i]!=0:
                    nums[i]=nums1[i]
              else:
                    nums[i]=0
                    
        return nums
            