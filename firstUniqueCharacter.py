class Solution:
    def firstUniqChar(self, s):
        #count of each letter
        letterCount = {}
        #unique letters
        uniqueLetters = {}

        #count the letters
        for letter in s:
            if letterCount.get(letter):
                letterCount[letter] += 1
            else:
                letterCount[letter] = 1

        #establish unique letters only
        for entry in letterCount.keys():
            if letterCount[entry] < 2:
                uniqueLetters[entry] = s.index(entry)

        if uniqueLetters == {}:
            return -1
        #return the first letter's index
        return list(uniqueLetters.values())[0]