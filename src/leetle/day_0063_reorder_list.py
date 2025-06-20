class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"TreeNode({self.val}, {self.next})"


def parse(head):
    llist = []
    while True:
        if head is None:
            return llist
        llist.append(head.val)
        head = head.next


def reorder(parsed):
    length = len(parsed)

    start = 0
    end = length - 1

    head = ListNode()
    curr = head
    while True:
        after = ListNode()
        curr.val = parsed[start]
        next_ = ListNode(val=parsed[end], next=after)
        curr.next = next_
        curr = after

        start += 1
        end -= 1
        if start == end:
            after.val = parsed[start]
            return head
        if start >= end:
            next_.next = None
            return head


def solve(head):
    if head is None:
        return head
    parsed = parse(head)
    if len(parsed) == 1:
        return head
    return reorder(parsed)
