class LinkedList:
  def __init__(self, val):
    self.val = val
    self.next = None

  def mergeTwoLists(self, l1, l2):
    pointer1 = l1
    pointer2 = l2
    l3 = LinkedList(None)
    #iterate through each list
    while (pointer1 is not None) and (pointer2 is not None):
        if pointer1.val < pointer2.val:
          l3.addNode(pointer1.val)
          pointer1 = pointer1.next
        elif pointer1.val > pointer2.val:
          l3.addNode(pointer2.val)
          pointer2 = pointer2.next
        #if both are the same, iterate both pointers
        elif pointer1.val == pointer2.val:
          l3.addNode(pointer1.val)
          l3.addNode(pointer2.val)
          pointer1 = pointer1.next
          pointer2 = pointer2.next
    #iterate through second list if first list comes to an end
    if pointer1 == None:
        while pointer2 is not None:
            l3.addNode(pointer2.val)
            pointer2 = pointer2.next
    #iterate through first list if second list comes to an end
    elif pointer2 == None:
        while pointer1 is not None:
            l3.addNode(pointer1.val)
            pointer1 = pointer1.next
    l3.printList()

  def addNode(self, a):
    #check if empty
    if self.val == None:
        self.val = a
        self.next = None
    else:
        a = LinkedList(a)
        pointer = self
        #find last node
        while pointer.next is not None:
            pointer = pointer.next
        #replace the None object with the new node
        pointer.next = a
  
  def printList(self):
    print("\nPrinting list: \n")
    if self.val == None:
      pointer = self.next
    else:
      pointer = self
    while pointer is not None:
      print(pointer.val, end=" ")
      pointer = pointer.next

def main():
  l1 = LinkedList(None)
  l1.addNode(1)
  l1.addNode(2)
  l1.addNode(4)
  l1.printList()
  l2 = LinkedList(None)
  l2.addNode(1)
  l2.addNode(3)
  l2.addNode(5)
  l2.addNode(6)
  l2.printList()
  l1.mergeTwoLists(l1,l2)

if __name__ == "__main__":
  main()