class Solution:
    def minAddToMakeValid(self, S):
        stack = []
        
        for bracket in S:
            #guard for empty stack
            if len(stack)>0:
                #check if bracket can be closed
                if stack[len(stack)-1] == '(' and bracket == ')':
                    stack.pop()
                else:
                    stack.append(bracket)
            else:
                stack.append(bracket)

        #the length of the stack is the minimum number of brackets required to balance
        return len(stack)