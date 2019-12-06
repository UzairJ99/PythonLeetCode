class Solution:
    def reverseString(self, s):
        #pointers to first and last characters
        c1, c2 = 0, len(s)-1

        while c1 < c2:
            #swap the characters
            s[c1], s[c2] = s[c2], s[c1]
            #increment the pointers
            c1 += 1
            c2 -= 1