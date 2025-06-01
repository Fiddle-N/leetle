class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val}, {self.left}, {self.right})"


def parse(tree):
    # not required for puzzle
    parent = TreeNode(tree.pop(0))
    child_nodes = [parent]

    while tree:
        node = child_nodes.pop(0)
        if node is None:
            continue

        left_val = tree.pop(0)
        right_val = tree.pop(0) if tree else None

        left = TreeNode(left_val) if left_val is not None else None
        right = TreeNode(right_val) if right_val is not None else None

        node.left = left
        node.right = right

        child_nodes.extend([left, right])

    return parent


def traverse_preorder(parsed_tree):
    if parsed_tree is None:
        return []

    preorder_tree = []

    def traverse(node):
        preorder_tree.append(node.val)
        if node.left is not None:
            traverse(node.left)
        if node.right is not None:
            traverse(node.right)

    traverse(parsed_tree)
    return preorder_tree


def solve(root: TreeNode):
    return traverse_preorder(parsed_tree)
