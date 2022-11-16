class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dic={'type':1,'color':2,'name':3}
        res=0
        for i in range(len(items)):
            if items[i][dic[ruleKey]-1]==ruleValue:
                res+=1
        return res
        