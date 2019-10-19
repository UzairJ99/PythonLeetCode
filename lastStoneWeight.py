#import MaxHeap class from maxHeap file
from .maxHeap import MaxHeap

class Solution:
    def lastStoneWeight(self, stones):
        stoneHeap = MaxHeap(stones)
        print(stoneHeap.heap)
        while len(stoneHeap.heap) > 2:
            y = stoneHeap.pop() #largest stone
            x = stoneHeap.pop() #second largest
            
            if x==y:
                continue
            else:
                #smash
                y = y-x
                #reassign the stone into the heap
                stoneHeap.push(y)
        
        #check if the stones are all destroyed
        if len(stoneHeap.heap) == 1:
            return 0
        else:
            return stoneHeap.peek()