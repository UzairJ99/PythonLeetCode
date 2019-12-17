class Solution:
    def merge(self, nums1, m, nums2, n):
        #keep 3 pointers, 1 to the end of the array, and 1 for each list
        p1, p2, p3 = m-1, n-1, -1
        
        #check for empty lists
        if m == 0:
            nums1[:] = nums2[:]
        elif n == 0:
            nums1[:] = nums1[:]
        else:
            #increment till one of the two pointers reach past their end
            while (p1 >= 0 and p2 >= 0):
                if nums2[p2] > nums1[p1]:
                    #append greater element to end of nums1
                    nums1[p3] = nums2[p2] 
                    #decrement pointers but keep p1 where it is to compare to next element
                    p2 -= 1
                    p3 -= 1
                elif nums1[p1] > nums2[p2]:
                    #append greater element to end of nums1
                    nums1[p3] = nums1[p1] 
                    #decrement pointers but keep p1 where it is to compare to next element
                    p1 -= 1
                    p3 -= 1
                else:
                    #append both elements to end of nums1
                    nums1[p3] = nums1[p1] 
                    nums1[p3-1] = nums1[p1]
                    #decrement all pointers
                    p2 -= 1
                    p1 -= 1
                    p3 -= 2 #decrement twice because they were duplicates

            #copy over all remaining nums2 elements into their respective place in nums1
            if p1 < 0:
                nums1[:p3+1] = nums2[:p2+1]
            elif p2 < 0:
                #copy over all remaining nums1 elements into their respective place in nums1
                nums1[:p3+1] = nums1[:p1+1]