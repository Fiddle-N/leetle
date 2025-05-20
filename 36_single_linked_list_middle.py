# Singly Linked List Definition
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def solve(head):
  parsed = []
  curr = head
  while True:
    parsed.append(curr)
    if curr.next is None:
      break
    curr = curr.next
  return parsed[len(parsed) // 2]
