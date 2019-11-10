class Solution:
    def removeOuterParentheses(self, S):
        newBrackets = []
        count = 0
        for bracket in S:
            if bracket == "(":
                count += 1
            else:
                count -= 1
            if (count != 1 and bracket =="(") or (count != 0 and bracket == ")"):
                newBrackets.append(bracket)
            else:
                pass
        
        return ''.join(newBrackets)