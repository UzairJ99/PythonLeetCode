class Solution:
    def twoSum(self, numbers, target):
        keys = {}
        for index, value in enumerate(numbers):
            #check if the difference value is already in the dictionary
            if (target - value) in keys: 
                #if the difference already exists in the dictionary, we've found a pair
                break
            else:
                #add the value to the dictionary; non-zero indexed
                keys[value] = index + 1
        #sort the indices
        return sorted([keys[target - value], index + 1])