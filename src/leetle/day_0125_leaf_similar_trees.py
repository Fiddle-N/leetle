class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(root):
    if root is None or root.left is None or root.right is None:
        return True
    return False
