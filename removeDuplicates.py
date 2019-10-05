class Solution:
    def removeDuplicates(self, S):
        #stack
        nonDoubles = []
        for letter in range(len(S)):
            #push to stack
            nonDoubles.append(S[letter])
            if len(nonDoubles) > 1:
                #check if top of stack matches the previous top of the stack
                if(nonDoubles[len(nonDoubles) - 1] == nonDoubles[len(nonDoubles) - 2]):
                    #remove the duplicates
                    nonDoubles.pop()
                    nonDoubles.pop()
        #convert stack to list
        nonDoubles = ''.join(nonDoubles)
        return nonDoubles