
from typing import Any, List, Generator
class TreeNode:
    def __init__(self, data: Any, left: "TreeNode" = None, right: "TreeNode" = None) -> None:
        self.data = data
        self.left = left
        self.right = right
    def __str__(self) -> None:
        return f"{self.__class__.__name__}(data={self.data}, left={self.left}, right={self.right})"
class BinarySearchTree:
    def __init__(self, tree_data: List[Any]) -> None:
        self.root = TreeNode(tree_data[0])
        for value in tree_data[1:]:
            self.add(value)
    def add(self, value: Any) -> None:
        stack = [self.root]
        while stack:
            root = stack.pop()
            if value <= root.data:
                if root.left is None:
                    root.left = TreeNode(value)
                    return
                stack.append(root.left)
            else:
                if root.right is None:
                    root.right = TreeNode(value)
                    return
                stack.append(root.right)
    @classmethod
    def inorder(cls, node: "TreeNode") -> Generator[Any, None, None]:
        if node != None:
            for left in cls.inorder(node.left):
                yield left
            yield node
            for right in cls.inorder(node.right):
                yield right
    def __iter__(self):
        return iter((n.data for n in self.inorder(self.root)))
    def data(self) -> "TreeNode":
        return self.root
    def sorted_data(self) -> List[int]:
        return list(self)