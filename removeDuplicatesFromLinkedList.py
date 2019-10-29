class Solution:
    def deleteDuplicates(self, head):
        pointer = head
        #check if list exists
        if head:
            #this pointer keeps track of the next elements value
            check = head.next
            while(check):
                #iterate the next pointer until there is no longer a match
                if pointer.val == check.val:
                    check = check.next
                else:
                    #increment main pointer
                    pointer.next.val = check.val
                    pointer = pointer.next
            #we now reach the end of the list so we deallocate the rest of the list because all unique values end at pointer
            pointer.next = None
        return head