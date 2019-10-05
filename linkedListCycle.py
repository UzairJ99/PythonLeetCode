class Solution:
    def hasCycle(self, head):
        pointer = head
        #hashtable to check occurances
        nodeMap = {}
        while (pointer):
            #if the node is in the hashtable, that means there was a cycle
            if nodeMap.get(pointer):
                return True
            else:
                #add to hashtable
                nodeMap[pointer] = 1
            #iterate
            pointer = pointer.next
        return False