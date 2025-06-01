# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def solve(head, n):
    llist = []
    curr = head
    while True:
        llist.append(curr)
        if curr.next is None:
            break
        curr = curr.next

    if len(llist) == 1:
        assert n == 1
        return None

    if n == 1:
        llist[-2].next = None
    elif n == len(llist):
        head = llist[1]
    else:
        left_idx = -n - 1
        right_idx = -n + 1
        llist[left_idx].next = llist[right_idx]

    return head
