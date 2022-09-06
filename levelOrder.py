"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        # the total number of nodes is between [0, 10 ^ 4]
        # check if root is None to cover 0 node case
        if not root: return []
        # init ans
        ans = []
        # standard bfs approach
        # start with the root node
        q = deque([root])
        # do the following logic when the queue is not empty
        while q:
            # level is used to store all the node values at the current level
            level = []
            # for each element in the current queue
            for _ in range(len(q)):
                # get the first node from the queue and pop it
                node = q.popleft()
                # add it to level
                level += [node.val]
                # this node may include other nodes, we add them all to the queue
                for n in node.children: q.append(n)
            # we've processed this level, add it to ans
            ans += [level]
        # return final ans
        return ans