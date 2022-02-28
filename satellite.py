
def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    elif set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")
    elif len(set(preorder)) != len(preorder):
        raise ValueError("traversals must contain unique items")
    tree, _ = search(preorder, inorder, 0)
    return tree
def search(preorder, inorder, index):
    if index == len(preorder):
        return {}, index
    node = preorder[index]
    if node not in inorder:
        return {}, index
    else:
        i = inorder.index(node)
        left_inorder = inorder[:i]
        right_inorder = inorder[i + 1:]
        index += 1
        left, index = search(preorder, left_inorder, index)
        right, index = search(preorder, right_inorder, index)
        return {"v": inorder[i], "l": left, "r": right}, index
