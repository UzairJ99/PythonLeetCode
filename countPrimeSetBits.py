import math

class Solution:
    def countPrimeSetBits(self, L, R):
        count = 0

        #find each number that has a prime number of set bits (set = 1)
        for numbers in range(L, R+1):
            setBits = bin(numbers).count('1')
            if self.isPrime(setBits):
                count += 1

        return count
    
    def isPrime(self, num):
        #anything less than 1 inclusive is not a prime number
        if num <= 1:
            return False

        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        
        return True