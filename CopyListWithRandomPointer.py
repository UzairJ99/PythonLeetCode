# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        #empty list case guard
        if not head:
            return None

        pointer = head
        storage = {}

        #copy node values into hashmap
        while pointer:
            storage[pointer] = Node(pointer.val)
            pointer = pointer.next

        #reset pointer to original list
        pointer = head
        while pointer:
            if pointer.random:
                storage[pointer].random = storage[pointer.random]
            if pointer.next:
                storage[pointer].next = storage[pointer.next]
            pointer = pointer.next

        return storage[head]