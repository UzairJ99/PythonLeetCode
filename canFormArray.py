class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        arrMap = {}
        
        for i, val in enumerate(arr):
            arrMap[val] = i
        
        for piece in pieces:
            if (arrMap.get(piece[0]) != None):
                ind = arrMap[piece[0]] # get the corresponding position of the number from the arrMap
            else:
                return False
            
            if len(piece) > 1:
                for i in range(len(piece)):
                    # out of bounds check
                    if (ind >= len(arr)):
                        return False
                    
                    # match indices
                    if (arr[ind] != piece[i]):
                        return False
                    ind += 1 # increment the pointer index
                    
                    
        
        return True