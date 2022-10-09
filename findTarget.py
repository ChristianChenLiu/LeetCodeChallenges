# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        ans=[]
        def helper(node):
            if not node :return
            else:
                helper(node.left)
                ans.append(node.val)
                helper(node.right)
        helper(root)
        l,r=0,len(ans)-1
        while l<r:
            tot=ans[l]+ans[r]
            if tot>k: r-=1
            elif tot<k: l+=1
            else: return True
        return False