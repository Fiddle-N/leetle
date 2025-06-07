def solve(arr):
  max_ = -1
  replaced = []
  for num in reversed(arr):
    replaced.append(max_)
    if num > max_:
      max_ = num
  return list(reversed(replaced))
