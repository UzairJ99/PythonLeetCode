class Solution:
    def titleToNumber(self, s):
        #ord('A') - 64 gives the value of the letter in the alphabet
        decVal = 0
        radix = 0
        
        #convert the alphabet (26) base number into decimal base
        for character in range(len(s)-1,-1,-1):
            decVal += (ord(s[character])-64)*26**(radix)
            radix += 1
        
        return decVal