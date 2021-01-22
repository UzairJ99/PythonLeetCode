class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store indices and values into hashmap
        indices = {}
        for i, val in enumerate(nums):
            indices[val] = i
        
        for j, val in enumerate(nums):
            diff = target - val
            # check if difference exists in the list and return the index pair
            if (indices.get(diff) != None and indices.get(diff) != j):
                return [j, indices.get(diff)]