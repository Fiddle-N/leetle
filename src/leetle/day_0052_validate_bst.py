# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math


class Solution:
    def __init__(self):
        self._is_valid = True

    def solve(self, root):
        self._solve(root)
        return self._is_valid

    def _solve(self, root, lbound=-math.inf, ubound=math.inf):
        if not lbound < root.val < ubound:
            self._is_valid = False
            return

        if root.left is not None:
            self._solve(root.left, lbound=lbound, ubound=root.val)
            if not self._is_valid:
                return
        if root.right is not None:
            self._solve(root.right, lbound=root.val, ubound=ubound)
            if not self._is_valid:
                return


def solve(root):
    if root is None:
        # somehow no tree at all is a valid tree
        return True
    return Solution().solve(root)
