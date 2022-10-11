class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
#         combs=[]
#         def _combine(arr,num):
#             if len(arr)==k:
#                 combs.append(arr)
#             for i in range(num,n+1):
#                 _combine(arr+[i],i+1)
                
#         _combine([],1)
#         return combs
        return combinations(range(1, n+1), k)