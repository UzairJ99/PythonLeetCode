class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        index = 0
        #if (head is None or head.next is None):
        while head and head.val == val:
            head = head.next
            
        if head is None:
            return head
        
        if head.next is None and head.val == val:
            return head
        
        pointer = head
        
        while pointer.next is not None:   
            if pointer.next.val == val:
                pointer.next = pointer.next.next
                
            else:
                pointer = pointer.next
                
        
        return head