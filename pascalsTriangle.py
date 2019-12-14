class Solution:
    def generate(self, numRows):
        output = []

        for level in range(1, numRows+1):
            row = [0]*level
            row[0], row[-1] = 1, 1
            #use two pointers
            if level > 2:
                p1, p2 = 0, 1
                for digit in range(1,level-1):
                    row[digit] = output[level-2][p1] + output[level-2][p2]
                    p1 += 1
                    p2 += 1
            output.append(row)
        return output