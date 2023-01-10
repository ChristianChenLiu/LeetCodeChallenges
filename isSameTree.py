# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # DFS through both trees
        def dfs(node1, node2):

            # If there is no node1 and there is no node2, return True
            if not node1 and not node2:
                return True

            # If there is no node1 or there is no node2 or node1!=node2, return False
            if not node1 or not node2 or node1.val != node2.val:
                return False

            # Else, check both child of node1 and node2
            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)

        return dfs(p, q) #Done