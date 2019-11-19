class Solution:
    def sortArrayByParityII(self, A):
        output, i = [0]*len(A), 0
        #loop through A
        for digit in A:
            #check even
            if digit % 2 == 0:
                output[i] = digit
                i += 2
        #reset i for odd indices now
        i = 1
        for digit in A:
            #check odd
            if digit % 2 != 0:
                output[i] = digit
                i += 2
        
        return output