# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or head == None: return head
        
        tail = head
        
        nodeList = [tail]
        
        while tail.next != None:
            tail = tail.next
            nodeList.append(tail)
        
        rotation =  k % len(nodeList)
        
        if rotation == 0 or len(nodeList) == 1: return head
        
        tail.next = head
        
        nodeList[-rotation-1].next = None
        
        return nodeList[-rotation]