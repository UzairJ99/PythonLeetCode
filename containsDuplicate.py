class Solution:
    def containsDuplicate(self, nums):
        count = {}
        for n in nums:
            #if element is already in the dictionary, break
            if count.get(n):
                return True
            else:
                count[n] = 1
        return False