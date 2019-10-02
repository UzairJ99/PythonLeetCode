class Solution:
    def repeatedNTimes(self, A):
        #size is 2N
        N = len(A)//2  
        elements = {}
        #count occurances of each element and store them in a dictionary
        for x in A:
            if elements.get(x):
                elements[x] += 1
            else:
                elements[x] = 1
        #check which value matches N
        for x in elements.keys():
            if elements[x] == N:
                return x
            else:
                continue