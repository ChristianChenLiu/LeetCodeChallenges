# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        
        safe = head
        unique = head.val
        
        while head.next != None:
            if head.next.val > unique:
                head = head.next
                unique = head.val
            else:
                head.next = head.next.next
        
        return safe
        