class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ""
        
        if len(strs) == 0:
            return ""
        
        if len(strs) < 2:
            return strs[0]

        #set prefix to first word
        prefix = strs[0]

        for word in range(1, len(strs)):
            #pointer to first character of both prefix and word
            p1 = 0
            while p1 < len(strs[word]) and p1 < len(prefix):
                #loop through word and stored prefix simultaneously
                if strs[word][p1] == prefix[p1]:
                    p1 += 1
                else:
                    #reset prefix upto this character
                    prefix = prefix[:p1]
            #reset prefix upto the character of p1 in the shorter word
            prefix = prefix[:p1]
        
        return prefix