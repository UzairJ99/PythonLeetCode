class Solution:
    def isAnagram(self, s, t):
        #convert string to a count of characters
        S = {}
        for char in s:
            if S.get(char):
                S[char] += 1
            else:
                S[char] = 1

        #reduce the count from the string dictionary at every letter
        for char in t:
            if S.get(char):
                S[char] -= 1
                #remove the character from the dictionary once the count is 0
                if S[char] == 0:
                    del S[char]
            #if the character isn't in the dictionary, t cannot be an anagram of s
            else:
                return False
        
        #if it's an anagram the dictionary should be empty now
        if S == {}:
            return True
        else:
            return False