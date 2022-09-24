class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        l = intervals
        l.sort()
        ans = [l[0]]
        curr=0
        for i in range(1,len(l)):
            i1,i2 = l[i][0],l[i][1]
            a1,a2 = ans[-1][0],ans[-1][1]
            if a2>=i1:
                if i2>a2:
                    ans[-1][1]=i2
            else:
                ans.append(l[i])
        return ans