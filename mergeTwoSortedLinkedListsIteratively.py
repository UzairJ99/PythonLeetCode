# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ListNode(0)
        prev = temp
        
        while True:
            if l1 is None:
                prev.next = l2
                break
            if l2 is None:
                prev.next = l1
                break
                
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
                
            prev = prev.next
            
        return temp.next