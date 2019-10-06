class Solution:
    def deleteNode(self, node):
        #given access to only the node to be deleted and not the prior node, copy value of next node to this node
        node.val = node.next.val
        #delete the next node instead
        node.next = node.next.next