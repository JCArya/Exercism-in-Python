
class Node:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous
    def __str__(self):
        return f"node:{self.value}"
class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.len = 0
    def push(self, value):
        """Inserts value at the back of the list
        """
        # create new node
        new = Node(value, None, self.last)
        was_empty = self.is_empty()
        # link it with existing nodes
        if not was_empty:
            previous = self.last
            previous.next = new
        # adjust list pointers
        self.last = new
        if was_empty:
            self.first = self.last
        self.len += 1
        return self.last.value
    def pop(self):
        """Removes value from the back of the list
        """
        # get last value for later return
        return_value = self.last.value
        # update existing nodes and adjuts list pointers
        if self.last.previous != None:
            new_last = self.last.previous
            new_last.next = None
            self.last = new_last
        else:
            self.last = None
            self.first = None
        self.len -= 1
        return return_value
    def shift(self):
        """Removes value from the front
        """
        # get last value for later return
        return_value = self.first.value
        # update existing nodes and adjuts list pointers
        if self.first.next != None:
            new_first = self.first.next
            new_first.previous = None
            self.first = new_first
        else:
            self.first = self.last = None
        self.len -= 1
        return return_value
    def unshift(self, value):
        """Inserts value at the front
        """
        # create new node
        new = Node(value, self.first, None)
        was_empty = self.is_empty()
        # link it with existing nodes
        if not was_empty:
            previous_first = self.first
            previous_first.previous = new
        # adjust list pointers
        self.first = new
        if was_empty:
            self.last = self.first
        self.len += 1
        return new
    def is_empty(self):
        print(self)
        return self.first == self.last == None
    def __len__(self):
        return self.len
    def __str__(self):
        nodes = ""
        for node in self:
            nodes += f"{node}->"
        return f"first: {self.first}\nlast:{self.last}\nnodes:\n{nodes}"
    def __iter__(self):
        return LinkedListIterator(self)
class LinkedListIterator:
    def __init__(self, linked_list):
        self.linked_list = linked_list
        self.current_node = linked_list.first
    def __next__(self):
        if self.current_node != None:
            return_node = self.current_node
            self.current_node = self.current_node.next
            return return_node.value
        else:
            raise StopIteration
