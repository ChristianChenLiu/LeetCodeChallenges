# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recursive(self,root,Sum,targetSum):
        
        if root!=None and root.left==None and root.right==None:
            
            if Sum+root.val == targetSum:
                return True
            return False
        
        if root!=None:
            return self.recursive(root.left,Sum+root.val,targetSum) or self.recursive(root.right,Sum+root.val,targetSum)
        
        return False
    
    def hasPathSum(self, root, targetSum):
        
        return self.recursive(root,0,taum)