class Solution:
    def singleNumber(self, nums):
        #concept: a XOR b XOR a = b
        x = 0
        
        #iterate through each bit and XOR it with the previous result value
        for bit in nums:
            x = x ^ bit
          
        #this leaves us with the unique bit because all the duplicates zeroed out
        return x