class Solution:
    def groupThePeople(self, groupSizes):
        output = []

        groups = {}
        #iterate through list
        for i, size in enumerate(groupSizes):
            #create a key in a dictionary whose value is a list of length
            # [3] : [0,1,2]
            if groups.get(size):
                if len(groups[size]) < size:
                    groups[size] += [i]
                if len(groups[size]) == size:
                    #when key's list is full, append to output list and key's empty the list
                    # [3] : [x,x,x]
                    output.append(groups[size])
                    groups[size] = []
            else:
                #create key with list
                groups[size] = [i]
                if len(groups[size]) == size:
                    #when key's list is full, append to output list and key's empty the list
                    # [3] : [x,x,x]
                    output.append(groups[size])
                    groups[size] = [i]

        return output