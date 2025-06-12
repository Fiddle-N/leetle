class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head, n):
  prev = None
  curr = head
  while curr is not None:
    if curr.val == n:
      if curr == head:
        head = curr.next
      else:
        # non-head
        prev.next = curr.next
    prev = curr
    curr = curr.next
  return head
