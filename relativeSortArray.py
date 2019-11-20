class Solution:
    def relativeSortArray(self, arr1, arr2):
        #create a dictionary for first array
        vals = {}
        output = []
        other = []
        #create dictionary for second array
        arr2dict = dict([(x,1) for x in arr2])
        
        for dig in arr1:
            if vals.get(dig):
                vals[dig] += 1
            else:
                vals[dig] = 1
        
        #count each occurance of every key from arr2 in arr1
        for digit in arr1:
            if arr2dict.get(digit) is None:
                other.append(digit)
        
        for key in arr2:
            output += [key]*vals[key]
        
        other = sorted(other)
        output += other
        return output