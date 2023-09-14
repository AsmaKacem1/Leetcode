# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,output):
        if not root:
            return 
        self.inorder(root.left,output)
        output.append(root.val) 
        self.inorder(root.right,output)
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        output=[]
        output1=[]
        output2=[]
        self.inorder(root1,output1)
        self.inorder(root2,output2)
        i1,i2,N1,N2=0,0,len(output1),len(output2)
        while i1<N1 and i2<N2:
            if output1[i1]<output2[i2]:
                output.append(output1[i1])
                i1+=1
            else:
                output.append(output2[i2])
                i2+=1
        return output+output1[i1:]+output2[i2:]
        
    


    
