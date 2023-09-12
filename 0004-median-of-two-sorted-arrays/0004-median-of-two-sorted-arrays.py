class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i,j=0,0
        mergedarray=[]
        n,m=len(nums1),len(nums2)
        if n==0:
            return (nums2[m//2])/1 if m%2!=0 else (nums2[m//2]+nums2[(m//2)-1])/2
        if m==0:
            return (nums1[n//2])/1 if n%2!=0 else (nums1[n//2]+nums1[(n//2)-1])/2
        while i<n and j<m:
            if nums1[i]>nums2[j]:
                mergedarray.append(nums2[j])
                j+=1
            else:
                mergedarray.append(nums1[i])
                i+=1

            if i==len(nums1):
                mergedarray+=nums2[j:]
            if j==len(nums2):
                mergedarray+=nums1[i:]
        return (mergedarray[(n+m)//2])/1 if (n+m)%2!=0 else (mergedarray[(n+m)//2]+mergedarray[((n+m)//2)-1])/2
        