# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        def check(node , node1):
            if node==None and node1 == None:
                return True 
            if node ==None or node1 == None:
                return False
            if node.val != node1.val:
                return False
            
            return check(node.left , node1.right) and check(node.right , node1.left)
            
        return check(root.left , root.right)