class Solution:
    def backspaceCompare(self, S, T):
        s_stack = []
        t_stack = []
        
        for char in S:
            if char != "#":
                s_stack.append(char)
            else:
                if len(s_stack) > 0:
                    #erase previous character
                    s_stack.pop()
                else:
                    continue
        
        for char in T:
            if char != "#":
                t_stack.append(char)
            else:
                if len(t_stack) > 0:
                    t_stack.pop()
                else:
                    continue
        
        #if both stacks are equal, they both become the same after being typed
        return s_stack == t_stack