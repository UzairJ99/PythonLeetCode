class MyQueue:

    def __init__(self):
        self.items = []
        
    def push(self, x):
        self.items.append(x)  

    def pop(self):
        #check if not empty
        if not self.empty():
            #get the element that was first pushed
            element = self.items[0]
            #remove the first element from the queue
            self.items = self.items[1:]
            return element
        else:
            return None
        
    def peek(self):
        if not self.empty():
            #get the element that was first pushed
            element = self.items[0]
            return element
        else:
            return None      

    def empty(self):
        #check size of queue
        return len(self.items) < 1