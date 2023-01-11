class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Construct the tree using the edges.
        # Since the tree is undricted, we need to add both directions in the tree.
        tree = defaultdict(list)
        for s,e in edges:
            tree[s].append(e)
            tree[e].append(s)
        
        # node is the current node we are examing.
        # par is the node's direct parent node.
        def dfs(node,par):
            res = 0
            # Since it is a tree, there will be no cycles.
            # However, the tree is undirected, which means one of the neighbor node is its parent node.
            for nei in tree[node]:
                # Make sure we are not going backward to its parent node.
                if nei != par:
                    res += dfs(nei,node)
            
            # case1, res != 0, this means we have found some apples down the tree
            # case2, hasApple[node]==True, this means the current node has a apple on it
            # In both cases, we will have to increase the result by 2.
            # Adding 2 because we need 1 to get to this node and 1 going back
            if res or hasApple[node]:
                return res + 2
            
            # There is no apple on this node or down the tree, res should 0.
            # In this case we don't want to come to this node at all, so return 0.
            return res
        
        # Following the dfs, you can see that when we coming back to node 0, if there are some apples in the tree,
        # We added an extra 2 to the result, so we need to -2 here.
        # In case there is no apples in this tree, dfs will return 0, but we can't return -2, so just return 0
        return max(dfs(0,-1)-2, 0)