class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        

    def push(self, x):
        self.stack.append(x)
        #set new min element
        if len(self.min) < 1 or x <= self.min[-1]:
            self.min.append(x)

    def pop(self):
        #check if minimum value is being popped
        if self.stack[-1] == self.min[-1]:
            #remove from minimum stack as well
            self.min.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min[-1]