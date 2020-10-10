class Solution:
    def fib(self, N: int) -> int:
        if (N <= 1):
            return N
        return self.memoize(N)
    
    def memoize(self, N):
        memory = [0, 1]
        memory += [0]*(N-1) # create space for the remaining values
        
        for i in range(2, N+1):
            memory[i] = memory[i-1] + memory[i-2]
        
        return memory[N]