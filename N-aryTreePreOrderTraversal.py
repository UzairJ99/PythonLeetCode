class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root):
        nodes = [root]
        output = []

        if root is None:
            return None

        #DFS
        while len(nodes) > 0:
            node = nodes.pop()
            output.append(node.val)
            #Reverse the children list because we want output from left to right, not right to left
            nodes += node.children[::-1]

        return output