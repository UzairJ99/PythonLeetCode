class MaxHeap:
    def __init__(self, items=[]):
        #we don't use the first index because of left/right child index calculations
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.floatUp(len(self.heap)-1)

    #insert into heap
    def push(self, data):
        #add to list
        self.heap.append(data)
        #move up the heap
        self.floatUp(len(self.heap)-1)

    #check the max element
    def peek(self):
        #check if top of heap exists
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
    
    #remove the max element
    def pop(self):
        if len(self.heap) > 2:
            #swap largest and smallest element
            self.swap(1, len(self.heap)-1)
            #returns last element in list aka largest value
            max = self.heap.pop()
            #move the element back into place
            self.bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    #swap index values
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    #shift an element up the heap
    def floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            #swap
            self.swap(index, parent)
            #repeat float up until the element is at it's appropriate location
            self.floatUp(parent) #parent is the new index

    #shift an element down the heap
    def bubbleDown(self, index):
        leftChild = index*2
        rightChild = index*2+1
        largest = index
        #determine which child to swap with
        if len(self.heap) > rightChild:
            #if the current element is larger than both the children we don't need to bubble down
            if self.heap[index] > self.heap[leftChild] and self.heap[index] > self.heap[rightChild]:
                return
            elif self.heap[leftChild] > self.heap[rightChild]:
                largestChild = leftChild
                print("largest child:" , self.heap[largestChild])
            else:
                largestChild = rightChild
                print("largest child:" , self.heap[largestChild])
        #needed in the case where there is only one child (must be left child)
        elif len(self.heap) == rightChild:
            if self.heap[index] > self.heap[leftChild]:
                return
            else:
                largestChild = leftChild
        else:
            return

        #swap values
        self.swap(largest, largestChild)
        #bubbleDown the new largestChild value
        self.bubbleDown(largestChild)
