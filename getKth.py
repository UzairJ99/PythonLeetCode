class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # make list from lo to hi
        input = list(range(lo, hi+1))
        
        output = []
        
        def getPower(val, currPower):
            if val == 1:
                output.append(currPower)
                return None
            elif val % 2 == 0:
                # if even divide by 2, add to power, and recurse
                val /= 2
                currPower += 1
                getPower(val, currPower)
            else:
                val = (3 * val) + 1
                currPower += 1
                getPower(val, currPower)
        
        # create hashmap for mapping output and input
        outputDict = dict.fromkeys(input, 0)
        
        # get the power of each input number
        for num in input:
            getPower(num, 0)

        # match output with input in order
        for keys, vals in enumerate(outputDict.keys()):
            outputDict[vals] = output[keys]
        
        # sort
        outputDict = sorted((value, key) for (key, value) in outputDict.items())
        
        # return the kth value from output dictionary as a single number
        return outputDict[k-1][1]