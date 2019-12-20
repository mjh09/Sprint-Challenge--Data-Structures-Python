class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = LinkedList()

    def push(self, value):
        self.size+=1
        self.storage.add_to_head(value)

    def pop(self):
      if self.size >0:
        self.size-=1
        #del self.storage.head
        self.storage.head = self.storage.head.next_node

    def len(self):
        # return self.size
        return self.storage.length

class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    rll = Stack()
    rrll =Stack()
    while self.head is not None:
        rll.push(self.head.value)
        self.head = self.head.get_next()
    while rll.size >=1:
        rrll.push(rll.storage.head.value)
        rll.pop()
    while rrll.size>=1:
        self.add_to_head(rrll.storage.head.value)
        rrll.pop()