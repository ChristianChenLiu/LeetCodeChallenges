
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        levelnode=defaultdict(list)
        def bfs(node,level):
            if not node:
                return
            
            levelnode[level].append(node.val)
            bfs(node.left,level+1)
            bfs(node.right,level+1)
        bfs(root,0)
        average=[]
        for i in levelnode.values():
            average.append(float(sum(i))/len(i))
        return average   