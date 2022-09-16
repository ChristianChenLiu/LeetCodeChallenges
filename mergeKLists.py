# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        N = len(lists)
        minHeap = []
        for i in range(N):
            if lists[i] is not None:
                heapq.heappush(minHeap, (lists[i].val, i))
                
        sentinel = ListNode(-1)
        curr = sentinel
        while len(minHeap):
            val, i = heapq.heappop(minHeap)
            
            curr.next = lists[i]
            curr = curr.next
            lists[i] = lists[i].next
            curr.next = None
            if lists[i] is not None:
                heapq.heappush(minHeap, (lists[i].val, i))
        
        return sentinel.next
                