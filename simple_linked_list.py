
class Node:
    def __init__(self, value):
        self.data = value
        self.next_node = None
    def value(self):
        return self.data
    def next(self):
        return self.next_node
class LinkedList:
    def __init__(self, values=[]):
        self.length = 0
        self.start = None
        if values:
            for i in values:
                self.push(i)
        print(self)
    def __str__(self):
        lkls = []
        if self.length == 0:
            return str(lkls)
        lkls.append(self.start.data)
        if self.length == 1:  
            pass
        else:
            node = self.start
            while node.next_node:
                node = node.next_node
                lkls.append(node.data)
        return str(f'elts: {self.length}, head is {self.start.data} -> {lkls}')
    def __iter__(self):
        node = self.start
        while node is not None:
            yield node.data
            node = node.next_node
    def __len__(self):
        return self.length
    def head(self):
        if self.length == 0: raise EmptyListException("The list is empty.")
        return self.start
    def push(self, value):
        if value is None: return
        print(f'push {value}')
        node = Node(value)
        node.next_node = self.start
        self.start = node
        self.length += 1
    def pop(self):
        print(f'pop')
        if self.length == 0:
            raise EmptyListException("The list is empty.")
        if self.length == 1:
            node = self.start
            self.start = None
        else:
            node = self.start
            self.start = node.next_node
        self.length -= 1
        return node.data
    def reversed(self):
        values = list(self)
        return LinkedList(values)
class EmptyListException(Exception):
    def __init__(self, message):
        self.message = message