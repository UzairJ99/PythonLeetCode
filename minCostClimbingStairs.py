class Solution:
    def minCostClimbingStairs(self, cost):
        #dynamic programming array
        dp = [0]*len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        
        for i in range(2,len(cost)):
            #get minimum cost of current step plus either 1 step or 2 steps back
            dp[i] = min(dp[i-1]+cost[i], dp[i-2]+cost[i])
            
        #take the smaller of the last two steps since either one can lead to the end in 1 or 2 jumps
        return min(dp[-1], dp[-2])