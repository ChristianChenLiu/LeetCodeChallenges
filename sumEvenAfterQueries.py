class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        current_sum = 0
        res = []
        
        #Summing all the even numbers in num
        for num in nums:
            if num % 2 == 0:
                current_sum += num
        
        for query in queries:
            val, index = query
            
            #changing the sum of even numbers only if nums[index] and val are
            #even + even = even or odd + odd = even, we increase the sum with val or nums[index] + val
            #even + odd = odd, we decrease the sum with nums[index] no longer even
            if nums[index] % 2 == 0 and val % 2 == 0:
                current_sum += val
            elif nums[index] % 2 == 1 and val % 2 == 1:
                current_sum += nums[index] + val
            elif nums[index] % 2 == 0:
                current_sum -= nums[index]
            
            #appending the updated sum
            res.append(current_sum)
            #updating the nums[index] with val as required per query
            nums[index] += val
        
        return res     