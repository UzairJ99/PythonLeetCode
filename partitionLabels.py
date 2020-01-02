class Solution:
    def partitionLabels(self, S):
        #create dictionary of character: last index
        lastIndex = {character: ix for ix, character in enumerate(S)}
        
        endpoint, anchor = 0, 0
        result = []
        
        for i, c in enumerate(S):
            #set endpoint to be the last index of the current letter at position i
            endpoint = max(endpoint, lastIndex[c])
            #if the last letter is met, append this partition to the answer
            if i == endpoint:
                #get size of partition + 1 because of zero indexing
                result.append(i - anchor + 1)
                #set the beginning of the next partition to the next character
                anchor = i + 1
        
        return result