
class Node():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
    def get_info(self):
        left = None if self.left == None else self.left.get_info()
        right = None if self.right == None else self.right.get_info()
        return {'value': self.value, 'left': left, 'right': right}
class Zipper:
    build_tree = lambda data: None if data == None else Node(data['value'], Zipper.build_tree(data['left']), Zipper.build_tree(data['right']))
    def __init__(self, tree):
        self.focus = self.root = Zipper.build_tree(tree)
        self.tracker = ''
    @staticmethod
    def from_tree(tree):
        return Zipper(tree)
    def value(self):
        return self.focus.value
    def set_value(self, value):
        self.focus.value = value
        return self
    def left(self):
        if self.focus.left == None:
            return None
        self.tracker += 'L'
        self.focus = self.focus.left
        return self
    def set_left(self, data):
        self.focus.left = None if data == None else Zipper.build_tree(data)
        return self
    def right(self):
        if self.focus.right == None:
            return None
        self.tracker += 'R'
        self.focus = self.focus.right
        return self
    def set_right(self, data):
        self.focus.right = None if data == None else Zipper.build_tree(data)
        return self
    def up(self):
        if len(self.tracker) == 0:
            return None
        else:
            self.focus = self.root
            track = self.tracker[:-1]
            self.tracker = ''
            for char in track:
                if char == 'R':
                    self.right()
                elif char == 'L':
                    self.left()
            return self
                    
    def to_tree(self):
        return self.root.get_info()
