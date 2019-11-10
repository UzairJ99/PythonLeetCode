class Solution:
    def isPalindrome(self, head):
        elements = []
        pointer = head
        #push each element into list
        while (pointer):
            elements.append(pointer.val)
            pointer = pointer.next
        
        #check if list is equal to it's reverse
        return elements == elements[::-1]