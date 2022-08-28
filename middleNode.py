# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current_mid = head
        count = 1
        
        while (head != None):
            if count % 2 == 0:
                current_mid = current_mid.next
            head = head.next
            count += 1
        
        return current_mid