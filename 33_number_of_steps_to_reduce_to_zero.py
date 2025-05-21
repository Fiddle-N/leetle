def solve(num):
  steps = 0
  curr = num
  while True:
    if curr == 0:
      return steps
    elif curr % 2 != 0:
      # odd
      curr -= 1
    else:
      # even
      curr /= 2
    steps += 1
