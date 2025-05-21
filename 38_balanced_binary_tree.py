# Binary Tree Definition
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#       self.right = right

class NotBalanced(Exception):
  pass
  

def _solve(node):
  if node is None:
    return 0
  left = _solve(node.left)
  right = _solve(node.right)
  if abs(left - right) > 1:
    raise NotBalanced
  height = max(left, right)
  return height + 1
    

def solve(root):
  if root is None:
    return True
  
  try:
    _solve(root)
  except NotBalanced:
    return False
  return True
