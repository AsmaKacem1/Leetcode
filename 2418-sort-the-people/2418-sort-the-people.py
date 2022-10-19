class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        new_list=list(zip(heights,names))
        new_list=sorted(new_list,reverse=True)
        res=[]
        for i in range(len(heights)):
            res.append(new_list[i][1])
            
        return res
        