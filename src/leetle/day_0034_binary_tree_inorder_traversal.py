# Binary Tree Definition
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#       self.right = right


def solve(root):
    if root is None:
        return []

    vals = []

    def _solve(root):
        if root.left is not None:
            _solve(root.left)
        vals.append(root.val)
        if root.right is not None:
            _solve(root.right)

    _solve(root)
    return vals
