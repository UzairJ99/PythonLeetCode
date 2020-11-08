class Solution:
    def countAndSay(self, n: int) -> str:
        # base case
        if (n == 1):
            return '1'
        else:
            # recursive call
            return self.say(n)
        
    # dependent function
    def say(self, n):
        # get the returned string value from the previous call
        numStr = self.countAndSay(n-1)
        # get the say version of the string
        sayVal = self.compressString(numStr)

        return sayVal
    
    # dependent function to compress the string into it's SAY format
    def compressString(self, strVal):
        outputStr = ''
        
        # split string into individual characters
        numStr = list(strVal)
        
        # compress the string
        count = 1
        prevLetter = numStr[0]
        if (len(numStr)>1):
            for letter in numStr[1:]:
                if (letter == prevLetter):
                    count += 1
                else:
                    outputStr += str(count)
                    outputStr += prevLetter
                    prevLetter = letter
                    count = 1
                
        outputStr += str(count)
        outputStr += prevLetter
        
        return outputStr