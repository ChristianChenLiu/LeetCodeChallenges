class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 != None and list2 != None:
            if list1.val <= list2.val:
                head = ListNode(list1.val)
                list1 = list1.next
            else: 
                head = ListNode(list2.val)
                list2 = list2.next
        elif list1 != None:
            head = ListNode(list1.val)
            list1 = list1.next
        elif list2 != None:
            head = ListNode(list2.val)
            list2 = list2.next
        else:
            head = None
        
        current_node = head
        
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                current_node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                current_node.next = ListNode(list2.val)
                list2 = list2.next
            current_node = current_node.next
        
        while list1 != None:
            current_node.next = ListNode(list1.val)
            list1 = list1.next
            current_node = current_node.next
        
        while list2 != None:
            current_node.next = ListNode(list2.val)
            list2 = list2.next
            current_node = current_node.next
            
        return head