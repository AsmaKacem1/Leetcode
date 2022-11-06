class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        nums3=[]
        for i in nums1:
            if i not in dic:
                dic[i]=1
        for i in nums2:
            if i in dic:
                nums3.append(i)
                dic.pop(i)
        return nums3
        