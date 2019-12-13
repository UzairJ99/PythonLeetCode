class Solution:
    def missingNumber(self, nums):
        #make a list of size of length of list nums + missing value
        indices = ['x']*(len(nums)+1)
        
        if nums == []:
            return 0
        
        #fill up the indices list
        for val in nums:
            indices[val] = val
        
        #look for any unchanged x values
        for val in range(len(indices)):
            if indices[val] == 'x':
                return val