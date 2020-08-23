class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # create empty output list
        outputStr = [""]*len(indices)
        
        # assign letter with index according to indices
        for ind, place in enumerate(indices):
            outputStr[place] = s[ind]
        
        # return as string
        return ''.join(outputStr)