# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        #function to get the length of the list
        def getLength(head):
            pointer = head
            #count number of nodes
            while pointer:
                pointer = pointer.next
                self.len += 1
            return self.len
        
        self.len = 0
        #get the middle of the list
        length = getLength(head)
        middle = (length//2)
        
        pointer = head
        #iterate until the middle
        for x in range(middle):
            pointer = pointer.next
        return pointer