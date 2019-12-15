class Solution:
    def hammingWeight(self, n):
        count = 0
        #XOR each bit with 0
        for bit in str(n):
            #1^1= 1 which will add to the count of 1s
            count += (int(bit)^0)
            
        return count