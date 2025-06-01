class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def unpack(head):
  unpacked = []
  curr = head
  while curr is not None:
    unpacked.append(curr)
    curr = curr.next
  return unpacked


def solve(head, k):
  if head is None:
    return None
  unpacked = unpack(head)

  llen = len(unpacked)
  mod_k = k % llen

  if mod_k == 0:
    return head

  left, right = unpacked[:-mod_k], unpacked[-mod_k:]

  left[-1].next = None
  right[-1].next = left[0]

  return right[0]
