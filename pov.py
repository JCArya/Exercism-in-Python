from json import dumps
class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children or []
    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}
    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)
    def __repr__(self):
        return f'Tree({self.label}, {[c.label for c in self.children]})'
    def __lt__(self, other):
        return self.label < other.label
    def __eq__(self, other):
        return self.__dict__() == other.__dict__()
    @staticmethod
    def from_path(path, parent=None):
        children = [c for c in path[0].children if not parent or c.label != parent.label]
        if len(path) > 1:
            children.append(Tree.from_path(path[1:], path[0]))
        return Tree(path[0].label, children)
    def from_pov(self, from_node):
        if from_node == self.label:
            return self
        if path := self.dfs(from_node):
            return Tree.from_path(path[::-1])
        raise ValueError("Tree could not be reoriented")
    def path_to(self, from_node, to_node):
        tree_from_node = self.from_pov(from_node)
        if path := tree_from_node.dfs(to_node):
            return [t.label for t in path]
        raise ValueError("No path found")
    def dfs(self, to_node):
        if self.label == to_node:
            return [self]
        for child in self.children:
            if subp := child.dfs(to_node):
                return [self] + subp
        return None
