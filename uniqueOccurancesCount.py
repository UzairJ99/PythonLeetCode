class Solution:
    def uniqueOccurrences(self, arr):
        count = {}
        #count occurances of each item and add to dictionary
        for x in arr:
            if (checkKey(count,x)):
                count[x] += 1
            else:
                count[x] = 1
        print(count)
        
        unique = []
        #check if dictionary contains only unique values
        for x in count.keys():
            if count[x] in unique:
                return False
            else:
                unique.append(count[x])
        return True

#check if key exists       
def checkKey(d,x):
    if d.get(x):
        return True
    else:
        return False