class Solution:
    def countBits(self, num: int) -> List[int]:
        # memoization technique storing previously computed values
        storage = [0]*(num+1)

        # find previous 2^n value
        prev2n = 0
        n = 0
        
        for index in range(num+1):
            digit = index
            # every 2^n will have one 1 so we can fill those values in immediately
            if digit == 2**n:
                storage[index] = 1
                prev2n = 2**n
                n += 1
                continue
            
            # difference between current value and last 2^n value
            diff = digit - prev2n
            # pull values from storage to compute current value
            storage[index] = storage[prev2n] + storage[diff]
        
        return storage