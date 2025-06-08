class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse_postorder(parsed_tree):
    if parsed_tree is None:
        return []

    postorder_tree = []

    def traverse(node):
        if node is None:
            return
        traverse(node.left)
        traverse(node.right)
        postorder_tree.append(node.val)
        
    traverse(parsed_tree)
    return postorder_tree


def solve(root: TreeNode):
    return traverse_postorder(root)
