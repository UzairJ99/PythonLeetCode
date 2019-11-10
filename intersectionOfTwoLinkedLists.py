class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        lengthA = self.getLength(headA)
        lengthB = self.getLength(headB)
        
        #pointer1 will refer to the longer list
        if lengthA > lengthB:
            pointer1 = headA
            pointer2 = headB
        else:
            pointer1 = headB
            pointer2 = headA

        #determine how many initial nodes to skip for the longer list
        #this will align the lists so the intersecting node is reached by both lists at the same iteration
        startingNode = abs(lengthA - lengthB)

        #skip to startingNode for the longer list so we have an equal count of iterations
        for skips in range(startingNode):
            pointer1 = pointer1.next

        while (pointer1):
            #check if the pointers reference the same node in memory
            if pointer1 == pointer2:
                return pointer1
            #continue iteration
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        #in the case there are no intersections
        return None
        
    #get the length of the list
    def getLength(self, head):
        count = 0
        pointer = head
        while(pointer):
            count += 1
            pointer = pointer.next
        
        return count