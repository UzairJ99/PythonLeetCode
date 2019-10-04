class Solution:
    def judgeCircle(self, moves):
        x = 0
        y = 0
        #change coordinates upon move
        for move in moves:
            if move == "U":
                y += 1
            elif move == "D":
                y -= 1
            elif move == "R":
                x += 1
            elif move == "L":
                x -= 1
        #check if final coordinates are the origin
        return (x == 0 and y == 0)