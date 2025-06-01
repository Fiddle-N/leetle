# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def solve(head, n):
    l = []
    curr = head
    while True:
        l.append(curr)
        if curr.next is None:
            break
        curr = curr.next

    if len(l) == 1:
        assert n == 1
        return None

    if n == 1:
        l[-2].next = None
    elif n == len(l):
        head = l[1]
    else:
        left_idx = -n - 1
        right_idx = -n + 1
        l[left_idx].next = l[right_idx]

    return head
