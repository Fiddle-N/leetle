class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _parse(node):
    if node is None:
        return None
    if node.left is None and node.right is None:
        return [[node.val]]
    children = []
    if (lchildren := _parse(node.left)) is not None:
        children.extend(lchildren)
    if (rchildren := _parse(node.right)) is not None:
        children.extend(rchildren)
    for num in children:
        num.append(node.val)
    return children


def parse(root):
    return [int("".join(str(digit) for digit in reversed(num))) for num in _parse(root)]


def solve(root):
    if root is None:
        return 0
    return sum(parse(root))
