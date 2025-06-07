class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SumLeftLeaves:
    def __init__(self):
        self._lsum = 0

    def _solve(self, node, side=None):
        if node is None:
            return True
        no_lchild = self._solve(node.left, "left")
        no_rchild = self._solve(node.right, "right")
        is_leaf = no_lchild and no_rchild
        if side == "left" and is_leaf:
            self._lsum += node.val
        return False

    def solve(self, node):
        self._solve(node)
        return self._lsum


def solve(root):
    if root is None:
        return 0
    return SumLeftLeaves().solve(root)
