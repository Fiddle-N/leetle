class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SumLeaves:
    def __init__(self):
        self._sum = 0

    def _solve(self, node):
        if node is None:
            return True
        no_lchild = self._solve(node.left)
        no_rchild = self._solve(node.right)
        is_leaf = no_lchild and no_rchild
        if is_leaf:
            self._sum += node.val
        return False

    def solve(self, node):
        self._solve(node)
        return self._sum


def solve(root):
    if root is None:
        return 0
    return SumLeaves().solve(root)
