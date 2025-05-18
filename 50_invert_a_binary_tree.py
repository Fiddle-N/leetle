# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def solve(root):
  if root is None:
    return root

  def _solve(root):
    tmp = root.left
    root.left = root.right
    root.right = tmp

    if root.left is not None:
      _solve(root.left)
    if root.right is not None:
      _solve(root.right)

  _solve(root)
  return root
