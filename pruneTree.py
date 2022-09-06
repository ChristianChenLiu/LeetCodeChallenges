# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def traverse(node):
            
            if not node:
                return 0
            else:
                left_max = traverse(node.left)
                right_max = traverse(node.right)
                
                if not left_max:
                    node.left = None
                if not right_max:
                    node.right = None
                
                return max(node.val, left_max, right_max)
        
        max_node = traverse(root)
        
        if not max_node:
            return None
        else:
            return root