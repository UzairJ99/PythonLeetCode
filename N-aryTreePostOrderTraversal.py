class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root):
        nodes = [root]
        #return values
        output = []

        if root is None:
            return None

        #DFS
        while len(nodes) > 0:
            node = nodes.pop()
            #place this value into our return list
            output.append(node.val)
            #add the children
            nodes += node.children

        #reverse our output list which makes it postorder traversal
        output = output[::-1]
        return output