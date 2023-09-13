# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def traverse(self,root,dic):
        if not root:
            return
        dic[root.val]+=1
        self.traverse(root.left,dic)
        self.traverse(root.right,dic)
    

        
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic=defaultdict(int)
        self.traverse(root,dic)
        val,result=0,[]
        for key in dic:
            if val<dic[key] :
                val=dic[key]
                result=[key]
            elif val==dic[key] :
                result.append(key)
        return result



        