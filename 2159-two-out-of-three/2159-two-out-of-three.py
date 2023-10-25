class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1=set()
        set2=set()
        result_set=set()
        for i in nums1:
            set1.add(i)
        for j in nums2:
            if j in set1:
                result_set.add(j)
            set2.add(j)
        for k in nums3:
            if (k in set1 or k in set2 ):
                result_set.add(k)

        return list(result_set)
        