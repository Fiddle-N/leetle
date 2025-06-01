# Singly Linked List Definition
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(head):
    if head is None:
        return head
    new_head = None
    curr = head
    while curr is not None:
        next_ = ListNode(curr.val)
        next_.next = new_head
        new_head = next_
        curr = curr.next
    return new_head
