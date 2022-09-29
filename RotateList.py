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
        #if we not need to rotate or linked list is empty, we just return head
        if k == 0 or head == None: return head
        
        #we try to get the tail (last node in the linked list)
        #and append all the nodes in the linked list to nodeList on the way
        tail = head
        nodeList = [tail]
        while tail.next != None:
            tail = tail.next
            nodeList.append(tail)
        
        #we calculate the actual rotation required
        rotation =  k % len(nodeList)
        
        #if rotation is actually 0 or linked list only have a single node,
        #we just return the head
        if rotation == 0 or len(nodeList) == 1: return head
        
        #Otherwise, we link the tail to the head
        #then we get the new tail to point to None
        #and return the node that was pointed to before from our new tail
        tail.next = head
        nodeList[-rotation-1].next = None
        
        return nodeList[-rotation]