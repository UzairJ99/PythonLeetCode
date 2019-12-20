class Solution:
    def permute(self, nums):
        output = []
        
        def permuteString(a, l, r): 
            if l==r: 
                output.append(a[:])
            else: 
                for i in range(l,r+1): 
                    a[l], a[i] = a[i], a[l] #fix one digit
                    permuteString(a, l+1, r) #permute remaining digits
                    a[l], a[i] = a[i], a[l] #backtrack upto previous level of tree
                    
        permuteString(nums,0,len(nums)-1)
        return output