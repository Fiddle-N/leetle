from collections import deque
from dataclasses import dataclass

@dataclass
class Item:
  product: int
  digits: list[int]

def solve(product):
  if product < 0:
    return -1
  if product == 0:
    return 10
  if product == 1:
    return 1
  q = deque([
    Item(
      product,
      digits=[]
    )
  ])
  while True:
    if not q:
      return -1
    item = q.popleft()
    for div in range(2, 10):
      quot, mod = divmod(item.product, div)
      if mod != 0:
        continue
      digits = item.digits.copy()
      digits.append(div)
      if quot == 1:
        return int(
          ''.join(
            str(digit) 
            for digit in digits
          )
        )
      q.append(
        Item(
          quot,
          digits
        )
      )
