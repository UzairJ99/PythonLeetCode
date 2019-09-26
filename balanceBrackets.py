class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x == "(" or x == "{" or x == "[":
                stack.append(x)
            else:
                if len(stack) == 0:
                    return False
                else:
                    y = stack[len(stack)-1]
                if (x == ")" and y == "(") or (x == "}" and y == "{") or (x == "]" and y == "["):
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        else:
            return True