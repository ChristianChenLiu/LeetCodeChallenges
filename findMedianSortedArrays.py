class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        target_index = (len(nums1) + len(nums2))//2
        
        size_1 = len(nums1)
        size_2 = len(nums2)

        result = []
        i, j = 0, 0

        while i < size_1 and j < size_2:
            if nums1[i] < nums2[j]:
              result.append(nums1[i])
              i += 1

            else:
              result.append(nums2[j])
              j += 1
                
            if i + j > target_index:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return result[target_index]
                else: 
                    return (result[target_index - 1]+result[target_index])/2

        result = result + nums1[i:] + nums2[j:]
        
        if (len(nums1) + len(nums2)) % 2 == 1:
            return float(result[target_index])
        else: 
            return (result[target_index - 1]+result[target_index])/2