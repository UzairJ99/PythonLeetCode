# class ListNode:
def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
    def getDecimalValue(self, head):
        # get list of values from linkedlist
        binaryList = []
        
        node = head
        while node:
            binaryList.append(node.val)
            node = node.next
        
        # convert binary valued list to decimal value
        decimalVal = 0
        binaryList = binaryList[::-1]  # reverse values to get correct powers
        for power, val in enumerate(binaryList):
            decimalVal += val * (2 ** power)
        
        return decimalVal