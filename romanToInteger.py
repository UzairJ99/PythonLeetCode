class Solution:
    def romanToInt(self, s):
        sum = 0
        #pointer to previous character
        prev = -1
        
        translator = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        #start with last character so pointer isn't aligned with current character
        if len(s) > 0:
            sum += translator[s[-1]]

        #loop backwards through string starting at the second last character
        for char in range(len(s)-2,-1,-1):
            if s[char] == 'I' and (s[prev] == 'V' or s[prev] == 'X'):
                sum -= 1
            elif s[char] == 'X' and (s[prev] == 'L' or s[prev] == 'C'):
                sum -= 10
            elif s[char] == 'C' and (s[prev] == 'D' or s[prev] == 'M'):
                sum -= 100
            else:
                sum += translator[s[char]]
            prev -= 1

        return sum