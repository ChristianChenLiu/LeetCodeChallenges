# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = ""
        while (head != None):
            s += str(head.val)
            head = head.next
        return palindromeChecker(s)
    
def palindromeChecker(string):
    
    if len(string) <= 1: return True

    for i in range(len(string)//2):
        if string[i] != string[-i - 1]:
            return False

    return True
        
        
        