class Solution:
    def findComplement(self, num):
        #convert to binary string without the leading '0b'
        num = bin(num)[2:]
        
        output = ""
        
        #XOR each bit with 1 to flip the value
        for bit in num:
            #convert to int to XOR, then convert back to string
            bit = str(int(bit)^1)
            output += bit
            
        #convert binary to decimal
        return int(output,2)