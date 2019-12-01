class Solution:
    def intersection(self, nums1, nums2):
        output = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        #find shorter list
        if len(nums1) >= len(nums2):
            largerList = nums1
            shorterList = nums2
        else:
            largerList = nums2
            shorterList = nums1

        #binarySearch function
        def binarySearch(arr, val):
            hi, lo = len(arr)-1, 0
            mid = (hi + lo) // 2

            while lo <= hi:
                mid = (hi + lo) // 2
                if arr[mid] == val:
                    return val 
                elif val > arr[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            #not found
            return -1

        #iterate binary search for each element in shorter list on the longer list
        for element in shorterList:
            foundElement = binarySearch(largerList, element)
            if foundElement != -1:
                output.append(foundElement)
                #remove from the list so we get the duplicates as well
                largerList.remove(element)
            else:
                continue

        return output