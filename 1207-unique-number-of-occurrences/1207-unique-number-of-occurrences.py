class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic={}
        L=[]
        res=set()
        for i in arr:
            if (i in dic):
                dic[i]+=1
            else:
                dic[i]=1
        L=list(dic.values())
        res=set(L)
        return len(res)==len(L)
            