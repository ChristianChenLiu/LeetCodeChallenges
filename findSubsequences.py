class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def dfs(index,running):

            if len(running) >= 2:
                res.append(running)
                
            
            dup_bag = set()
            for i in range(index+1,len(nums)):
                
                if nums[i] >= nums[index] and nums[i] not in dup_bag:    
                    dfs(i,running+[nums[i]])
                    
                dup_bag.add(nums[i])
                
            return 
        
        ib = set()
        for k in range(len(nums)):
            if nums[k] not in ib:
                dfs(k,[nums[k]])
            ib.add(nums[k])
            
        return res 