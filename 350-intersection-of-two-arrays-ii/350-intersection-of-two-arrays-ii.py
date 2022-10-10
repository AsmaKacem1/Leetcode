class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        L=[]
        for i in range(len(nums2)):
            if nums2[i] in dic:
                dic[nums2[i]]+=1
            else:
                dic[nums2[i]]=1
        for i in range (len(nums1)):
            if nums1[i] in dic:
                L.append(nums1[i])
                dic[nums1[i]]=dic[nums1[i]]-1
                if (dic[nums1[i]]==0):
                    dic.pop(nums1[i])
      
        return L
        