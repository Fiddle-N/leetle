# Binary Tree Definition
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#        self.right = right

def solve(root):
  if root is None:
    return 0
  return max(
    solve(root.left),
    solve(root.right)
  ) + 1
