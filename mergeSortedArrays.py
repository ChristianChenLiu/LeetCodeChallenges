class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        x=m-1
        y=n-1
        i=m+n-1
        while y>=0:
            if x>=0 and nums1[x]>nums2[y]:
                nums1[i]=nums1[x]
                i=i-1
                x=x-1
            else:
                nums1[i]=nums2[y]
                i=i-1
                y=y-1