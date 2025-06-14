import itertools


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def unpack(head):
    unpacked = []
    curr = head
    while curr is not None:
        unpacked.append(curr.val)
        curr = curr.next
    return unpacked


def swap(node_list):
    # can't use itertools.grouped
    # as using Py3.10
    new_l = []
    l_iter = iter(node_list)
    while batch := list(itertools.islice(l_iter, 2)):
        new_l.extend(reversed(batch))
    return new_l


def repack(node_list):
    head = ListNode()
    curr = None
    for num in node_list:
        if curr is None:
            curr = head
        else:
            curr.next = ListNode()
            curr = curr.next
        curr.val = num
    return head


def solve(head):
    if head is None:
        return None
    unpacked = unpack(head)
    swapped = swap(unpacked)
    return repack(swapped)
