class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # initialize output list
        output = [False]*len(candies)
        
        # get max value of current list before extra candies
        currMax = max(candies)
        currKid = 0 # iterator for kids
        
        for kid in candies:
            if (kid+extraCandies) >= currMax:
                output[currKid] = True
            currKid += 1
        
        return output