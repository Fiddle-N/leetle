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


def interleave(node_list):
    new_l = []
    for idx in range(0, len(node_list), 2):
        new_l.append(node_list[idx])
    for idx in range(1, len(node_list), 2):
        new_l.append(node_list[idx])
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
    swapped = interleave(unpacked)
    return repack(swapped)
