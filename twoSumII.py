class Solution:
    def twoSum(self, numbers, target):
        sums = {}
        output = []
        
        #iterate through each element and perform (target - element)
        for element in numbers:
            #hashmap that element to it's difference in a dictionary (element: target-element)
            sums[element] = target - element

        #iterate through the list
        for key in numbers:
            #if the value exists both in the sums and nums dictionary, get the index
            if sums.get(key) in numbers:
                output.append(numbers.index(key)+1)
                numbers.remove(key) #remove the element to avoid duplicate indices
                output.append(numbers.index(sums.get(key))+2) #increment index after above deletion
                break #ignore duplicate pairings
            else:
                continue
        
        return output       