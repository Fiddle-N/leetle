class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val}, {self.left}, {self.right})"


def traverse_preorder(parsed_tree):
    if parsed_tree is None:
        return []

    preorder_tree = []

    def traverse(node):
        if node is None:
            return
        preorder_tree.append(node.val)
        traverse(node.left)
        traverse(node.right)

    traverse(parsed_tree)
    return preorder_tree


def solve(root: TreeNode):
    return traverse_preorder(root)
