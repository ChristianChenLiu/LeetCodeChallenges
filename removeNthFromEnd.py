# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        point = head
        count = 1
        array = [point]
        
        while point.next != None:
            count += 1
            point = point.next
            array.append(point)
        
        if count == 1:
            return None
            
        if count == n:
            return array[1]
        
        if -n != -1:
            array[-n - 1].next = array[-n + 1]
        else:
            array[-n - 1].next = None
        
        return head