class Solution:
    def sortedSquares(self, A):
        B = [x*x for x in A]
        B = sorted(B)
        return B