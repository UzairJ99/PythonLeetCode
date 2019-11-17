class Solution:
    def peakIndexInMountainArray(self, A):
        lo, hi = 0, len(A)-1
        mid = (lo+hi)//2

        while (lo <= hi):
            mid = (lo+hi)//2

            #check if middle is greater than both sides
            if A[mid] >= A[mid-1] and A[mid] >= A[mid+1]:
                return mid
            #check the right side of the array
            elif A[mid] < A[mid+1]:
                lo = mid+1
            #check the left side of the array
            else:
                hi = mid-1

        return 0     