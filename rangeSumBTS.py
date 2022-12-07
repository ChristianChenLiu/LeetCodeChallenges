# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        return root and root.val * (L <= root.val <= R) + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R) or 0