class Solution:
    def fizzBuzz(self, n):
        output = []
        for num in range(1,n+1):
            #multiple of both 3 and 5
            if (num % 3 == 0 and num % 5 == 0):
                output.append("FizzBuzz")
            #multiple of 3
            elif num % 3 == 0:
                output.append("Fizz")
            #multiple of 5
            elif num % 5 == 0:
                output.append("Buzz")
            else:
                output.append(str(num))
                
        return output