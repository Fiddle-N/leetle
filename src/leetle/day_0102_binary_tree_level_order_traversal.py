from collections import deque
from dataclasses import dataclass


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


@dataclass
class QueueItem:
  node: TreeNode
  level: int


class LevelOrderTraversal:

  def __init__(self):
    self.output = []

  def traverse(self, root):
    q = deque([QueueItem(node=root, level=0)])
    while q:
      item = q.pop()
      self._add(item)
      if item.node.left is not None:
        q.appendleft(
          QueueItem(
            node=item.node.left,
            level=item.level + 1
          )
        )
      if item.node.right is not None:
        q.appendleft(
          QueueItem(
            node=item.node.right,
            level=item.level + 1
          )
        )
    return self.output
      

  def _add(self, item):
    try:
      self.output[item.level]
    except IndexError:
      # assume the previous level is present
      self.output.append([])
    finally:
      self.output[item.level].append(item.node.val)
      

def solve(root):
  if root is None:
    return []
  return LevelOrderTraversal().traverse(root)
