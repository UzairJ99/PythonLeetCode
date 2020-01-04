class Solution:
    def removeElement(self, nums, val):
        anchor = 0
        pointer = 0

        for i in range(len(nums)):
            if nums[i] == val:
                anchor = i
                pointer = i+1
                #search for next value that isn't val
                while pointer < len(nums) and nums[pointer] == val:
                    pointer += 1
                #return list upto last changed element
                if pointer >= len(nums):
                    return len(nums[:anchor])
                else:
                    #swap the values
                    nums[anchor], nums[pointer] = nums[pointer], nums[anchor]