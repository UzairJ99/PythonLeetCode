class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zeroProduct, numOfZeros = 1, 1, 0
        productArray = []
        
        for num in nums:
            if (num != 0):
                zeroProduct *= num
            else:
                numOfZeros += 1
            if (numOfZeros > 1):
                zeroProduct = 0
            product *= num
            
        for num in nums:
            if (num == 0):
                productArray.append(zeroProduct)
            else:
                productArray.append(product//num)
                
        return productArray
