class Solution:
    def hammingDistance(self, x, y):
        #count the different bits. we use XOR to get a resultant binary number
        count, diff = 0, bin(x ^ y)
        
        for bit in diff:
            #each 1 means x and y had different bit values at the position
            if bit == '1':
                count += 1
        
        return count